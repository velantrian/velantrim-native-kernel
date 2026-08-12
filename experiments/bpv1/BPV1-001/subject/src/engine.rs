//! BPV1-001 bounded epistemic store.
//!
//! EXPERIMENTAL_INSTRUMENT_NOT_CANON. The store is derived from the
//! preregistered problem-level obligations, not from the current
//! Python/Event/reducer/Receipt/SQL lineage.

use serde::Serialize;
use std::collections::{HashSet, VecDeque};

pub const ACTIVE_CLAIM_SLOTS: usize = 32;
pub const RETAINED_DETAIL_PER_SLOT: usize = 2;
pub const CRASH_JOURNAL_MAX_ENTRIES: usize = 8;
/// The preregistered BPV1-001 cap is 32 retained witness records. Once the
/// detailed witness set would exceed the cap, older witnesses are folded into
/// one bounded per-slot rollup record rather than silently dropped.
pub const LOSS_WITNESS_MAX_RECORDS: usize = 32;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
pub enum EpistemicPosition {
    Unknown,
    Supported,
    Refuted,
    ScopedUncertain,
    UnresolvedPlurality,
    Unsupported,
}

impl EpistemicPosition {
    fn digest_tag(self) -> &'static str {
        match self {
            Self::Unknown => "UNKNOWN",
            Self::Supported => "SUPPORTED",
            Self::Refuted => "REFUTED",
            Self::ScopedUncertain => "SCOPED_UNCERTAIN",
            Self::UnresolvedPlurality => "UNRESOLVED_PLURALITY",
            Self::Unsupported => "UNSUPPORTED",
        }
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct ClaimVersion {
    pub version_id: u64,
    pub proposition: String,
    pub context: String,
    pub source: String,
    pub evidence: Vec<String>,
    pub authority: String,
    pub epistemic_position: EpistemicPosition,
    pub predecessor_version_id: Option<u64>,
    pub created_at_mutation: u64,
    /// Local corruption detector only; never a cross-lineage identity or a
    /// hash-chain/history commitment.
    pub content_digest: u64,
}

impl ClaimVersion {
    fn hash_part(hash: &mut u64, bytes: &[u8]) {
        // Length-prefix each part so concatenation cannot hide boundaries.
        for byte in (bytes.len() as u64).to_le_bytes() {
            *hash ^= byte as u64;
            *hash = hash.wrapping_mul(0x100000001b3);
        }
        for byte in bytes {
            *hash ^= *byte as u64;
            *hash = hash.wrapping_mul(0x100000001b3);
        }
    }

