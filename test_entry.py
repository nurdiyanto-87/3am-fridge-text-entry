#!/usr/bin/env python3
"""Tests for main.py — pure standard library (unittest)."""

import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


class TestEntry(unittest.TestCase):
    def run_main(self, cwd):
        result = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py")],
            cwd=cwd, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        with open("/output/entry.txt", encoding="utf-8") as f:
            return f.read()

    def test_gate(self):
        """Gate: 1-140 chars, single line, non-blank, UTF-8."""
        with tempfile.TemporaryDirectory() as d:
            text = self.run_main(d)
        self.assertTrue(1 <= len(text) <= 140, len(text))
        self.assertNotIn("\n", text)
        self.assertEqual(text.strip(), text)
        self.assertTrue(text.strip())
        self.assertIn("3am", text)
        self.assertIn("haunted", text)
        self.assertIn("ghost", text)
        self.assertIn("hum", text)

    def test_deterministic(self):
        """Grader runs the program twice: output must be identical."""
        with tempfile.TemporaryDirectory() as d:
            first = self.run_main(d)
            second = self.run_main(d)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
