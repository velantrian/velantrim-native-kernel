//! BPV1-001 bounded epistemic store.
//!
//! EXPERIMENTAL_INSTRUMENT_NOT_CANON. This engine is derived from the
//! problem-level obligations in `docs/research/BPV1_PREREGISTRATION.json`,
//! not from the current Python/Event/reducer/Receipt/SQL lineage. It does
//! not import, translate, or reuse any of those forms.
//!
//! Design summary:
//! - A fixed number of claim slots hold the current accountable state.
//! - Claim/reality: propositions are representations, never equated with
//!   objective truth.
//! - Source, Evidence, and Authority are distinct, non-conflated fields.
//! - Context scopes the same proposition text into materially different
//!   claims.
//! - Unknown is a first-class epistemic position, never coerced to false.
//! - Revision keeps a bounded amount of predecessor detail; older detail is
//!   compacted with an explicit loss witness, never silently dropped.
//! - Conflicting claims without an authorized resolution rule remain an
//!   unresolved plurality rather than picking a silent winner.
//! - There is no authoritative per-operation append log and no exact-replay
//!   requirement: current accountability is derived from the current
//!   bounded state, not from replaying history.
//! - A bounded crash journal exists only to aid local recovery; it never
//!   defines semantic history.

use serde::Serialize;
use std::collections::{HashSet, VecDeque};

pub const ACTIVE_CLAIM_SLOTS: usize = 32;
pub const RETAINED_DETAIL_PER_SLOT: usize = 2;
pub const CRASH_JOURNAL_MAX_ENTRIES: usize = 8;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
pub enum EpistemicPosition {
    Unknown,
    Supported,
    Refuted,
    ScopedUncertain,
    UnresolvedPlurality,
    /// Not reached by the scripted BPV1-001 workload in this run; kept for
    /// model completeness (a claim invalidated by detected corruption would
    /// use this position rather than silently keeping its prior one).
    #[allow(dead_code)]
    Unsupported,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
pub enum PreservationState {
    Full,
    Lossy,
    /// Not reached by the scripted BPV1-001 workload in this run; kept for
    /// model completeness alongside `Lossy`/`Indeterminate` per the plan's
    /// declared preservation-state vocabulary.
    #[allow(dead_code)]
    Unsupported,
    #[allow(dead_code)]
    Indeterminate,
}

/// A single version of a claim: a scoped representation, never claimed to
/// equal objective reality.
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
    /// Content digest used only to detect corruption of durable bytes; not
    /// an authoritative per-operation append-log entry and not required for
    /// exact replay.
    pub content_digest: u64,
}

impl ClaimVersion {
    fn compute_digest(&self) -> u64 {
        // Simple content digest (FNV-1a) over the semantically material
        // fields. Used only for local corruption detection, not as a
        // cross-lineage identity or hash-chain claim.
        let mut hash: u64 = 0xcbf29ce484222325;
        for part in [
            self.proposition.as_str(),
            self.context.as_str(),
            self.source.as_str(),
            self.authority.as_str(),
        ] {
            for byte in part.bytes() {
                hash ^= byte as u64;
                hash = hash.wrapping_mul(0x100000001b3);
            }
        }
        hash
    }
}

/// A candidate in an unresolved plurality: kept live because no preregistered
/// Authority rule resolves the conflict.
#[derive(Debug, Clone, Serialize)]
pub struct PluralityCandidate {
    pub version: ClaimVersion,
}

/// A bounded summary of compacted predecessor detail. The full body is
/// dropped; only enough identity remains to prove the compaction happened
/// and to bind it to a witness.
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

