# Contributing to PACT

PACT is a **frozen research artifact** under the original tested hypothesis. Its final registered classification is `PACT_GATE10A_NO_MATERIAL_PHYSICAL_IMPACT`, recommendation `FREEZE`. See the [current summary](README.md) and [final decision](reports/gate10a/decision.json).

## Welcome maintenance

- Bug fixes and reproducibility repairs.
- Documentation, portability and test improvements.
- Independent extensions with clearly identified assumptions and outputs.

Preserve frozen results, original failures, registration settings, architecture identities and hashes. Report inconsistencies separately instead of silently changing an old result or resealing its receipt. Predictor gains, routed measurements and practical benefit must remain distinct.

## Separate research hypotheses

New objectives or power models, renewed optimization, transient IR, thermal studies and changes to scientific conclusions require a separate hypothesis and preregistration in an isolated experiment namespace or fork. State the frozen PACT baseline revision. Do not overwrite historical evidence or tune registered thresholds after viewing outcomes.

## Validation and review

Use a focused branch and PR. Describe the concrete problem, resulting behavior, validation and limitations. Install `.[optimizer,dev]` and run the complete inexpensive harness on Linux/WSL:

```sh
PYTHONPATH=src:scripts:. python -m pytest -q
python scripts/verify_reproducibility.py
python scripts/verify_end_to_end.py --verification-output scratch/end_to_end_verification.json
git diff --check
```

Model changes need independent exact-reference, rollback, topology/identity and replay checks. Documentation changes need link checks and verification against the [canonical evidence index](docs/reproduction/canonical_results.md). Report skips and unavailable tools; a numerical test pass is not physical qualification. See [environment](docs/reproduction/environment.md) and [development contracts](docs/development.md).

## Retention and upstream tools

Keep source, schemas/configuration, essential fixtures, selected orders, compact tables, provenance and negative conclusions in Git. Put environments, caches, builds and bulk runtime output under ignored scratch/archive roots. Search references and hash bindings before deleting duplicates; follow the [archive policy](archives/README.md). Public history rewrites require a separate deliberate operation.

Preserve exact tool revisions and qualified patches. Follow upstream licenses and contribution rules; local qualification does not establish upstream acceptance. A new result must not require mutating frozen evidence.
