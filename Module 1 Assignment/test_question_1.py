# test_question_1.py
import pytest
from unittest.mock import patch
from datetime import datetime
from question_1 import main


class TestArrivalTimeCalculator:
    """Tests for Arrival Time Calculator"""

    def print_info(self, capsys, message):
        """Print info and clear output buffer"""
        print(message)
        capsys.readouterr()  # Clear the buffer

    @patch('builtins.input')
    def test_basic_trip(self, mock_input, capsys):
        """Basic trip: 500 miles at 70mph starting at 11:00 AM"""
        # Test setup
        inputs = ["2019-3-15", "11:00 AM", "500", "70", "n"]
        expected = {
            "hours": "Hours: 7",  # This should fail - wrong hours - was 711
            "minutes": "Minutes: 8",
            "arrival_time": "06:08 PM"
        }

        self.print_info(capsys,
                        f"\n{'=' * 50}\n"
                        f"Test: Basic Trip\n"
                        f"Inputs: {inputs}\n"
                        f"Expected: {expected}\n"
                        f"{'=' * 50}"
                        )

        # Run test
        mock_input.side_effect = inputs
        main()
        output = capsys.readouterr().out

        # Verify each expected value
        for key, value in expected.items():
            assert value in output, (
                f"\nFAILED: {key} check failed\n"
                f"Expected: {value}\n"
                f"Output: {output}"
            )

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

        self.print_info(capsys,
                        f"\n{'=' * 50}\n"
                        f"Test: Overnight Trip\n"
                        f"Inputs: {inputs}\n"
                        f"Expected: {expected}\n"
                        f"{'=' * 50}"
                        )

        mock_input.side_effect = inputs
        main()
        output = capsys.readouterr().out

        for key, value in expected.items():
            assert value in output, (
                f"\nFAILED: {key} check failed\n"
                f"Expected: {value}\n"
                f"Output: {output}"
            )

    @patch('builtins.input')
    def test_invalid_miles(self, mock_input, capsys):
        """Test handling of negative miles input"""
        inputs = ["2023-12-25", "11:00 AM", "-500", "500", "70", "n"]
        expected_messages = ["positive", "valid", "number", "at least"]

        self.print_info(capsys,
                        f"\n{'=' * 50}\n"
                        f"Test: Invalid Miles\n"
                        f"Inputs: {inputs}\n"
                        f"Expected messages: {expected_messages}\n"
                        f"{'=' * 50}"
                        )

        mock_input.side_effect = inputs
        main()
        output = capsys.readouterr().out.lower()

        assert any(msg in output for msg in expected_messages), (
            f"\nFAILED: Error message check failed\n"
            f"Expected one of: {expected_messages}\n"
            f"Output: {output}"
        )

    @patch('builtins.input')
    def test_deliberate_fail(self, mock_input, capsys):
        """This test should fail to demonstrate error reporting"""
        inputs = ["2019-3-15", "11:00 AM", "500", "70", "n"]
        expected = {
            "hours": "Hours: 6",  # Wrong! Should be 7
            "arrival_time": "06:08 PM"  # Wrong! Should be 06:08 PM
        }

        self.print_info(capsys,
                        f"\n{'=' * 50}\n"
                        f"Test: Deliberate Failure\n"
                        f"Inputs: {inputs}\n"
                        f"Expected (Wrong): {expected}\n"
                        f"{'=' * 50}"
                        )

        mock_input.side_effect = inputs
        main()
        output = capsys.readouterr().out

        # This should fail since we're expecting wrong values
        for key, value in expected.items():
            assert value in output, (
                f"\nFAILED (as expected): {key} check failed\n"
                f"Expected (Wrong): {value}\n"
                f"Actual (Correct): {output}"
            )
