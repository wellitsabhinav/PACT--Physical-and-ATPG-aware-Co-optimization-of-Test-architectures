# PACT Agent Instructions

## Project status

PACT is frozen research under its original tested hypothesis. The final classification is `PACT_GATE10A_NO_MATERIAL_PHYSICAL_IMPACT`; the recommendation is `FREEZE`. Maintenance does not authorize new searches, ATPG, routes, tuning or expensive scientific campaigns.

## Scientific integrity

- Preserve canonical result bytes, selections, registered thresholds, hashes, provenance, classifications and negative outcomes.
- Never invent metrics, promote candidates after seeing measurements or reinterpret failed gates.
- Keep proxy predictions, implemented activity, qualification and practical physical impact distinct.
- b17's ATPG admission timeout is not an optimizer loss; b18 was policy-deferred.
- Thermal impact was not evaluated. Transient droop and industrial/signoff generalization were not established.
- Document apparent evidence inconsistencies separately; do not silently repair or reseal them as formatting cleanup.

## Source-of-truth hierarchy

1. `README.md`: current public summary and final outcome.
2. `docs/methodology/`: model/objective/schedule and qualification definitions.
3. `docs/reproduction/canonical_results.md`: exact protocols, tables, selections and verification boundaries.
4. `reports/gate10a/`: registered final impact protocol, report and decision.
5. `results/`, other `reports/`, `benchmarks/`, `config/`, `experiments/`: retained evidence at original paths.
6. `docs/history/`, `cleanup/`, `archives/`: historical context, maintenance snapshots and recovery. Historical next actions do not override the freeze.

## Repository hygiene

- Keep source, compact fixtures, selected orders, final tables, manifests, failed-run receipts and qualified patches.
- Use ignored `scratch/` or configured experiment storage for caches, builds, logs and bulk output.
- Search references and hash bindings before removing/moving files. Duplicate bytes can be independent receipt-bound evidence.
- Follow `archives/README.md`; retain uncertain source trees and raw evidence until verified recovery exists.
- Do not rewrite public Git history as routine cleanup.

## Development workflow

- Use a dedicated branch and PR; do not modify `main` directly.
- Install `python -m pip install -e '.[optimizer,dev]'`.
- Run the inexpensive suite on Linux/WSL: `PYTHONPATH=src:scripts:. python -m pytest -q`.
- Run `python scripts/verify_reproducibility.py` and `python scripts/verify_end_to_end.py --verification-output scratch/end_to_end_verification.json` for public-release maintenance or retained-evidence work.
- Validate documentation links, structured files and `git diff --check`; report unavailable dependencies and skips accurately.
- Before committing, compare evidence paths/hashes against the starting revision. Do not launch EDA campaigns for documentation work.

## Experiment and documentation policy

Bug, portability, test and documentation fixes are welcome. New objectives, power models, transient/thermal studies or renewed optimization require a separate hypothesis, registration and output namespace or fork. Never overwrite frozen evidence.

Explain achievements, limits and exact evidence locations. Avoid speculative causal language: saved counterfactual substitutions are nonlinear/order-dependent and do not uniquely apportion causality. Activity proxies do not measure watts or voltage drop.

## External tools and instruction scope

Preserve exact OpenROAD/ORFS/OpenSTA/FAN_ATPG revisions, submodules, patches, build identities and original failures. Local qualification does not imply upstream acceptance; current binaries do not reproduce frozen tool identity.

This is the only active PACT-owned agent policy. Files inside ignored `external/` dependencies or preserved upstream snapshots describe those upstream trees; they are provenance, not additional PACT policy. Do not alter them merely to reduce the filename count.
