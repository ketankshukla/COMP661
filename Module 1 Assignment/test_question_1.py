# test_question_1.py
import pytest
from unittest.mock import patch
from datetime import datetime
from question_1 import main

# ==================== PASSING TEST CASES ====================

# Valid Input Test Cases - These should all pass
VALID_TEST_CASES = [
    pytest.param(
        {
            "name": "Basic Same-Day Trip",
            "inputs": ["2019-3-15", "11:00 AM", "500", "70", "n"],
            "expected_outputs": {
                "hours": 7,
                "minutes": 8,
                "arrival_date": "2019-03-15",
                "arrival_time": "06:08 PM"
            }
        },
        id="Basic Same-Day Trip"
    ),
    pytest.param(
        {
            "name": "Overnight Trip",
            "inputs": ["2020-3-15", "11:00 PM", "700", "55", "n"],
            "expected_outputs": {
                "hours": 12,
                "minutes": 43,
                "arrival_date": "2020-03-16",
                "arrival_time": "11:43 AM"
            }
        },
        id="Overnight Trip"
    ),
    pytest.param(
        {
            "name": "Exact Hour Trip",
            "inputs": ["2023-12-25", "11:00 AM", "60", "60", "n"],
            "expected_outputs": {
                "hours": 1,
                "minutes": 0,
                "arrival_date": "2023-12-25",
                "arrival_time": "12:00 PM"
            }
        },
        id="Exact Hour Trip"
    ),
    pytest.param(
        {
            "name": "Half Hour Trip",
            "inputs": ["2023-12-25", "11:00 AM", "30", "60", "n"],
            "expected_outputs": {
                "hours": 0,
                "minutes": 30,
                "arrival_date": "2023-12-25",
                "arrival_time": "11:30 AM"
            }
        },
        id="Half Hour Trip"
    ),
]

# Invalid Input Test Cases - These should pass by correctly handling errors
INVALID_TEST_CASES = [
    pytest.param(
        {
            "name": "Invalid Date Format",
            "inputs": ["2023/12/25", "2023-12-25", "11:00 AM", "500", "70", "n"],
            "should_contain": ["date", "format", "YYYY-MM-DD"],
            "retry_value": "2023-12-25"
        },
        id="Invalid Date Format"
    ),
    pytest.param(
        {
            "name": "Invalid Time Format",
            "inputs": ["2023-12-25", "25:00", "11:00 AM", "500", "70", "n"],
            "should_contain": ["time", "format", "HH:MM"],
            "retry_value": "11:00 AM"
        },
        id="Invalid Time Format"
    ),
    pytest.param(
        {
            "name": "Invalid Miles - Negative",
            "inputs": ["2023-12-25", "11:00 AM", "-500", "500", "70", "n"],
            "should_contain": ["positive", "number", "value"],
            "retry_value": "500"
        },
        id="Negative Miles"
    ),
    pytest.param(
        {
            "name": "Invalid Speed - Zero",
            "inputs": ["2023-12-25", "11:00 AM", "500", "0", "70", "n"],
            "should_contain": ["speed", "positive", "value"],
            "retry_value": "70"
        },
        id="Zero Speed"
    ),
    pytest.param(
        {
            "name": "Invalid Speed - Non-Numeric",
            "inputs": ["2023-12-25", "11:00 AM", "500", "abc", "70", "n"],
            "should_contain": ["number", "valid", "value"],
            "retry_value": "70"
        },
        id="Non-Numeric Speed"
    ),
]

# ==================== FAILING TEST CASES ====================

# These test cases are designed to fail to demonstrate error reporting
FAILING_TEST_CASES = [
    pytest.param(
        {
            "name": "Wrong Hour Calculation",
            "inputs": ["2019-3-15", "11:00 AM", "500", "70", "n"],
            "expected_outputs": {
                "hours": 6,  # Wrong! Should be 7
                "minutes": 8,
                "arrival_date": "2019-03-15",
                "arrival_time": "07:08 PM"  # Wrong! Should be 06:08 PM
            }
        },
        id="Wrong Hour Calculation"
    ),
    pytest.param(
        {
            "name": "Wrong Date for Overnight Trip",
            "inputs": ["2020-3-15", "11:00 PM", "700", "55", "n"],
            "expected_outputs": {
                "hours": 12,
                "minutes": 43,
                "arrival_date": "2020-03-15",  # Wrong! Should be 2020-03-16
                "arrival_time": "11:43 AM"
            }
        },
        id="Wrong Overnight Date"
    ),
    pytest.param(
        {
            "name": "Wrong Minutes Calculation",
            "inputs": ["2023-12-25", "11:00 AM", "30", "60", "n"],
            "expected_outputs": {
                "hours": 0,
                "minutes": 45,  # Wrong! Should be 30
                "arrival_date": "2023-12-25",
                "arrival_time": "11:45 AM"  # Wrong! Should be 11:30 AM
            }
        },
        id="Wrong Minutes Calculation"
    ),
]


