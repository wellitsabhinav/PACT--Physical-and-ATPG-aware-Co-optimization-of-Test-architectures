# Canonical results and reproduction

PACT is frozen: **`PACT_GATE10A_NO_MATERIAL_PHYSICAL_IMPACT`**, recommendation **`FREEZE`**. The [README](../../README.md) is the public summary; linked original protocols, comparisons and decisions below are the evidence. Historical reports retain their then-current next steps without changing this final decision.

## Reproduction levels

| Level | Command or inputs | What it establishes |
|---|---|---|
| 1 — numerical example | [README quick start](../../README.md#level-1--lightweight-numerical-example) | Synthetic numerical search and legal topology; no EDA or physical benefit claim |
| 2 — retained evidence | `python scripts/verify_reproducibility.py` | 674 original/export bindings, Stage-A checksum/projection agreement and 18 Stage-B starts/selections replayed through independent reference/incremental evaluators |
| 2 — end-to-end records | `python scripts/verify_end_to_end.py --verification-output scratch/end_to_end_verification.json` | 12 delivered records: architectures, complete collapsed fault-class exports, recovered workloads, bound measurements and deltas |
| 3 — physical reconstruction | Frozen ODB/SDC, technology/library inputs, workloads/maps/orders and exact qualified toolchain | Re-execution of a specified physical realization; requires raw inputs beyond the lightweight checkout |

The explicit `--verification-output` keeps the new end-to-end receipt in ignored scratch storage; omitting it retains the historical behavior of rewriting `final_verification.json`. Do not commit host-specific verification receipts.

The verifiers do not launch search, ATPG or EDA. They do not remeasure Gate 10A, independently rebuild historical binaries, or derive routed measurements from predictor scores. Verify Gate 10A's final values in its bound CSV/JSON and per-run receipts; this is a separate evidence set from the 674-binding Stage-A/B verifier.

## Exact evidence by scientific stage

| Stage / claim | Canonical reports and measurements | Protocol, selection and provenance |
|---|---|---|
| Solver contracts | [Development/test scope](../development.md), [working-solver selections](../../reports/working_solver/final/) | [Architecture](../architecture/overview.md), [objectives](../methodology/objectives.md) |
| Stage A: 19/19 selected records qualified; 27/30 indexed architectures measured/qualified | [Completion receipt](../../results/pact_oss_benchmark/topology_recovery_20261004/completion.json), [public export](../../results/stage_a/README.md), [architecture index](../../results/stage_a/architecture_index.csv), [implemented metrics](../../results/stage_a/implemented_metrics.csv), [comparisons](../../results/stage_a/pairwise_comparison.csv) | [Exact baseline definitions](../benchmarks.md), [manifests](../../benchmarks/manifests/), [export checksums](../../results/stage_a/checksums.json) |
| Stage B: nine routed selections; mixed predictor transfer | [Final report](../../results/pact_stage_b/REPORT.md), [routed results](../../results/pact_stage_b/routed_results.csv), [candidate results](../../results/pact_stage_b/candidate_results.csv), [comparisons](../../results/pact_stage_b/comparison.csv) | [Frozen method](../stage_b_method.md), [portable inputs](../../results/pact_stage_b/inputs/), [selected orders](../../results/pact_stage_b/architectures/) |
| End-to-end test/physical qualification | [Report](../../results/pact_end_to_end_20261004/REPORT.md), [canonical dataset](../../results/pact_end_to_end_20261004/canonical_results.json), [final verification](../../results/pact_end_to_end_20261004/final_verification.json) | [Frozen baselines](../../results/pact_end_to_end_20261004/frozen_baselines.json), [fault/replay scope](../end_to_end_qualification.md) |
| Multiseed/placement studies | [Milestone scope and limitations](../history/research_milestones.md), [Stage-B report](../../results/pact_stage_b/REPORT.md) | [Retained original bindings](../../reports/repository_cleanup/retained_evidence_sha256.json); full prior campaigns require archive recovery |
| Cold-start, CPU and larger designs | [Cold-start report](../../results/pact_cold_start_unseen_20261004/cold_start_report.md), [CPU report](../../results/pact_cpu_scalability_20261005/cpu_scalability_report.md), [large-unseen results](../large_unseen_results.md) | [Cold-start contract](../pact_cold_start.md), [CPU contracts](../cpu_scalability.md), [atomic receipt policy](../experiment_receipts.md) |
| Gate 09: mixed competition; admission-limited generalization | [Full cohort report](../../results/pact_gate09_open_source_20261005/final/campaign/report.md), [b14](../../results/pact_gate09_open_source_20261005/final/b14_opt/report.md), [b15](../../results/pact_gate09_open_source_20261005/final/b15_opt/report.md), [b17 timeout diagnosis](../../results/pact_gate09_open_source_20261005/admission_diagnostics/b17_opt.json) | [Preregistration](../../results/pact_gate9_large_scale_unseen_20261005/benchmark_preregistration.json), [competitive definitions](../../results/pact_gate09_open_source_20261005/manifests/competitive_method_definitions.json) |
| Gate 10A: nine qualified architectures, no material static-PI benefit | [Final report](../../reports/gate10a/report.md), [comparison CSV](../../reports/gate10a/final_comparison.csv), [power](../../reports/gate10a/power_results.csv), [IR](../../reports/gate10a/ir_results.csv), [decision](../../reports/gate10a/decision.json) | [Preregistration](../../reports/gate10a/preregistration.md), [protocol](../../reports/gate10a/protocol.json), [selections](../../reports/gate10a/selected_architectures.json), [tools](../../reports/gate10a/tool_provenance.json), [reuse manifest](../../reports/gate10a/artifact_reuse_manifest.json), [machine summary](../../reports/gate10a/machine_summary.json) |

Gate 10A reuses frozen Gate 09 routed artifacts and measured activity; it is not a new search or routing campaign. [Negative findings](../experiments/negative_results.md) explain the joint worst/p99 materiality rule and the limits of causal interpretation.

The original Gate 09 cohort report ends with two host-absolute WSL links. Use the portable b14/b15 report links in the table above when reading outside that host. Those historical report bytes remain unchanged.

## Exact physical inputs and recovery

Physical reconstruction requires frozen placed/routed databases and SDC, workload/FF maps/orders, technology/Liberty/LEF/RC/PDN hashes and exact binary/submodule/patch identities. See [environment](environment.md) and [upstream provenance](../upstream.md). Pinned source alone does not recreate a frozen placement or prove an identical binary build.

The [archive manifest](../../archives/MANIFEST.csv) indexes raw campaigns. Verify compressed payload and extracted-member SHA256/lengths, then restore original relative layouts before adapters need them. Absolute archive paths are custodian-local recovery locations, not public download links. Some outputs existed only externally and require access from the experiment custodian; the public checkout alone cannot reproduce all physical measurements.

Originally tracked inputs can be recovered from pre-cleanup revision `f2569d498cd5f26a88c4954ec163498eb3cf7d91`, for example `git show REVISION:PATH > recovered-file`. Verify original byte hashes against the inventories. A newly generated placement or rerun is a new realization unless hashes match; relocation does not relabel an old realization.

## Portable receipt identities

Public metadata uses `repo://`, `dep://` and `run://` for repository, dependency and experiment roots. Resolve these using the checkout, `PACT_DEPENDENCY_ROOT` / individual overrides and `PACT_EXPERIMENT_ROOT`. `env://`, `archive://` and `maintenance://` describe historical environments/recovery and are not distributed inputs.

The [normalization ledger](../../reports/repository_cleanup/path_metadata_normalization.json) records original/public byte identities for earlier path/hostname-only exports. Embedded historical bindings refer to the original receipts; the ledger's `original_revision` recovers those bytes. The retained verifier checks both unchanged originals and audited public exports. This cleanup changes neither that ledger nor scientific values, hashes or normalization rules.

## Retention boundaries

Canonical tables, selected orders, protocols, manifests, failed attempts, tool/source snapshots and hashes stay at stable paths. Raw route/extraction/simulation data may be generated yet irreplaceable evidence; follow the [archive policy](../../archives/README.md) before discarding it. Prior maintenance audits are dated provenance, not current inventory or scientific status. No public Git history rewrite is part of this release.
