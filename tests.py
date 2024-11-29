import unittest
from patterns import highlight_info
from hilite import main
from io import StringIO
import sys

class TestHighlightInfo(unittest.TestCase):
    def test_highlights_core_patterns(self):
        data = "Found an IP 192.168.1.1, email admin@example.com, and file /etc/passwd."
        result = highlight_info(data)

        # Check IP Address
        self.assertIn("192.168.1.1", result.get("IP Address", []))

        # Check Email Address
        self.assertIn("admin@example.com", result.get("Email Address", []))

        # Check File Path
        file_paths = result.get("File Path", [])
        self.assertTrue(any("/etc/passwd" in path for path in file_paths))

    def test_no_highlights(self):
        data = "This string has no patterns."
        result = highlight_info(data)
        self.assertEqual(result, {})  # Expect no matches

class TestHiliteScript(unittest.TestCase):
    def test_main_script_execution(self):
        # Simulate piped input for the main script
        input_data = "Found an IP 192.168.1.1 and email admin@example.com."
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()

        # Execute the main script
        main()

        # Capture script output
        output = sys.stdout.getvalue()

        # Ensure the critical information is highlighted
        self.assertIn("192.168.1.1", output)
        self.assertIn("admin@example.com", output)

if __name__ == "__main__":
    unittest.main()