class TestArrivalTimeCalculator:
    """Test suite for Arrival Time Calculator"""

    @patch('builtins.input')
    @pytest.mark.parametrize("test_case", VALID_TEST_CASES)
    def test_valid_inputs(self, mock_input, test_case, capsys):
        """Test cases with valid inputs - These should all pass"""
        print(f"\n{'=' * 80}")
        print(f"\033[1;33mTest Case: {test_case['name']}\033[0m")
        print(f"Inputs: {test_case['inputs']}")
        print(f"Expected: {test_case['expected_outputs']}")
        print(f"{'=' * 80}\n")

        # Setup mock input
        mock_input.side_effect = test_case['inputs']

        # Run the program
        main()
        output = capsys.readouterr().out

        # Print actual output
        print("\n\033[1;36mActual Program Output:\033[0m")
        print(output)

        # Check each expected output
        for key, value in test_case['expected_outputs'].items():
            assert str(value) in output, (
                f"\nMismatch found for {key}:"
                f"\nExpected: {value}"
                f"\nNot found in output:\n{output}"
            )

    @patch('builtins.input')
    @pytest.mark.parametrize("test_case", INVALID_TEST_CASES)
    def test_invalid_inputs(self, mock_input, test_case, capsys):
        """Test cases with invalid inputs - These should pass by correctly handling errors"""
        print(f"\n{'=' * 80}")
        print(f"\033[1;33mTest Case: {test_case['name']}\033[0m")
        print(f"Invalid Input: {test_case['inputs'][0]}")
        print(f"Should Contain Any: {test_case['should_contain']}")
        print(f"{'=' * 80}\n")

        # Setup mock input with retry values
        mock_input.side_effect = test_case['inputs']

        # Run the program
        main()
        output = capsys.readouterr().out.lower()

        # Print actual output
        print("\n\033[1;36mActual Program Output:\033[0m")
        print(output)

        # Check if error message contains any of the expected texts
        found = any(keyword.lower() in output for keyword in test_case['should_contain'])
        assert found, (
            f"\nError message should contain one of: {test_case['should_contain']}"
            f"\nActual output:\n{output}"
        )

    @patch('builtins.input')
    @pytest.mark.parametrize("test_case", FAILING_TEST_CASES)
    def test_failing_cases(self, mock_input, test_case, capsys):
        """These tests should fail because the expected outputs are deliberately wrong"""
        print(f"\n{'=' * 80}")
        print(f"\033[1;33mTest Case: {test_case['name']}\033[0m")
        print(f"Inputs: {test_case['inputs']}")
        print(f"Deliberately Wrong Expected Outputs: {test_case['expected_outputs']}")
        print(f"{'=' * 80}\n")

        # Setup mock input
        mock_input.side_effect = test_case['inputs']

        # Run the program
        main()
        output = capsys.readouterr().out

        # Print actual output
        print("\n\033[1;36mActual Program Output:\033[0m")
        print(output)

        # These assertions should fail because the expected outputs are wrong
        found_mismatch = False
        for key, value in test_case['expected_outputs'].items():
            if str(value) not in output:
                print(f"\n\033[1;31mMismatch found for {key}:\033[0m")
                print(f"Expected (Wrong): {value}")
                print(f"Actual output: {output}")
                found_mismatch = True

        # Assert that we found at least one mismatch
        assert found_mismatch, (
            f"\nTest was supposed to fail but passed!\n"
            f"This test case has deliberately wrong expected outputs.\n"
            f"Expected outputs: {test_case['expected_outputs']}\n"
            f"Actual output:\n{output}"
        )