    fn compute_digest(&self) -> u64 {
        let mut hash: u64 = 0xcbf29ce484222325;
        Self::hash_part(&mut hash, self.proposition.as_bytes());
        Self::hash_part(&mut hash, self.context.as_bytes());
        Self::hash_part(&mut hash, self.source.as_bytes());
        for evidence in &self.evidence {
            Self::hash_part(&mut hash, evidence.as_bytes());
        }
        Self::hash_part(&mut hash, self.authority.as_bytes());
        Self::hash_part(&mut hash, self.epistemic_position.digest_tag().as_bytes());
        Self::hash_part(
            &mut hash,
            self.predecessor_version_id
                .map(|value| value.to_string())
                .unwrap_or_else(|| "NONE".to_string())
                .as_bytes(),
        );
        hash
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct PluralityCandidate {
    pub version: ClaimVersion,
}

#[derive(Debug, Clone, Serialize)]
pub struct CompactedPredecessorSummary {
    pub version_id: u64,
    pub proposition_context: String,
    pub reason: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct LossWitness {
    pub witness_id: u64,
    pub affected_claim_identities: Vec<String>,
    pub compacted_count: u32,
    pub reason: String,
    pub basis_authority: String,
    pub emitted_at_mutation: u64,
}

#[derive(Debug, Clone, Serialize, Default)]
pub struct LossWitnessRollupEntry {
    pub slot_id: usize,
    pub compacted_count: u64,
    pub first_version_id: u64,
    pub last_version_id: u64,
}

#[derive(Debug, Clone, Serialize, Default)]
pub struct LossWitnessRollup {
    pub first_witness_id: Option<u64>,
    pub last_witness_id: Option<u64>,
    pub compacted_count: u64,
    pub reason: String,
    pub basis_authority: String,
    /// At most one entry per fixed claim slot, so this summary is bounded by
    /// ACTIVE_CLAIM_SLOTS rather than by the number of compactions.
    pub entries: Vec<LossWitnessRollupEntry>,
}

impl LossWitnessRollup {
    pub fn is_empty(&self) -> bool {
        self.compacted_count == 0
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct CorruptionRecord {
    pub slot: usize,
    pub detected_at_mutation: u64,
    pub description: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct RejectedAuthorityAttempt {
    pub slot: usize,
    pub attempted_authority: String,
    pub attempted_at_mutation: u64,
}

#[derive(Debug, Clone, Serialize)]
pub struct CrashJournalEntry {
    pub mutation_index: u64,
    pub summary: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct ClaimSlot {
    pub slot_id: usize,
    pub current: Option<ClaimVersion>,
    pub plurality: Vec<PluralityCandidate>,
    pub detailed_predecessors: VecDeque<ClaimVersion>,
    pub compacted_summaries: Vec<CompactedPredecessorSummary>,
    pub corrupted: bool,
}

impl ClaimSlot {
    fn new(slot_id: usize) -> Self {
        Self {
            slot_id,
            current: None,
            plurality: Vec::new(),
            detailed_predecessors: VecDeque::new(),
            compacted_summaries: Vec::new(),
            corrupted: false,
        }
    }
}

pub struct Engine {
    pub slots: Vec<ClaimSlot>,
    pub trusted_authorities: HashSet<String>,
    pub loss_witnesses: VecDeque<LossWitness>,
    pub loss_witness_rollup: LossWitnessRollup,
    pub corruption_records: Vec<CorruptionRecord>,
    pub rejected_authority_attempts: Vec<RejectedAuthorityAttempt>,
    pub crash_journal: VecDeque<CrashJournalEntry>,
    pub next_version_id: u64,
    pub next_witness_id: u64,
    pub mutation_count: u64,
}

pub enum MutationOutcome {
    Applied,
    RejectedForgedAuthority,
}

impl Engine {
    pub fn new() -> Self {
        let mut trusted_authorities = HashSet::new();
        trusted_authorities.insert("AUTH-TRUSTED".to_string());
        trusted_authorities.insert("AUTH-ALT".to_string());
        trusted_authorities.insert("BPV1-CLEANUP-AUTHORITY".to_string());
        Self {
            slots: (0..ACTIVE_CLAIM_SLOTS).map(ClaimSlot::new).collect(),
            trusted_authorities,
            loss_witnesses: VecDeque::new(),
            loss_witness_rollup: LossWitnessRollup::default(),
            corruption_records: Vec::new(),
            rejected_authority_attempts: Vec::new(),
            crash_journal: VecDeque::new(),
            next_version_id: 1,
            next_witness_id: 1,
            mutation_count: 0,
        }
    }

    fn journal(&mut self, summary: String) {
        if self.crash_journal.len() >= CRASH_JOURNAL_MAX_ENTRIES {
            self.crash_journal.pop_front();
        }
        self.crash_journal.push_back(CrashJournalEntry {
            mutation_index: self.mutation_count,
            summary,
        });
    }

    fn fresh_version_id(&mut self) -> u64 {
        let id = self.next_version_id;
        self.next_version_id += 1;
        id
    }

    pub fn admit_or_revise(
        &mut self,
        slot_id: usize,
        proposition: &str,
        context: &str,
        source: &str,
        evidence: Vec<String>,
        authority: &str,
        epistemic_position: EpistemicPosition,
        counterevidence_withheld: bool,
    ) -> MutationOutcome {
        self.mutation_count += 1;
        if !self.trusted_authorities.contains(authority) {
            self.rejected_authority_attempts.push(RejectedAuthorityAttempt {
                slot: slot_id,
                attempted_authority: authority.to_string(),
                attempted_at_mutation: self.mutation_count,
            });
            self.journal(format!("REJECTED forged authority attempt on slot {slot_id}"));
            return MutationOutcome::RejectedForgedAuthority;
        }

        let resolved_position = if counterevidence_withheld {
            EpistemicPosition::ScopedUncertain
        } else {
            epistemic_position
        };
        let version_id = self.fresh_version_id();
        let predecessor_id = self.slots[slot_id].current.as_ref().map(|v| v.version_id);
        let mut version = ClaimVersion {
            version_id,
            proposition: proposition.to_string(),
            context: context.to_string(),
            source: source.to_string(),
            evidence,
            authority: authority.to_string(),
            epistemic_position: resolved_position,
            predecessor_version_id: predecessor_id,
            created_at_mutation: self.mutation_count,
            content_digest: 0,
        };
        version.content_digest = version.compute_digest();

        let slot = &mut self.slots[slot_id];
        if let Some(previous) = slot.current.take() {
            slot.detailed_predecessors.push_front(previous);
        }
        slot.current = Some(version);
        self.journal(format!("REVISE slot {slot_id} -> version {version_id}"));
        MutationOutcome::Applied
    }

    pub fn admit_plurality(
        &mut self,
        slot_id: usize,
        proposition: &str,
        context: &str,
        candidates: &[(&str, &str, &str)],
    ) {
        self.mutation_count += 1;
        for (source, evidence, authority) in candidates {
            let version_id = self.fresh_version_id();
            let mut version = ClaimVersion {
                version_id,
                proposition: proposition.to_string(),
                context: context.to_string(),
                source: source.to_string(),
                evidence: vec![evidence.to_string()],
                authority: authority.to_string(),
                epistemic_position: EpistemicPosition::UnresolvedPlurality,
                predecessor_version_id: None,
                created_at_mutation: self.mutation_count,
                content_digest: 0,
            };
            version.content_digest = version.compute_digest();
            self.slots[slot_id].plurality.push(PluralityCandidate { version });
        }
        self.journal(format!("PLURALITY slot {slot_id}"));
    }

    pub fn touch(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        self.journal(format!("TOUCH slot {slot_id}"));
    }

    pub fn simulate_truncation(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        if let Some(version) = self.slots[slot_id].current.as_mut() {
            version.content_digest ^= 0xdead_beef_dead_beef;
        }
        self.journal(format!("SIMULATE_TRUNCATION slot {slot_id}"));
    }

    pub fn detect_and_handle_corruption(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        let mutation_count = self.mutation_count;
        let slot = &mut self.slots[slot_id];
        if let Some(version) = slot.current.as_ref() {
            if version.compute_digest() != version.content_digest {
                slot.corrupted = true;
                self.corruption_records.push(CorruptionRecord {
                    slot: slot_id,
                    detected_at_mutation: mutation_count,
                    description: "semantic content digest mismatch".to_string(),
                });
            }
        }
        self.journal(format!("RECOVERY_CHECK slot {slot_id}"));
    }

    fn parse_identity(identity: &str) -> Option<(usize, u64)> {
        let (slot, version) = identity.strip_prefix("slot-")?.split_once(":v")?;
        Some((slot.parse().ok()?, version.parse().ok()?))
    }

    fn roll_up_witness(&mut self, witness: LossWitness) {
        let rollup = &mut self.loss_witness_rollup;
        if rollup.first_witness_id.is_none() {
            rollup.first_witness_id = Some(witness.witness_id);
            rollup.reason = witness.reason.clone();
            rollup.basis_authority = witness.basis_authority.clone();
        }
        rollup.last_witness_id = Some(witness.witness_id);
        rollup.compacted_count += u64::from(witness.compacted_count);

        for identity in witness.affected_claim_identities {
            let Some((slot_id, version_id)) = Self::parse_identity(&identity) else {
                continue;
            };
            if let Some(entry) = rollup.entries.iter_mut().find(|entry| entry.slot_id == slot_id) {
                entry.compacted_count += 1;
                entry.first_version_id = entry.first_version_id.min(version_id);
                entry.last_version_id = entry.last_version_id.max(version_id);
            } else if rollup.entries.len() < ACTIVE_CLAIM_SLOTS {
                rollup.entries.push(LossWitnessRollupEntry {
                    slot_id,
                    compacted_count: 1,
                    first_version_id: version_id,
                    last_version_id: version_id,
                });
            }
        }
        rollup.entries.sort_by_key(|entry| entry.slot_id);
    }

    fn push_loss_witness(&mut self, witness: LossWitness) {
        loop {
            let rollup_records = usize::from(!self.loss_witness_rollup.is_empty());
            if self.loss_witnesses.len() + rollup_records + 1 <= LOSS_WITNESS_MAX_RECORDS {
                break;
            }
            if let Some(oldest) = self.loss_witnesses.pop_front() {
                self.roll_up_witness(oldest);
            } else {
                break;
            }
        }
        self.loss_witnesses.push_back(witness);
    }

    pub fn compact_cycle(&mut self, cycle: u64) {
        let mut affected_identities = Vec::new();
        let mut compacted_count: u32 = 0;
        for slot in &mut self.slots {
            while slot.detailed_predecessors.len() > RETAINED_DETAIL_PER_SLOT {
                if let Some(dropped) = slot.detailed_predecessors.pop_back() {
                    slot.compacted_summaries.push(CompactedPredecessorSummary {
                        version_id: dropped.version_id,
                        proposition_context: format!("{}::{}", dropped.proposition, dropped.context),
                        reason: "BOUNDED_RETENTION_COMPACTION".to_string(),
                    });
                    while slot.compacted_summaries.len() > RETAINED_DETAIL_PER_SLOT {
                        slot.compacted_summaries.remove(0);
                    }
                    affected_identities.push(format!("slot-{}:v{}", slot.slot_id, dropped.version_id));
                    compacted_count += 1;
                }
            }
        }
        if compacted_count > 0 {
            let witness_id = self.next_witness_id;
            self.next_witness_id += 1;
            self.push_loss_witness(LossWitness {
                witness_id,
                affected_claim_identities: affected_identities,
                compacted_count,
                reason: "BOUNDED_RETENTION_COMPACTION".to_string(),
                basis_authority: "BPV1-CLEANUP-AUTHORITY".to_string(),
                emitted_at_mutation: self.mutation_count,
            });
        }
        self.journal(format!("COMPACT_CYCLE {cycle} compacted={compacted_count}"));
    }

    pub fn total_detailed_predecessors(&self) -> usize {
        self.slots.iter().map(|slot| slot.detailed_predecessors.len()).sum()
    }

    pub fn loss_witness_record_count(&self) -> usize {
        self.loss_witnesses.len() + usize::from(!self.loss_witness_rollup.is_empty())
    }

    pub fn durable_state_bytes(&self) -> usize {
        serde_json::to_vec(&self.durable_snapshot())
            .map(|bytes| bytes.len())
            .unwrap_or(usize::MAX)
    }

    pub fn durable_snapshot(&self) -> DurableSnapshot {
        DurableSnapshot {
            slots: self.slots.clone(),
            loss_witnesses: self.loss_witnesses.iter().cloned().collect(),
            loss_witness_rollup: self.loss_witness_rollup.clone(),
            corruption_records: self.corruption_records.clone(),
            rejected_authority_attempts: self.rejected_authority_attempts.clone(),
            crash_journal: self.crash_journal.iter().cloned().collect(),
        }
    }
}

#[derive(Debug, Clone, Serialize)]
pub struct DurableSnapshot {
    pub slots: Vec<ClaimSlot>,
    pub loss_witnesses: Vec<LossWitness>,
    pub loss_witness_rollup: LossWitnessRollup,
    pub corruption_records: Vec<CorruptionRecord>,
    pub rejected_authority_attempts: Vec<RejectedAuthorityAttempt>,
    pub crash_journal: Vec<CrashJournalEntry>,
}

#[cfg(test)]
mod tests {
    use super::*;

    fn seeded_engine() -> Engine {
        let mut engine = Engine::new();
        engine.admit_or_revise(
            0,
            "semantic-proposition",
            "CTX",
            "SRC",
            vec!["EVIDENCE-A".to_string()],
            "AUTH-TRUSTED",
            EpistemicPosition::Supported,
            false,
        );
        engine
    }

    #[test]
    fn evidence_mutation_is_detected() {
        let mut engine = seeded_engine();
        engine.slots[0].current.as_mut().unwrap().evidence[0] = "EVIDENCE-TAMPERED".to_string();
        engine.detect_and_handle_corruption(0);
        assert!(engine.slots[0].corrupted);
    }

    #[test]
    fn epistemic_position_mutation_is_detected() {
        let mut engine = seeded_engine();
        engine.slots[0].current.as_mut().unwrap().epistemic_position = EpistemicPosition::Refuted;
        engine.detect_and_handle_corruption(0);
        assert!(engine.slots[0].corrupted);
    }

    #[test]
    fn witness_storage_remains_bounded_beyond_preregistered_workload() {
        let mut engine = Engine::new();
        for cycle in 1..=96_u64 {
            for slot in 0..ACTIVE_CLAIM_SLOTS {
                engine.admit_or_revise(
                    slot,
                    &format!("slot-{slot}-cycle-{cycle}"),
                    "CTX-BOUND",
                    "SRC-BOUND",
                    vec![format!("EVIDENCE-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
            engine.compact_cycle(cycle);
        }
        assert!(engine.loss_witness_record_count() <= LOSS_WITNESS_MAX_RECORDS);
        assert!(!engine.loss_witness_rollup.is_empty());
        assert!(engine.loss_witness_rollup.compacted_count > 0);
        assert!(engine.loss_witness_rollup.entries.len() <= ACTIVE_CLAIM_SLOTS);
    }
}
