from datetime import datetime, timedelta
from dateutil import parser, relativedelta
import re

# Get current date once and remove time component
CURRENT_DATE = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


def validate_name(name):
    """
    Validate the name input.
    Returns cleaned name or raises ValueError with specific message.
    """
    if not name:
        raise ValueError("Name cannot be empty.")

    # Remove extra whitespace and check length
    cleaned_name = " ".join(name.split())
    if len(cleaned_name) > 50:
        raise ValueError("Name is too long (maximum 50 characters).")

    # Check for invalid characters
    if not all(c.isalpha() or c.isspace() or c in "-'" for c in cleaned_name):
        raise ValueError("Name can only contain letters, spaces, hyphens, and apostrophes.")

    return cleaned_name


def get_birth_date(date_str):
    """
    Convert MM/DD/YY format to datetime object using dateutil parser.
    Raises ValueError for invalid dates.
    """
    # Verify the format first
    if not re.match(r'^\d{2}/\d{2}/\d{2}$', date_str):
        raise ValueError("Date must be in MM/DD/YY format (e.g., 06/01/69)")

    try:
        # Parse the date using dateutil
        birth_date = parser.parse(date_str, dayfirst=False)

        # Adjust the year if it's later than current year
        if birth_date.year > CURRENT_DATE.year:
            birth_date = birth_date.replace(year=birth_date.year - 100)

        # Verify it's not in the future
        if birth_date > CURRENT_DATE:
            raise ValueError("Birth date cannot be in the future")

        # Verify it's not too far in the past
        if birth_date.year < CURRENT_DATE.year - 130:
            raise ValueError("Birth date seems unreasonably old (over 130 years)")

        return birth_date

    except (ValueError, parser.ParserError) as e:
        raise ValueError(f"Invalid date: {str(e)}")


def calculate_age(birth_date):
    """
    Calculate age in years or days using relativedelta for years
    and timedelta for days.
    """
    # Calculate exact age using relativedelta for years
    age_rel = relativedelta.relativedelta(CURRENT_DATE, birth_date)
    years_old = age_rel.years

    # For under 2 years, calculate exact days using timedelta
    if years_old < 2:
        days_old = (CURRENT_DATE - birth_date).days
        return f"{days_old} days old"
    else:
        return f"{years_old} years old"


def calculate_days_to_birthday(birth_date):
    """
    Calculate days until next birthday using timedelta.
    Handles leap years correctly.
    """
    # Create next birthday date
    next_birthday = birth_date.replace(year=CURRENT_DATE.year)

    # If birthday has passed this year, look at next year
    if next_birthday < CURRENT_DATE:
        next_birthday = birth_date.replace(year=CURRENT_DATE.year + 1)

    # Calculate days until birthday
    days_until = (next_birthday - CURRENT_DATE).days

    # Handle special cases
    if days_until == 0:
        return "today"
    elif days_until == 1:
        return "tomorrow"
    elif days_until == -1:
        return "yesterday"
    else:
        return f"in {days_until} days"


def format_date(date):
    """Format date as 'Day, Month DD, YYYY'."""
    return date.strftime("%A, %B %d, %Y")


def get_valid_name():
    """Get and validate name input from user."""
    while True:
        try:
            name = input("Enter name: ")
            return validate_name(name)
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Please try again.")


def get_valid_date():
    """Get and validate date input from user."""
    while True:
        try:
            date_str = input("Enter birthday (MM/DD/YY): ")
            return get_birth_date(date_str)
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Please try again.")


def get_continue_response():
    """Get and validate continue response from user."""
    while True:
        response = input("Continue? (y/n): ").lower().strip()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' for yes or 'n' for no.")


def main():
    print("Birthday Calculator")
    print("-" * 20)
    print(f"Current date: {format_date(CURRENT_DATE)}\n")

    while True:
        try:
            # Get valid inputs
            name = get_valid_name()
            birth_date = get_valid_date()

            # Display results
            print("\nResults:")
            print("-" * 8)
            print(f"Birthday:  {format_date(birth_date)}")
            print(f"Today:     {format_date(CURRENT_DATE)}")

            # Calculate and display age
            age_str = calculate_age(birth_date)
            print(f"{name} is {age_str}.")

            # Calculate and display days to birthday
            birthday_str = calculate_days_to_birthday(birth_date)
            print(f"{name}'s birthday is {birthday_str}.")

            # Ask to continue
            print()
            if not get_continue_response():
                print("\nBye!")
                break
            print()

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again.")
            print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        print("Program terminated.")
