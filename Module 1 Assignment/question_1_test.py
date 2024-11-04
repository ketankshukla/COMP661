import unittest
from unittest.mock import patch
from datetime import datetime
from question_1 import (
    validate_date, validate_time, calculate_travel_time,
    calculate_arrival_datetime, format_results, main
)


class TestArrivalTimeCalculator(unittest.TestCase):
    def setUp(self):
        """This runs before each test"""
        print("\n" + "=" * 50)

    def test_validate_date(self):
        """Test date validation with various inputs"""
        print("\nTest: Date Validation")

        # Valid dates
        self.assertTrue(validate_date("2023-12-25")[0], "Should accept valid date YYYY-MM-DD")
        self.assertTrue(validate_date("2023-1-5")[0], "Should accept valid date with single digit month/day")

        # Invalid dates
        self.assertFalse(validate_date("2023/12/25")[0], "Should reject incorrect format")
        self.assertFalse(validate_date("2023-13-01")[0], "Should reject invalid month")
        self.assertFalse(validate_date("2023-02-30")[0], "Should reject invalid day")
        self.assertFalse(validate_date("1800-01-01")[0], "Should reject year before 1900")
        self.assertFalse(validate_date("2200-01-01")[0], "Should reject year after 2100")
        self.assertFalse(validate_date("abc")[0], "Should reject non-numeric input")
        self.assertFalse(validate_date("")[0], "Should reject empty string")

    def test_validate_time(self):
        """Test time validation with various inputs"""
        print("\nTest: Time Validation")

        # Valid times
        self.assertTrue(validate_time("11:00 AM")[0], "Should accept valid time HH:MM AM")
        self.assertTrue(validate_time("1:30 PM")[0], "Should accept valid time H:MM PM")

        # Invalid times
        self.assertFalse(validate_time("13:00 PM")[0], "Should reject hours > 12")
        self.assertFalse(validate_time("11:60 AM")[0], "Should reject minutes > 59")
        self.assertFalse(validate_time("11:00")[0], "Should reject missing AM/PM")
        self.assertFalse(validate_time("11:00 XM")[0], "Should reject invalid meridiem")
        self.assertFalse(validate_time("abc")[0], "Should reject non-numeric input")
        self.assertFalse(validate_time("")[0], "Should reject empty string")

    def test_calculate_travel_time(self):
        """Test travel time calculations"""
        print("\nTest: Travel Time Calculations")

        # Test case 1: Console example (500 miles at 70 mph)
        hours, minutes = calculate_travel_time(500, 70)
        self.assertEqual((hours, minutes), (7, 8),
                         "First console example (500mi @ 70mph) should be 7h 8m")

        # Test case 2: Console example (700 miles at 55 mph)
        hours, minutes = calculate_travel_time(700, 55)
        self.assertEqual((hours, minutes), (12, 43),
                         "Second console example (700mi @ 55mph) should be 12h 43m")

        # Test exact hour
        hours, minutes = calculate_travel_time(60, 60)
        self.assertEqual((hours, minutes), (1, 0),
                         "60 miles @ 60mph should be exactly 1 hour")

        # Test less than hour
        hours, minutes = calculate_travel_time(30, 60)
        self.assertEqual((hours, minutes), (0, 30),
                         "30 miles @ 60mph should be exactly 30 minutes")

    def test_calculate_arrival_datetime(self):
        """Test arrival datetime calculations"""
        print("\nTest: Arrival DateTime Calculations")

        # Same day arrival
        arrival = calculate_arrival_datetime("2019-3-15", "11:00 AM", 7, 8)
        self.assertEqual(arrival.strftime('%Y-%m-%d %I:%M %p'),
                         "2019-03-15 06:08 PM", "Same day arrival should calculate correctly")

        # Next day arrival
        arrival = calculate_arrival_datetime("2020-3-15", "11:00 PM", 12, 43)
        self.assertEqual(arrival.strftime('%Y-%m-%d %I:%M %p'),
                         "2020-03-16 11:43 AM", "Next day arrival should calculate correctly")

    def test_format_results(self):
        """Test results formatting"""
        print("\nTest: Results Formatting")

        arrival_datetime = datetime(2019, 3, 15, 18, 8)  # 6:08 PM
        results = format_results(7, 8, arrival_datetime)

        self.assertEqual(results['hours'], 7, "Hours should be formatted correctly")
        self.assertEqual(results['minutes'], 8, "Minutes should be formatted correctly")
        self.assertEqual(results['arrival_date'], '2019-03-15', "Date should be formatted correctly")
        self.assertEqual(results['arrival_time'], '06:08 PM', "Time should be formatted correctly")

    @patch('builtins.input', side_effect=["2019-3-15", "11:00 AM", "500", "70", "n"])
    def test_main_first_example(self, mock_input):
        """Test main function with first console example"""
        print("\nTest: Main Function - First Example")

        with patch('builtins.print') as mock_print:
            main()
            printed_items = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]

            expected_outputs = ["Hours: 7", "Minutes: 8", "2019-03-15", "06:08 PM"]
            for expected in expected_outputs:
                self.assertTrue(
                    any(expected in item for item in printed_items),
                    f"Output should contain '{expected}'"
                )

    @patch('builtins.input', side_effect=["2020-3-15", "11:00 PM", "700", "55", "n"])
    def test_main_second_example(self, mock_input):
        """Test main function with second console example"""
        print("\nTest: Main Function - Second Example")

        with patch('builtins.print') as mock_print:
            main()
            printed_items = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]

            expected_outputs = ["Hours: 12", "Minutes: 43", "2020-03-16", "11:43 AM"]
            for expected in expected_outputs:
                self.assertTrue(
                    any(expected in item for item in printed_items),
                    f"Output should contain '{expected}'"
                )

    @patch('builtins.input', side_effect=[
        "2019-3-15", "11:00 AM", "500", "70", "y",
        "2020-3-15", "11:00 PM", "700", "55", "n"
    ])
    def test_main_multiple_calculations(self, mock_input):
        """Test main function with multiple calculations"""
        print("\nTest: Main Function - Multiple Calculations")

        with patch('builtins.print') as mock_print:
            main()
            printed_items = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]

            expected_outputs = ["06:08 PM", "11:43 AM"]
            for expected in expected_outputs:
                self.assertTrue(
                    any(expected in item for item in printed_items),
                    f"Output should contain '{expected}'"
                )

    @patch('builtins.input', side_effect=[
        "invalid-date", "2019-3-15", "11:00 AM", "500", "70", "n"
    ])
    def test_main_invalid_date(self, mock_input):
        """Test main function with invalid date input"""
        print("\nTest: Main Function - Invalid Date Handling")

        with patch('builtins.print') as mock_print:
            main()
            printed_items = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]
            self.assertTrue(
                any("date" in item.lower() for item in printed_items),
                "Should show error message for invalid date"
            )

    @patch('builtins.input', side_effect=[
        "2019-3-15", "13:00 PM", "11:00 AM", "500", "70", "n"
    ])
    def test_main_invalid_time(self, mock_input):
        """Test main function with invalid time input"""
        print("\nTest: Main Function - Invalid Time Handling")

        with patch('builtins.print') as mock_print:
            main()
            printed_items = [str(call[0][0]) for call in mock_print.call_args_list if call[0]]
            self.assertTrue(
                any("time" in item.lower() for item in printed_items),
                "Should show error message for invalid time"
            )


if __name__ == '__main__':
    # Create a test suite with more detailed output
    unittest.main(verbosity=2)
