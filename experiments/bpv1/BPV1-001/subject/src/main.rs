//! BPV1-001 experimental falsification instrument runner.
//!
//! EXPERIMENTAL_INSTRUMENT_NOT_CANON. The subject emits raw, implementation-
//! neutral facts only. It does not emit the oracle's PASS-oriented booleans
//! for structural claims such as "no event log" or "no exact replay".
//! `tools/bpv1/qualify_observations.py` derives the frozen observation shape
//! externally before `evaluate.py` applies the preregistered oracle.

mod engine;

use engine::{Engine, EpistemicPosition};
use serde_json::{json, Value};
use std::path::PathBuf;

const SCENARIO_ID: &str = "BPV1-001-cross-lineage-bounded-accountability-v1";
const PLAN_SHA256: &str = "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0";

const SLOT_FX01_UNKNOWN: usize = 0;
const SLOT_FX02_ROLES: usize = 1;
const SLOT_FX03_CONTEXT_A: usize = 2;
const SLOT_FX03_CONTEXT_B: usize = 3;
const SLOT_FX04_REVISION: usize = 4;
const SLOT_FX05_PLURALITY: usize = 5;
const SLOT_FX07_TRUNCATION: usize = 6;
const SLOT_FX08_FORGED_AUTHORITY: usize = 7;
const SLOT_FX09_WITHHELD_COUNTEREVIDENCE: usize = 8;
const SLOT_FX10_COMPACTED_LOSS: usize = 9;
const SLOT_FX12_DIVERGENT_A: usize = 10;
const SLOT_FX12_DIVERGENT_B: usize = 11;

const REVISION_CYCLES: u64 = 16;
const CHECKPOINT_CYCLES: [u64; 3] = [4, 8, 16];

fn position_name(position: EpistemicPosition) -> &'static str {
    match position {
        EpistemicPosition::Unknown => "UNKNOWN",
        EpistemicPosition::Supported => "SUPPORTED",
        EpistemicPosition::Refuted => "REFUTED",
        EpistemicPosition::ScopedUncertain => "SCOPED_UNCERTAIN",
        EpistemicPosition::UnresolvedPlurality => "UNRESOLVED_PLURALITY",
        EpistemicPosition::Unsupported => "UNSUPPORTED",
    }
}

