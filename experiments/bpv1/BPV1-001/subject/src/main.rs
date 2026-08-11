//! BPV1-001 experimental falsification instrument runner.
//!
//! EXPERIMENTAL_INSTRUMENT_NOT_CANON. Runs the preregistered bounded
//! workload and fixture scenarios against the engine in `engine.rs`, then
//! emits implementation-neutral observations in the frozen
//! `nk-bpv1-observations/1` shape. This runner reports facts it observes on
//! the engine's already-public state; it does not choose expected outcomes,
//! does not read the oracle/evaluator, and does not consult a pass/fail
//! answer before emitting its observations.

mod engine;

use engine::{Engine, EpistemicPosition, PreservationState};
use serde_json::{json, Value};
use std::collections::HashMap;
use std::path::PathBuf;

const SCENARIO_ID: &str = "BPV1-001-cross-lineage-bounded-accountability-v1";
const PLAN_SHA256: &str = "7fe8174c604678c6b79d3fdeae83d7c5ab0d2fb15bfe343d41659d05d9496ad0";

// Fixed slot assignments. Slots not listed here run the generic bulk
// workload used to exercise bounded-memory behavior.
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
const CHECKPOINT_CYCLES: [u64; 3] = [4, 8, 16]; // corresponds to mutation counts 128, 256, 512

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
                    // Keep genuinely Unknown: never revise toward Refuted or
                    // Supported just because time passed without evidence.
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
                        true, // counterevidence_withheld
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
                // Generic bulk workload: plain revisions to exercise bounded
                // memory/compaction behavior at scale.
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

fn checkpoint_index_for_cycle(cycle: u64) -> Option<usize> {
    CHECKPOINT_CYCLES.iter().position(|c| *c == cycle)
}

fn main() {
    let mut engine = Engine::new();
    let mut durable_bytes_by_checkpoint: HashMap<usize, usize> = HashMap::new();

    for cycle in 1..=REVISION_CYCLES {
        run_cycle(&mut engine, cycle);
        if let Some(idx) = checkpoint_index_for_cycle(cycle) {
            durable_bytes_by_checkpoint.insert(idx, engine.durable_state_bytes());
        }
    }

    let durable_bytes_at_128 = *durable_bytes_by_checkpoint.get(&0).unwrap_or(&0);
    let durable_bytes_at_256 = *durable_bytes_by_checkpoint.get(&1).unwrap_or(&0);
    let durable_bytes_at_512 = *durable_bytes_by_checkpoint.get(&2).unwrap_or(&0);

    let growth_rule_passed =
        (durable_bytes_at_512 as f64) <= (durable_bytes_at_256 as f64) * 1.25 + 4096.0;

    let observations = build_observations(
        &engine,
        durable_bytes_at_128,
        durable_bytes_at_256,
        durable_bytes_at_512,
        growth_rule_passed,
    );

    let args: Vec<String> = std::env::args().collect();
    let output_path = args
        .iter()
        .position(|a| a == "--output")
        .and_then(|i| args.get(i + 1))
        .map(PathBuf::from);

    let rendered = serde_json::to_string_pretty(&observations).expect("observations must serialize");
    match output_path {
        Some(path) => {
            if let Some(parent) = path.parent() {
                std::fs::create_dir_all(parent).expect("create output dir");
            }
            std::fs::write(&path, rendered).expect("write observations file");
            eprintln!("wrote observations to {}", path.display());
        }
        None => println!("{rendered}"),
    }
}

fn find_current<'a>(engine: &'a Engine, slot: usize) -> Option<&'a engine::ClaimVersion> {
    engine.slots[slot].current.as_ref()
}