/// One claim slot: current accountable version, bounded detailed lineage,
/// and compacted-lineage summaries. Slots holding an unresolved plurality
/// instead carry `plurality` candidates and no single `current`.
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
        ClaimSlot {
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
    pub loss_witnesses: Vec<LossWitness>,
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
        Engine {
            slots: (0..ACTIVE_CLAIM_SLOTS).map(ClaimSlot::new).collect(),
            trusted_authorities,
            loss_witnesses: Vec::new(),
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

    /// Admit or revise a normal (non-adversarial) claim in `slot`.
    /// `counterevidence_withheld` forces the resulting position to
    /// `ScopedUncertain` even when otherwise-sufficient evidence is present.
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
            // Detail accumulates here uncompacted; only `compact_cycle` may
            // convert overflow into a compacted summary bound to an
            // explicit loss witness. Trimming here without a witness would
            // be exactly the silent-loss behavior the plan forbids.
            slot.detailed_predecessors.push_front(previous);
        }
        slot.current = Some(version);
        self.journal(format!("REVISE slot {slot_id} -> version {version_id}"));
        MutationOutcome::Applied
    }

    /// Admit two materially conflicting candidates for the same
    /// proposition/context with no preregistered Authority rule to resolve
    /// them. Both remain live; neither is silently selected as the winner.
    pub fn admit_plurality(
        &mut self,
        slot_id: usize,
        proposition: &str,
        context: &str,
        candidates: &[(&str, &str, &str)],
    ) {
        // Admitting the whole conflicting-candidate set is one mutation:
        // the semantic event is "a plurality was admitted", not one event
        // per candidate.
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
            self.journal(format!("PLURALITY_CANDIDATE slot {slot_id}"));
        }
    }

    /// A mutation that intentionally performs no semantic change, used to
    /// keep a slot's mutation count aligned with the scripted workload
    /// without disturbing its epistemic position (e.g. keeping FX01's
    /// Unknown claim genuinely unresolved).
    pub fn touch(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        self.journal(format!("TOUCH slot {slot_id} (no semantic change)"));
    }

    /// Simulate on-disk truncation/corruption of a slot's current version by
    /// invalidating its content digest without changing the recorded
    /// content, representing a partial/corrupted durable write.
    pub fn simulate_truncation(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        if let Some(version) = self.slots[slot_id].current.as_mut() {
            version.content_digest ^= 0xdead_beef_dead_beef;
        }
        self.journal(format!("SIMULATE_TRUNCATION slot {slot_id}"));
    }

    /// Attempt recovery after a possible truncation: recompute the digest
    /// and compare. On mismatch, the slot is marked corrupted and can never
    /// silently claim intact accountability again without a fresh,
    /// explicitly re-admitted claim.
    pub fn detect_and_handle_corruption(&mut self, slot_id: usize) {
        self.mutation_count += 1;
        let mutation_count = self.mutation_count;
        let slot = &mut self.slots[slot_id];
        if let Some(version) = slot.current.as_ref() {
            let expected = version.compute_digest();
            if expected != version.content_digest {
                slot.corrupted = true;
                self.corruption_records.push(CorruptionRecord {
                    slot: slot_id,
                    detected_at_mutation: mutation_count,
                    description: "content digest mismatch after simulated truncation".to_string(),
                });
            }
        }
        self.journal(format!("RECOVERY_CHECK slot {slot_id}"));
    }

    /// Compact detailed predecessor bodies outside the retention window for
    /// every slot that currently exceeds it, emitting exactly one aggregated
    /// loss witness for this cycle. Never touches `current`.
    ///
    /// `compacted_summaries` is itself bounded per slot (`RETAINED_DETAIL_PER_SLOT`
    /// most recent entries only): a summary-of-what-was-lost list that grows
    /// forever would just be an unbounded per-operation log wearing a
    /// different name. Once a compaction's loss is captured by a witness in
    /// `loss_witnesses` (the durable, bounded record of the event), an
    /// older per-version summary is not additionally required to persist
    /// forever - the plan's declared retained scope is finite.
    pub fn compact_cycle(&mut self, cycle: u64) {
        let mut affected_identities = Vec::new();
        let mut compacted_count: u32 = 0;
        for slot in self.slots.iter_mut() {
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
            self.loss_witnesses.push(LossWitness {
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
        self.slots.iter().map(|s| s.detailed_predecessors.len()).sum()
    }

    pub fn durable_state_bytes(&self) -> usize {
        // The durable, retained experiment state: current claims, bounded
        // detailed predecessors, compacted summaries, loss witnesses, and
        // the bounded crash journal. This excludes process RSS/allocator
        // overhead by construction (we measure the serialized form).
        serde_json::to_vec(&self.durable_snapshot())
            .map(|bytes| bytes.len())
            .unwrap_or(usize::MAX)
    }

    pub fn durable_snapshot(&self) -> DurableSnapshot {
        DurableSnapshot {
            slots: self.slots.clone(),
            loss_witnesses: self.loss_witnesses.clone(),
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
    pub corruption_records: Vec<CorruptionRecord>,
    pub rejected_authority_attempts: Vec<RejectedAuthorityAttempt>,
    pub crash_journal: Vec<CrashJournalEntry>,
}