fn run_cycle(engine: &mut Engine, cycle: u64) {
    for slot in 0..engine::ACTIVE_CLAIM_SLOTS {
        match slot {
            SLOT_FX01_UNKNOWN => {
                if cycle == 1 {
                    engine.admit_or_revise(
                        slot,
                        "unresolved-proposition-U",
                        "CTX-DEFAULT",
                        "SRC-NONE",
                        vec![],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Unknown,
                        false,
                    );
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX02_ROLES => {
                engine.admit_or_revise(
                    slot,
                    "role-structured-proposition",
                    "CTX-DEFAULT",
                    &format!("SRC-{cycle}"),
                    vec![format!("EVIDENCE-{cycle}-a"), format!("EVIDENCE-{cycle}-b")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
            SLOT_FX03_CONTEXT_A => {
                engine.admit_or_revise(
                    slot,
                    "shared-proposition-text",
                    "CTX-A",
                    &format!("SRC-A-{cycle}"),
                    vec![format!("EVIDENCE-A-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
            SLOT_FX03_CONTEXT_B => {
                engine.admit_or_revise(
                    slot,
                    "shared-proposition-text",
                    "CTX-B",
                    &format!("SRC-B-{cycle}"),
                    vec![format!("EVIDENCE-B-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Refuted,
                    false,
                );
            }
            SLOT_FX04_REVISION => {
                engine.admit_or_revise(
                    slot,
                    &format!("revised-proposition-v{cycle}"),
                    "CTX-DEFAULT",
                    &format!("SRC-{cycle}"),
                    vec![format!("EVIDENCE-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
            SLOT_FX05_PLURALITY => {
                if cycle == 1 {
                    engine.admit_plurality(
                        slot,
                        "contested-proposition",
                        "CTX-CONTESTED",
                        &[
                            ("SRC-CLAIM-A", "EVIDENCE-CLAIM-A", "AUTH-TRUSTED"),
                            ("SRC-CLAIM-B", "EVIDENCE-CLAIM-B", "AUTH-ALT"),
                        ],
                    );
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX07_TRUNCATION => {
                if cycle == 1 {
                    engine.admit_or_revise(
                        slot,
                        "durable-proposition",
                        "CTX-DEFAULT",
                        "SRC-DURABLE",
                        vec!["EVIDENCE-DURABLE".to_string()],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else if cycle == 8 {
                    engine.simulate_truncation(slot);
                } else if cycle == 9 {
                    engine.detect_and_handle_corruption(slot);
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX08_FORGED_AUTHORITY => {
                if cycle == 1 {
                    engine.admit_or_revise(
                        slot,
                        "authority-guarded-proposition",
                        "CTX-DEFAULT",
                        "SRC-GUARDED",
                        vec!["EVIDENCE-GUARDED".to_string()],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else if cycle == 8 {
                    engine.admit_or_revise(
                        slot,
                        "authority-guarded-proposition-FORGED",
                        "CTX-DEFAULT",
                        "SRC-ATTACKER",
                        vec!["EVIDENCE-FORGED".to_string()],
                        "AUTH-FORGED-EVIL",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX09_WITHHELD_COUNTEREVIDENCE => {
                if cycle == 1 {
                    engine.admit_or_revise(
                        slot,
                        "counterevidence-pending-proposition",
                        "CTX-DEFAULT",
                        "SRC-PARTIAL",
                        vec!["EVIDENCE-PARTIAL".to_string()],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Supported,
                        true,
                    );
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX10_COMPACTED_LOSS => {
                engine.admit_or_revise(
                    slot,
                    &format!("compaction-observed-proposition-v{cycle}"),
                    "CTX-DEFAULT",
                    &format!("SRC-{cycle}"),
                    vec![format!("EVIDENCE-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
            SLOT_FX12_DIVERGENT_A => {
                if cycle <= 3 {
                    engine.admit_or_revise(
                        slot,
                        &format!("convergent-value-intermediate-{cycle}"),
                        "CTX-CONVERGENT",
                        "SRC-A",
                        vec!["EVIDENCE-A".to_string()],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else if cycle == 4 {
                    engine.admit_or_revise(
                        slot,
                        "convergent-final-value",
                        "CTX-CONVERGENT",
                        "SRC-A",
                        vec!["EVIDENCE-A".to_string()],
                        "AUTH-TRUSTED",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else {
                    engine.touch(slot);
                }
            }
            SLOT_FX12_DIVERGENT_B => {
                if cycle == 1 {
                    engine.admit_or_revise(
                        slot,
                        "convergent-final-value",
                        "CTX-CONVERGENT",
                        "SRC-B",
                        vec!["EVIDENCE-B-alternate".to_string()],
                        "AUTH-ALT",
                        EpistemicPosition::Supported,
                        false,
                    );
                } else {
                    engine.touch(slot);
                }
            }
            _ => {
                engine.admit_or_revise(
                    slot,
                    &format!("bulk-proposition-slot{slot}-v{cycle}"),
                    "CTX-BULK",
                    &format!("SRC-BULK-{cycle}"),
                    vec![format!("EVIDENCE-BULK-{cycle}")],
                    "AUTH-TRUSTED",
                    EpistemicPosition::Supported,
                    false,
                );
            }
        }
    }
    engine.compact_cycle(cycle);
}

fn current_raw(engine: &Engine, slot: usize) -> Value {
    match engine.slots[slot].current.as_ref() {
        Some(version) => json!({
            "version_id": version.version_id,
            "proposition": version.proposition,
            "context": version.context,
            "source": version.source,
            "evidence": version.evidence,
            "authority": version.authority,
            "epistemic_position": position_name(version.epistemic_position),
            "predecessor_version_id": version.predecessor_version_id,
        }),
        None => Value::Null,
    }
}

fn retained_identities(engine: &Engine) -> Vec<String> {
    let mut identities = Vec::new();
    for slot in &engine.slots {
        if let Some(current) = &slot.current {
            identities.push(format!("slot-{}:v{}", slot.slot_id, current.version_id));
        }
        for predecessor in &slot.detailed_predecessors {
            identities.push(format!("slot-{}:v{}", slot.slot_id, predecessor.version_id));
        }
    }
    identities.sort();
    identities
}

fn build_raw_observations(engine: &Engine, checkpoints: &[(u64, usize)]) -> Value {
    let fx02 = current_raw(engine, SLOT_FX02_ROLES);
    let fx04_slot = &engine.slots[SLOT_FX04_REVISION];
    let fx05_slot = &engine.slots[SLOT_FX05_PLURALITY];
    let fx06_witnesses: Vec<Value> = engine
        .loss_witnesses
        .iter()
        .map(|witness| json!({
            "witness_id": witness.witness_id,
            "affected_claim_identities": witness.affected_claim_identities,
            "compacted_count": witness.compacted_count,
            "reason": witness.reason,
            "basis_authority": witness.basis_authority,
            "emitted_at_mutation": witness.emitted_at_mutation,
        }))
        .collect();
    let detail_counts: Vec<usize> = engine
        .slots
        .iter()
        .map(|slot| slot.detailed_predecessors.len())
        .collect();
    let compacted_summary_counts: Vec<usize> = engine
        .slots
        .iter()
        .map(|slot| slot.compacted_summaries.len())
        .collect();
    let accountable_slot_count = engine
        .slots
        .iter()
        .filter(|slot| slot.current.is_some() || !slot.plurality.is_empty())
        .count();
    let checkpoint_values: Vec<Value> = checkpoints
        .iter()
        .map(|(mutation, bytes)| json!({"mutation": mutation, "durable_bytes": bytes}))
        .collect();

    json!({
        "protocol": "nk-bpv1-raw-observations/1",
        "scenario_id": SCENARIO_ID,
        "plan_sha256": PLAN_SHA256,
        "fixtures": {
            "BPV1-FX01-UNKNOWN-NOT-FALSE": {
                "current": current_raw(engine, SLOT_FX01_UNKNOWN),
            },
            "BPV1-FX02-ROLE-NONCONFLATION": {
                "current": fx02,
            },
            "BPV1-FX03-CONTEXT-BINDING": {
                "a": current_raw(engine, SLOT_FX03_CONTEXT_A),
                "b": current_raw(engine, SLOT_FX03_CONTEXT_B),
            },
            "BPV1-FX04-REVISION-SUPERSESSION": {
                "current": current_raw(engine, SLOT_FX04_REVISION),
                "detailed_predecessor_version_ids": fx04_slot.detailed_predecessors.iter().map(|v| v.version_id).collect::<Vec<_>>(),
                "compacted_summary_version_ids": fx04_slot.compacted_summaries.iter().map(|v| v.version_id).collect::<Vec<_>>(),
            },
            "BPV1-FX05-UNRESOLVED-PLURALITY": {
                "current_present": fx05_slot.current.is_some(),
                "candidates": fx05_slot.plurality.iter().map(|candidate| json!({
                    "version_id": candidate.version.version_id,
                    "proposition": candidate.version.proposition,
                    "context": candidate.version.context,
                    "source": candidate.version.source,
                    "authority": candidate.version.authority,
                    "epistemic_position": position_name(candidate.version.epistemic_position),
                })).collect::<Vec<_>>(),
            },
            "BPV1-FX06-BOUNDED-COMPACTION": {
                "retained_detail_per_slot": engine::RETAINED_DETAIL_PER_SLOT,
                "retained_identities": retained_identities(engine),
                "detail_counts": detail_counts,
                "compacted_summary_counts": compacted_summary_counts,
                "loss_witnesses": fx06_witnesses,
                "loss_witness_rollup": engine.loss_witness_rollup,
            },
            "BPV1-FX07-TRUNCATION-ROLLBACK": {
                "slot_corrupted": engine.slots[SLOT_FX07_TRUNCATION].corrupted,
                "corruption_records": engine.corruption_records.iter().filter(|record| record.slot == SLOT_FX07_TRUNCATION).map(|record| json!({
                    "slot": record.slot,
                    "detected_at_mutation": record.detected_at_mutation,
                    "description": record.description,
                })).collect::<Vec<_>>(),
            },
            "BPV1-FX08-FORGED-AUTHORITY": {
                "current": current_raw(engine, SLOT_FX08_FORGED_AUTHORITY),
                "rejected_attempts": engine.rejected_authority_attempts.iter().filter(|attempt| attempt.slot == SLOT_FX08_FORGED_AUTHORITY).map(|attempt| json!({
                    "attempted_authority": attempt.attempted_authority,
                    "attempted_at_mutation": attempt.attempted_at_mutation,
                })).collect::<Vec<_>>(),
            },
            "BPV1-FX09-WITHHELD-COUNTEREVIDENCE": {
                "current": current_raw(engine, SLOT_FX09_WITHHELD_COUNTEREVIDENCE),
            },
            "BPV1-FX10-DECLARED-LOSS-AND-UNSUPPORTED": {
                "detailed_predecessor_count": engine.slots[SLOT_FX10_COMPACTED_LOSS].detailed_predecessors.len(),
                "compacted_summary_count": engine.slots[SLOT_FX10_COMPACTED_LOSS].compacted_summaries.len(),
                "loss_witness_record_count": engine.loss_witness_record_count(),
            },
            "BPV1-FX11-NON-EVENT-HISTORY": {
                "active_slot_count": engine::ACTIVE_CLAIM_SLOTS,
                "accountable_slot_count": accountable_slot_count,
            },
            "BPV1-FX12-HIDDEN-SEMANTIC-DIVERGENCE": {
                "a": current_raw(engine, SLOT_FX12_DIVERGENT_A),
                "b": current_raw(engine, SLOT_FX12_DIVERGENT_B),
            },
        },
        "workload": {
            "mutation_count": engine.mutation_count,
            "checkpoints": checkpoint_values,
        },
    })
}

fn main() {
    let mut engine = Engine::new();
    let mut checkpoints: Vec<(u64, usize)> = Vec::new();

    for cycle in 1..=REVISION_CYCLES {
        run_cycle(&mut engine, cycle);
        if CHECKPOINT_CYCLES.contains(&cycle) {
            checkpoints.push((engine.mutation_count, engine.durable_state_bytes()));
        }
    }

    let observations = build_raw_observations(&engine, &checkpoints);
    let args: Vec<String> = std::env::args().collect();
    let output_path = args
        .iter()
        .position(|arg| arg == "--output")
        .and_then(|index| args.get(index + 1))
        .map(PathBuf::from);
    let rendered = serde_json::to_string_pretty(&observations).expect("raw observations must serialize");

    match output_path {
        Some(path) => {
            if let Some(parent) = path.parent() {
                std::fs::create_dir_all(parent).expect("create output dir");
            }
            std::fs::write(&path, rendered).expect("write raw observations file");
            eprintln!("wrote raw observations to {}", path.display());
        }
        None => println!("{rendered}"),
    }
}
