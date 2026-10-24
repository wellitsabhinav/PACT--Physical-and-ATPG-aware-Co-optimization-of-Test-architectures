# PACT Gate 11 input audit

## Discovery and read-only boundary

The current C: workspace is no longer a Git checkout and contains only forensic-quarantine directories. Original projects/results were inspected read-only. Canonical evidence was found in `F:\Research_Archives\PACT\`, selected through `F:\Research_Archives\AUDIT_REPORTS\archive_manifest.csv`. The archived active worktree was `C:\Users\Abhinav\OneDrive\Desktop\PACT\PACT`.

No original repository, archive, WSL registration, historical output, junction or symlink was modified. No environment/worktree was created outside F:. The user authorizes this separate Gate11 study; the original project's freeze remains intact.

## Recovered evidence

| Evidence | Path below `01_inputs/S008/PACT/` | Integrity/scope |
| --- | --- | --- |
| Stage A | `results/stage_a/`, `results/pact_oss_benchmark/topology_recovery_20261004/` | 19/19 selected and 27/30 indexed qualified; checksums/projections verified. |
| Gate09 | `results/pact_gate09_open_source_20261005/final/`, `repair_attempts/` | 18 b14/b15 rows, B0/B1/B2/B3T/B4/B5, C1/C2/C3, seed 11, fairness/hashes, selections and failures. |
| Gate10A | `reports/gate10a/` | Nine selected records, 17 attempted/control runs, net activity and per-instance power, spatial vectors, protocol/decision/tool provenance. |
| Implementations/evaluator | `src/pact/optimizer/`, `src/pact/activity/`, `scripts/pact_cpu_activity.py` | Depth3/stateful and exact compact Icarus sources; qualified crosscheck receipts. |
| End-to-end | `results/pact_end_to_end_20261004/` | Original verifier passes 12 records/fault-identity comparisons. |
| H8 diagnosis | `results/pact_h8_rootcause/` | Historical omitted-region/capacitance findings and nonlinear attribution limits. |
| Liberty/RC | `external/OpenROAD-flow-scripts/flow/platforms/nangate45/` | Exact hash-matched Liberty, setRC and grid strategy recovered; no tool build. |
| s5378 | Stage A/B tables | Total-route non-improvement corroborated; exact earlier phase1 HPWL raw pair not recovered. |

4,578 initial regular files plus seven additional required files were selectively extracted and individually checked against archived member hashes. No links were created. Both source containers matched the archived checksum ledger. `selected_inputs_manifest.json`, `extraction_receipts.json`, and `additional_extraction_receipts.json` identify each member. Environments, tool builds, .git objects and large caches were not wholesale restored.

`retained_hash_verification.json` passes 674 retained bindings, audited original/public normalization rules, Stage-A table projections and selected Gate10A outputs. This successful hash-only audit is separate from blocked numerical optimizer replay.

## Missing evidence and reproduction blockers

Selected raw count traces, routed Verilog/ODB/SPEF, logical/physical maps, qualified b14/b15 patterns, large stimuli and placement inputs are hash-addressed historically but absent from the recoverable PACT regular-file inventory. Alternate identical-file hashes were checked. Of 245 unique selected/input/tool/output bindings, 165 had recoverable matches and 80 did not. All recoverable required matches are now staged; a recorded binary hash does not recover the binary.

The prior `E:\PACT_ARCHIVES\20261008\gate_results\pact_gate09_open_source_20261005.tar.zst` path is absent. Its indexed expected SHA-256 is `2ed5ab00d1e4b9190d58ecd3c22fc03add0b2ea2f9bce8a8be662c06febe7a9f`. No substitute private package or download URL was invented.

Ubuntu-24.04 is registered but fails on missing `F:\green-ecc-iscas-sustainability-temp\wsl-relocated\Ubuntu-24.04\ext4.vhdx`; configured F: swap path is also missing. Linux did not start. No repair/reinstall/config change occurred. Native Icarus is present but cannot reconstruct the qualified workload without exact inputs/cell models and matching runtime/VPI evidence.

Original `verify_reproducibility.py` fails immediately because Numba is absent. Archived .optimizer-deps Numba/llvmlite are Linux binaries and were not used as a fake Windows replacement. The 18 numerical Stage-B State/reference replays are not newly verified. The separate end-to-end verifier passes.

No new VCD/SAIF, occupancy, timing-aware glitches, extracted route, ideal/routed comparison, transient IR, thermal, EM or signoff result exists. Prior complete-count validation is recovered record evidence plus export integrity, not a new read of missing raw traces. Frozen path-normalized exports were checked, not resealed.

## Provenance

- Recovered source snapshot: archived main worktree HEAD `e84f4afbf04a918060b4ad845f5166d8e6c7b92c`, from preserved Git audit G005. Selective regular-file restoration, not a full Git clone; original member hashes identify the actual bytes.
- Gate09 PACT SHA `71b059d9d1a00735d79b6a428693eaba549a5f33`; b14 comparison implementation SHA `e43da79d76d363fe67ae120d5e53a3c2d04a9a2f44549601d8df2daabc05cf3e`. Row-specific provenance is retained separately.
- Gate10A parent `53ebab37fd76970d7c5e676b0caec13c7c16296e`; preregistration `b9869834a3479a57f256c83fa74a4617faab4af2`.
- Common OpenROAD `08f67ee5ecd14db5a42be8c610bbfd1ccf079299`, version `26Q2-1164-g08f67ee5ec`, binary SHA-256 `fcd7dcfc37d329bd43a7ede75805319a2e70e6879da11d42b4fd1c2e50e645c3`.
- ORFS `5e8b1450d19263f797a27c4f371b9dd19f32a3aa`; declared embedded OpenSTA `76c4d6df3537ccce331b5caa812196c3330ba7c4`. Supporting OpenROAD source `dc5eee77c45dba8e5ace2fc89c38c6d9a4ed6e0f` differs from the binary. Standalone STA 3.1.0 was not the power engine.
- FAN_ATPG base `26b2b36c0e9db11a4b6d9e759df6e44357121f39`; qualified repair `4c253bfa613e5827f17c42a5fce8be7bea779e1e`.
- I99T sources `8a2c3b500ee7ff20e7031de92592b737bedc6d8c`.
- Nangate45 typical Liberty SHA-256 `8d540a4d4cf6d09d27c87ad067857a9c0c2eeb023ab7a56e058cd3113db4e9b1`; exact library/RC bytes recovered and verified.


## Storage/resources

Fresh root: `F:\Research\PACT\Gate11\`. All required numbered directories and scratch/cache/tmp exist. Initial free F: bytes: 168,161,681,408. Controlled TEMP/TMP/TMPDIR, pip/XDG/Python/Matplotlib/Numba caches, HOME, working/output directories resolve inside Gate11. No install/build/GPU/full physical flow ran. Analysis was serial; two inexpensive retention checks briefly overlapped.

Machine audit: `storage_audit_initial.json`, `storage_audit_final.json`, `current_tool_audit.json`, `10_logs/*.manifest.json`. Initial discovery is recorded retrospectively without invented timestamps. Initial inventory/recovery has source/log/member receipts rather than a fabricated prospective manifest; every launched scientific analysis has a prospective command/resource manifest.

Controllable experimental storage complies with F-only. Codex transcripts/tool transport, OS/WSL service bookkeeping, pagefile/antivirus/system logs cannot be certified as system-wide F-only. WSL tried its preconfigured missing F: swap/disk paths outside Gate11 and failed before Linux. No deliberate experimental output was written there or to C:/D:/E:.
