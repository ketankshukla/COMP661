# test_question_1.py
import pytest
from unittest.mock import patch
from question_1 import main
import sys

class TestArrivalTimeCalculator:
    """Tests for Arrival Time Calculator"""

    def print_info(self, capsys, test_name, inputs, expected):
        """Print info and clear output buffer"""
        print(
            f"\n{'=' * 50}\n"
            f"Test: {test_name}\n"
            f"Inputs: {inputs}\n"
            f"Expected: {expected}\n"
            f"{'=' * 50}"
        )
        capsys.readouterr()  # Clear the buffer

    def run_test(self, mock_input, capsys, test_name, inputs, expected):
        """Utility function to run a test case"""
        self.print_info(capsys, test_name, inputs, expected)

        # Set up the input mock
        mock_input.side_effect = inputs

        # Run the main function and capture output
        main()
        output = capsys.readouterr().out

        # Verify each expected value
        all_passed = True
        for key, value in expected.items():
            if value not in output:
                all_passed = False
                print(
                    f"\n❌ FAILED: {test_name} failed\n"
                    f"Inputs: {inputs}\n"
                    f"Expected: {value}\n"
                    f"Output: {output}\n"
                    f"Actual value observed: '{output}'"
                )
                # Exit with failure status without verbose traceback
                sys.exit(1)

        if all_passed:
            print(f"\n✅ PASSED: {test_name} passed successfully!\n"
                  f"Inputs: {inputs}\n"
                  f"Expected: {expected}\n"
                  f"Output: {output}\n")

    @patch('builtins.input')
    def test_basic_trip(self, mock_input, capsys):
        """Basic trip: 500 miles at 70mph starting at 11:00 AM"""
        inputs = ["2019-3-15", "11:00 AM", "500", "70", "n"]
        expected = {
            "hours": "Hours: 7",
            "minutes": "Minutes: 8",
            "arrival_time": "06:08 PM"
        }
        self.run_test(mock_input, capsys, "Basic Trip", inputs, expected)

    @patch('builtins.input')
    def test_overnight_trip(self, mock_input, capsys):
        """Overnight trip: 700 miles at 55mph starting at 11:00 PM"""
        inputs = ["2020-3-15", "11:00 PM", "700", "55", "n"]
        expected = {
            "hours": "Hours: 12",
            "minutes": "Minutes: 43",
            "arrival_date": "2020-03-16",
            "arrival_time": "11:43 AM"
        }
        self.run_test(mock_input, capsys, "Overnight Trip", inputs, expected)

    @patch('builtins.input')
    def test_invalid_miles(self, mock_input, capsys):
        """Test handling of negative miles input"""
        inputs = ["2023-12-25", "11:00 AM", "-500", "500", "70", "n"]
        expected_messages = ["positive", "valid", "number", "at least"]

        self.print_info(capsys, "Invalid Miles", inputs, expected_messages)

        # Run the main function and capture output
        mock_input.side_effect = inputs
        main()
        output = capsys.readouterr().out.lower()

        # Verify at least one expected message is in the output
        matching_message = next((msg for msg in expected_messages if msg in output), None)
        if matching_message:
            print(f"\n✅ PASSED: Invalid Miles test passed successfully!\n"
                  f"Inputs: {inputs}\n"
                  f"Expected: One of {expected_messages}\n"
                  f"Output: {output}\n"
                  f"Matched expected: '{matching_message}'\n")
        else:
            print(f"\n❌ FAILED: Invalid Miles test failed\n"
                  f"Inputs: {inputs}\n"
                  f"Expected one of: {expected_messages}\n"
                  f"Output: {output}\n"
                  f"Actual value observed: '{output}'")
            # Exit with failure status without verbose traceback
            sys.exit(1)

    @patch('builtins.input')
    def test_deliberate_fail(self, mock_input, capsys):
        """This test should fail to demonstrate error reporting"""
        inputs = ["2019-3-15", "11:00 AM", "500", "70", "n"]
        expected = {
            "hours": "Hours: 7",  # Wrong! Should be 7
            "arrival_time": "06:08 PM"  # Wrong! Should be 06:08 PM
        }
        self.print_info(capsys, "Deliberate Failure", inputs, expected)

        # Set up the input mock
        mock_input.side_effect = inputs

        # Run the main function and capture output
        main()
        output = capsys.readouterr().out

        # Verify each expected value
        for key, value in expected.items():
            if value not in output:
                print(
                    f"\n❌ FAILED: Deliberate Failure failed\n"
                    f"Inputs: {inputs}\n"
                    f"Expected: {value}\n"
                    f"Output: {output}\n"
                    f"Actual value observed: '{output}'"
                )
                # Exit with failure status without verbose traceback
                sys.exit(1)
