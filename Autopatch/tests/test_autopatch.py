import unittest
from vulnerability_scanner import scan_code
from patch_generator import generate_patch

class TestAutoPatch(unittest.TestCase):
    def test_scan_code(self):
        vulnerabilities = scan_code("test_files/test_vulnerable_code.py")
        self.assertTrue(len(vulnerabilities) > 0)

    def test_generate_patch(self):
        vulnerabilities = [{"line": 2, "type": "SQL Injection"}]
        patched_code = generate_patch("test_files/test_vulnerable_code.py", vulnerabilities)
        self.assertIn("escape(", patched_code)

if __name__ == "__main__":
    unittest.main()
