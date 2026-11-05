import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_record.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / 'examples/contribution-record.json').read_text())

    def published(self):
        result = copy.deepcopy(self.record)
        result['state'] = 'published'
        result['publication'] = {'url': 'https://github.com/a/b/pull/1', 'base_branch': 'dev',
                                 'head_sha': 'b' * 40, 'checked_sha': 'b' * 40,
                                 'action_authorization': 'explicit user request',
                                 'ci_status': 'approval_required'}
        return result

    def test_non_main_base_and_pending_approval(self):
        self.assertEqual([], validator.validate(self.published()))

    def test_duplicate_blocks_ready_and_published(self):
        for state in ('ready', 'published'):
            record = self.published()
            record.update(state=state, duplicate_status='unresolved')
            self.assertTrue(any('unresolved duplicate' in e for e in validator.validate(record)))

    def test_stale_sha_is_rejected(self):
        record = self.published()
        record['publication']['head_sha'] = 'c' * 40
        self.assertTrue(any('stale' in e for e in validator.validate(record)))

    def test_mismatched_base_is_rejected(self):
        record = self.published()
        record['publication']['base_branch'] = 'main'
        self.assertTrue(any('differs' in e for e in validator.validate(record)))

    def test_missing_authorization_and_invalid_ci(self):
        record = self.published()
        record['publication']['action_authorization'] = ''
        record['publication']['ci_status'] = 'green-ish'
        errors = validator.validate(record)
        self.assertTrue(any('action_authorization' in e for e in errors))
        self.assertTrue(any('ci_status' in e for e in errors))

    def test_invalid_json_cli(self):
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f:
            f.write('{')
            f.flush()
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_record.py'), f.name], capture_output=True)
        self.assertEqual(2, result.returncode)

    def test_example_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_record.py'), str(ROOT / 'examples/contribution-record.json')], capture_output=True)
        self.assertEqual(0, result.returncode)
        self.assertIn(b'claims were not verified', result.stdout)


if __name__ == '__main__':
    unittest.main()
