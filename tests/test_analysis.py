"""Meaningful validation and output round-trip tests."""
import copy
import csv
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("analysis", ROOT / "src/analyze_licenses.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))

    def test_outputs_preserve_vietnamese_and_all_three_projects(self):
        with tempfile.TemporaryDirectory() as folder:
            summary = module.generate(self.rows, folder)
            with open(Path(folder) / "comparison.csv", encoding="utf-8-sig", newline="") as f:
                data = list(csv.reader(f))
            self.assertEqual(len(data), 4)
            self.assertEqual({r[0] for r in data[1:]}, {"GNU Bash", "React", "Apache Spark"})
            self.assertEqual(data[0][0], "Dự án")
            self.assertEqual(summary["commercial_use_allowed_count"], 3)
            self.assertEqual(json.loads((Path(folder) / "summary.json").read_text()), summary)

    def test_duplicate_project_rejected(self):
        self.rows[2] = copy.deepcopy(self.rows[0])
        with self.assertRaises(ValueError):
            module.validate(self.rows)

    def test_untraceable_claim_rejected(self):
        self.rows[0]["sources"] = []
        with self.assertRaises(ValueError):
            module.validate(self.rows)

    def test_license_mismatch_rejected(self):
        self.rows[0]["license"] = "MIT"
        with self.assertRaises(ValueError):
            module.validate(self.rows)

if __name__ == "__main__":
    unittest.main()