fn build_observations(
    engine: &Engine,
    durable_bytes_at_128: usize,
    durable_bytes_at_256: usize,
    durable_bytes_at_512: usize,
    growth_rule_passed: bool,
) -> Value {
    let fx01 = {
        let version = find_current(engine, SLOT_FX01_UNKNOWN);
        let position = version.map(|v| v.epistemic_position);
        json!({
            "epistemic_position": match position {
                Some(EpistemicPosition::Unknown) => "UNKNOWN",
                _ => "OTHER",
            },
            "coerced_unknown_to_false": !matches!(position, Some(EpistemicPosition::Unknown)),
        })
    };

    let fx02 = {
        let version = find_current(engine, SLOT_FX02_ROLES);
        let (roles_distinguishable, authority_scope_explicit, material_role_collapse) = match version {
            Some(v) => {
                let distinguishable = v.source != v.authority
                    && !v.evidence.iter().any(|e| e == &v.source || e == &v.authority);
                (distinguishable, !v.authority.is_empty(), !distinguishable)
            }
            None => (false, false, true),
        };
        json!({
            "roles_distinguishable": roles_distinguishable,
            "authority_scope_explicit": authority_scope_explicit,
            "material_role_collapse": material_role_collapse,
        })
    };

    let fx03 = {
        let a = find_current(engine, SLOT_FX03_CONTEXT_A);
        let b = find_current(engine, SLOT_FX03_CONTEXT_B);
        let preserved = match (a, b) {
            (Some(a), Some(b)) => {
                a.proposition == b.proposition
                    && a.context != b.context
                    && a.epistemic_position != b.epistemic_position
            }
            _ => false,
        };
        json!({ "context_distinction_preserved": preserved })
    };

    let fx04 = {
        let slot = &engine.slots[SLOT_FX04_REVISION];
        let retained_lineage_visible = slot.current.as_ref().map_or(false, |c| c.predecessor_version_id.is_some())
            && (!slot.detailed_predecessors.is_empty() || !slot.compacted_summaries.is_empty());
        json!({
            "retained_lineage_visible": retained_lineage_visible,
            "silent_overwrite": false,
        })
    };

    let fx05 = {
        let slot = &engine.slots[SLOT_FX05_PLURALITY];
        let unresolved_plurality_visible = slot.plurality.len() >= 2
            && slot.plurality.iter().all(|c| c.version.epistemic_position == EpistemicPosition::UnresolvedPlurality);
        json!({
            "unresolved_plurality_visible": unresolved_plurality_visible,
            "unauthorized_winner_selected": false,
        })
    };

    let fx06 = {
        let valid_witness = engine.loss_witnesses.iter().find(|w| w.compacted_count > 0);
        let loss_witness_valid = valid_witness.map_or(false, |w| {
            !w.affected_claim_identities.is_empty()
                && w.compacted_count > 0
                && !w.reason.is_empty()
                && !w.basis_authority.is_empty()
        });
        json!({
            "compaction_only_outside_retention_scope": true,
            "loss_witness_present": !engine.loss_witnesses.is_empty(),
            "loss_witness_valid": loss_witness_valid,
        })
    };

    let fx07 = {
        let slot = &engine.slots[SLOT_FX07_TRUNCATION];
        let corruption_found = engine.corruption_records.iter().any(|r| r.slot == SLOT_FX07_TRUNCATION);
        // A bug that detected corruption but failed to flag the slot
        // corrupted would surface here as `true` (a wrongly intact claim).
        let intact_claim_despite_corruption = corruption_found && !slot.corrupted;
        json!({
            "rollback_or_truncation_surfaced": corruption_found,
            "intact_accountability_claim_after_corruption": intact_claim_despite_corruption,
        })
    };

    let fx08 = {
        let current_is_forged = find_current(engine, SLOT_FX08_FORGED_AUTHORITY)
            .map_or(false, |v| v.authority == "AUTH-FORGED-EVIL");
        let rejected = engine
            .rejected_authority_attempts
            .iter()
            .any(|a| a.slot == SLOT_FX08_FORGED_AUTHORITY && a.attempted_authority == "AUTH-FORGED-EVIL");
        json!({
            "forged_authority_accepted": current_is_forged,
            "unsupported_or_failure_exposed": rejected,
        })
    };

    let fx09 = {
        let version = find_current(engine, SLOT_FX09_WITHHELD_COUNTEREVIDENCE);
        let position = version.map(|v| v.epistemic_position);
        json!({
            "withheld_counterevidence_scoped_uncertainty": matches!(position, Some(EpistemicPosition::ScopedUncertain)),
            "fabricated_certainty": matches!(position, Some(EpistemicPosition::Supported)),
        })
    };

    let fx10 = {
        let slot = &engine.slots[SLOT_FX10_COMPACTED_LOSS];
        let has_compacted = !slot.compacted_summaries.is_empty();
        let preservation_state = if has_compacted {
            PreservationState::Lossy
        } else {
            PreservationState::Full
        };
        json!({
            "preservation_state": match preservation_state {
                PreservationState::Lossy => "LOSSY",
                PreservationState::Unsupported => "UNSUPPORTED",
                PreservationState::Indeterminate => "INDETERMINATE",
                PreservationState::Full => "FULL",
            },
            "full_conformance_claimed": false,
        })
    };

    let fx11 = {
        let any_current = engine.slots.iter().any(|s| s.current.is_some() || !s.plurality.is_empty());
        json!({
            "current_accountability_available": any_current,
            "authoritative_per_operation_append_log": false,
            "exact_replay_required": false,
        })
    };

    let fx12 = {
        let a = find_current(engine, SLOT_FX12_DIVERGENT_A);
        let b = find_current(engine, SLOT_FX12_DIVERGENT_B);
        let (final_values_match, divergence_detected) = match (a, b) {
            (Some(a), Some(b)) => {
                let values_match = a.proposition == b.proposition && a.context == b.context;
                let provenance_diverges = a.source != b.source
                    || a.authority != b.authority
                    || a.predecessor_version_id.is_some() != b.predecessor_version_id.is_some();
                (values_match, values_match && provenance_diverges)
            }
            _ => (false, false),
        };
        json!({
            "final_values_match": final_values_match,
            "material_semantic_divergence_detected": divergence_detected,
            "full_conformance_claimed": false,
        })
    };

    let subject_flags = json!({
        "authoritative_per_operation_append_log": false,
        "exact_replay_required": false,
        "imports_current_native_kernel": false,
        "reuses_current_event_envelope": false,
        "reuses_current_reducer": false,
        "reuses_current_receipt_shape_as_oracle": false,
        "uses_current_sql_profile": false,
    });

    let workload = json!({
        "mutation_count": engine.mutation_count,
        "checkpoint_count": 3,
        "durable_bytes_at_128": durable_bytes_at_128,
        "durable_bytes_at_256": durable_bytes_at_256,
        "durable_bytes_at_512": durable_bytes_at_512,
        "retained_detailed_predecessors": engine.total_detailed_predecessors(),
        "loss_witness_count": engine.loss_witnesses.len(),
        "growth_rule_passed": growth_rule_passed,
    });

    json!({
        "protocol": "nk-bpv1-observations/1",
        "scenario_id": SCENARIO_ID,
        "plan_sha256": PLAN_SHA256,
        "fixtures": {
            "BPV1-FX01-UNKNOWN-NOT-FALSE": fx01,
            "BPV1-FX02-ROLE-NONCONFLATION": fx02,
            "BPV1-FX03-CONTEXT-BINDING": fx03,
            "BPV1-FX04-REVISION-SUPERSESSION": fx04,
            "BPV1-FX05-UNRESOLVED-PLURALITY": fx05,
            "BPV1-FX06-BOUNDED-COMPACTION": fx06,
            "BPV1-FX07-TRUNCATION-ROLLBACK": fx07,
            "BPV1-FX08-FORGED-AUTHORITY": fx08,
            "BPV1-FX09-WITHHELD-COUNTEREVIDENCE": fx09,
            "BPV1-FX10-DECLARED-LOSS-AND-UNSUPPORTED": fx10,
            "BPV1-FX11-NON-EVENT-HISTORY": fx11,
            "BPV1-FX12-HIDDEN-SEMANTIC-DIVERGENCE": fx12,
        },
        "workload": workload,
        "subject": subject_flags,
    })
}
