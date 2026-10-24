# PACT Gate 11 reproducibility package

Root: `F:\Research\PACT\Gate11\`.

## Reports and audit

- `08_reports/PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md`
- `08_reports/PACT_GATE11_RESULTS.csv` and `PACT_GATE11_RESULTS_METADATA.json`
- `08_reports/PACT_GATE11_CAUSAL_FINDINGS.md`
- `08_reports/PACT_GATE11_DAC_NOVELTY.md`
- `08_reports/PACT_GATE11_DECISION.md`
- `08_reports/PACT_GATE11_CAUSAL_SUMMARY.png` and `.pdf`
- `00_audit/PACT_GATE11_INPUT_AUDIT.md`, storage audits and `PACKAGE_SHA256SUMS.json`

## Source/input identities and dependencies

`00_audit/selected_inputs_manifest.json` binds original path, archive/member, size and SHA256. Additional recoveries: `additional_extraction_receipts.json`; container hashes: `extraction_receipts.json`; missing/alternate matching: `required_binding_recovery.json`. `archived_source_git_audit_G005.json` and the scientific report distinguish source snapshot/Gate09/Gate10/tool commits. Historical scientific receipts remain byte-identical under `01_inputs/S008/PACT/reports/gate10a/`.

Current runtime: existing `D:\Python\python.exe` 3.12.5, NumPy2.1.3 and Matplotlib3.9.2. Exact executable hashes/package metadata: `00_audit/current_tool_audit.json`. Existing zstd1.5.5 streamed archives. No environment/dependency installation. Qualified EDA identities/Liberty hash are in the scientific report and recovered tool provenance. WSL EDA is blocked; native Icarus availability does not prove qualified experiment reproduction.

## Executed commands/environment

All scientific analysis uses this environment wrapper and prospective manifest:

```powershell
& 'F:\Research\PACT\Gate11\09_scripts\environment.ps1' `
  -Script 'F:\Research\PACT\Gate11\09_scripts\run_manifest.py' `
  -ScriptArgs @('UNIQUE_RUN_NAME','D:\Python\python.exe','-B','F:\Research\PACT\Gate11\09_scripts\SCRIPT.py')
```

`10_logs/*.manifest.json` records exact argv, cwd, source hashes, environment, UTC start/completion, wall/CPU time, peak working set and disk increment. stdout/stderr is beside each manifest. Original failed attempts/sources and WSL failure logs remain. `historical_Gate10A_all_attempts.csv` is the entire17-attempt historical table, not new execution. Discovery/inventory/initial recovery have retrospective command/source/receipt records without fabricated prospective timestamps.

Ordered stages: `inventory.py`, `recover_inputs.py`, `freeze_and_bindings.py`, `recover_extra.py`; original end-to-end verifier; `analyze_frozen_outputs.py`; sole registered `followup_01_factor_accounting.py`; `derive_diagnostics.py`; `enrich_predicted_transfer.py`; `tool_audit.py`; `write_reports.py`; final package validation. First two parser sources/logs are preserved. Original numerical optimizer verifier fails on Numba; no replacement is called equivalent.

## Safe rerun

Run `09_scripts/reproduce_analysis.py` through `environment.ps1` with the existing Python. It creates a fresh timestamped child under `02_reproduction/`, reuses staged inputs read-only, copies analysis scripts/protocol only, redirects every controllable cache/temp path into the child, records original/transformed source hashes and runs the frozen accounting pipeline. It refuses overlays and compares scientific numeric columns to the delivered table. Root/input path substitutions are explicit in its manifest; original executed sources remain preserved. It does not install, search, ATPG, route, extract or simulate. This is a delivered future rerun helper, not an additional optional experiment already executed.

Complete physical reproduction is blocked by80 missing raw/tool bindings and the missing qualified runtime. First restore the exact b14 B3T/C1 pair as described in the decision. Timing-aware modeling is a new registered extension, not a substitute for zero-delay history.

## Machine artifact locations

- `02_reproduction/frozen_comparisons.json`: frozen population/fairness.
- `03_activity/`: classified nets, source-class activity, predictor/implemented transfer.
- `04_power/native_power_components.csv`: Sequential/Combinational/Clock internal/switching/leakage.
- `05_parasitics/README.md`: availability boundary; C exports also in `03_activity/per_net_classified.csv` and frozen input CSVs.
- `06_causality/`: seven factor comparisons, complete spatial/concentration/source budgets, base/enriched/diagnostic JSON.
- `07_hypothesis/followup_01_preregistration.md`: single optional experiment's falsifiable protocol.
- `10_logs/`: all launched command/resource manifests, failures and verifier outputs.

## Storage compliance

All intentionally generated experiments/reports/scripts/logs/caches/temp data are on F: inside Gate11. Originals were read-only; unrelated files were not deleted/moved. Exact logical/allocated file bytes and scope: `00_audit/storage_audit_final.json`. Codex/OS service logs, paging and host bookkeeping cannot be forced entirely onto F:, so no absolute system-wide claim is made. WSL failed before Linux on missing preconfigured F: disk/swap paths. No working Linux /tmp/home experimental writes occurred.
