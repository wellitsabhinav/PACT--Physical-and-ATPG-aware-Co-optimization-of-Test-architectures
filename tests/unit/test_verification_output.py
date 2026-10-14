"""Local verification must be able to preserve the sealed receipt."""
import importlib.util
import json
from pathlib import Path


def test_end_to_end_verifier_can_write_outside_frozen_results(tmp_path):
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location('verify_end_to_end', root / 'scripts/verify_end_to_end.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    results = root / 'results/pact_end_to_end_20261004'
    sealed = results / 'final_verification.json'
    before = sealed.read_bytes()
    output = tmp_path / 'verification' / 'receipt.json'

    result = module.verify(results, verification_output=output)

    assert result['status'] == 'PASS'
    assert result['records_checked'] == 12
    assert json.loads(output.read_text(encoding='utf-8')) == result
    assert sealed.read_bytes() == before
