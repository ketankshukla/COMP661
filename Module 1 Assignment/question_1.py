from datetime import datetime, timedelta
import re


def validate_date(date_str):
    """Validate date format and values."""
    try:
        # Check format
        if not re.match(r'^\d{4}-\d{1,2}-\d{1,2}$', date_str):
            return False, "Date must be in YYYY-MM-DD format"

        # Parse date to check if valid
        year, month, day = map(int, date_str.split('-'))
        datetime(year, month, day)

        # Additional checks
        if year < 1900 or year > 2100:
            return False, "Year must be between 1900 and 2100"

        return True, ""
    except ValueError as e:
        return False, f"Invalid date: {str(e)}"


def validate_time(time_str):
    """Validate time format and values."""
    try:
        # Check basic format
        if not re.match(r'^\d{1,2}:\d{2} [AaPpMm]{2}$', time_str):
            return False, "Time must be in HH:MM AM/PM format"

        # Split time into components
        time_part, meridiem = time_str.split()
        hours, minutes = map(int, time_part.split(':'))

        # Validate hours and minutes
        if hours < 1 or hours > 12:
            return False, "Hours must be between 1 and 12"
        if minutes < 0 or minutes > 59:
            return False, "Minutes must be between 00 and 59"
        if meridiem.upper() not in ['AM', 'PM']:
            return False, "Time must end with AM or PM"

        return True, ""
    except ValueError as e:
        return False, "Invalid time format"


def get_valid_integer_input(prompt, min_value=1, max_value=10000):
    """Get and validate integer input."""
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                print("Input cannot be empty.")
                continue

            num = int(value)
            if num < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if num > max_value:
                print(f"Value must not exceed {max_value}.")
                continue
            return num
        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_date():
    """Get and validate date input."""
    while True:
        date_str = input("Estimated date of departure (YYYY-MM-DD): ").strip()
        valid, error_message = validate_date(date_str)
        if valid:
            return date_str
        print(error_message)


def get_valid_time():
    """Get and validate time input."""
    while True:
        time_str = input("Estimated time of departure (HH:MM AM/PM): ").strip()
        valid, error_message = validate_time(time_str)
        if valid:
            return time_str
        print(error_message)


def get_continue_response():
    """Get and validate continue response."""
    while True:
        response = input("Continue? (y/n): ").strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' for yes or 'n' for no.")


def calculate_travel_time(miles, mph):
    """Calculate travel time in hours and minutes."""
    total_minutes = (miles * 60) // mph
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes


def calculate_arrival_datetime(departure_date_str, departure_time_str, hours, minutes):
    """Calculate arrival date and time."""
    departure_str = f"{departure_date_str} {departure_time_str}"
    departure_datetime = datetime.strptime(departure_str, "%Y-%m-%d %I:%M %p")
    travel_time = timedelta(hours=hours, minutes=minutes)
    arrival_datetime = departure_datetime + travel_time
    return arrival_datetime


def get_trip_inputs():
    """Get all inputs needed for trip calculation."""
    departure_date = get_valid_date()
    departure_time = get_valid_time()
    print()  # Add blank line before numeric inputs
    miles = get_valid_integer_input("Enter miles: ", min_value=1, max_value=5000)
    mph = get_valid_integer_input("Enter miles per hour: ", min_value=1, max_value=200)
    return departure_date, departure_time, miles, mph


def format_results(hours, minutes, arrival_datetime):
    """Format the calculation results."""
    return {
        'hours': hours,
        'minutes': minutes,
        'arrival_date': arrival_datetime.strftime('%Y-%m-%d'),
        'arrival_time': arrival_datetime.strftime('%I:%M %p')
    }


def print_results(results):
    """Print the calculation results."""
    print("\nEstimated travel time")
    print(f"Hours: {results['hours']}")
    print(f"Minutes: {results['minutes']}")
    print(f"Estimated date of arrival: {results['arrival_date']}")
    print(f"Estimated time of arrival: {results['arrival_time']}")


def main():
    print("Arrival Time Estimator")

    while True:
        try:
            # Get all inputs
            departure_date, departure_time, miles, mph = get_trip_inputs()

            # Calculate travel time
            hours, minutes = calculate_travel_time(miles, mph)

            # Calculate arrival datetime
            arrival_datetime = calculate_arrival_datetime(
                departure_date, departure_time, hours, minutes)

            # Format and print results
            results = format_results(hours, minutes, arrival_datetime)
            print_results(results)

            # Check if user wants to continue
            print()
            if not get_continue_response():
                print("Bye!")
                break
            print()

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")
            print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Program will now exit.")
