from datetime import datetime
from dateutil import relativedelta

CURRENT_DATE = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

def calculate_age(birth_date):
    """Calculate age in years or days"""
    age_rel = relativedelta.relativedelta(CURRENT_DATE, birth_date)
    years_old = age_rel.years

    if years_old < 2:
        days_old = (CURRENT_DATE - birth_date).days
        return f"{days_old} days old"
    return f"{years_old} years old"

def calculate_days_to_birthday(birth_date):
    """Calculate days until next birthday"""
    next_birthday = birth_date.replace(year=CURRENT_DATE.year)
    if next_birthday < CURRENT_DATE:
        next_birthday = birth_date.replace(year=CURRENT_DATE.year + 1)

    days_until = (next_birthday - CURRENT_DATE).days

    if days_until == 0:
        return "today"
    elif days_until == 1:
        return "tomorrow"
    elif days_until == -1:
        return "yesterday"
    return f"in {days_until} days"

def get_valid_name():
    while True:
        name = input("Enter name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please enter a valid name.")

def get_valid_birth_date():
    while True:
        birth_date_input = input("Enter birthday (MM/DD/YY): ").strip()

        # Check for invalid format
        if not birth_date_input or len(birth_date_input) < 6 or len(birth_date_input) > 8:
            print("Invalid date format. Please enter a date in MM/DD/YY format.")
            continue

        try:
            # Split the input into month, day, year
            month_str, day_str, year_str = birth_date_input.split('/')

            # Convert to integers
            month = int(month_str)
            day = int(day_str)
            year = int(year_str)

            # Adjust for two-digit year
            if 0 <= year <= 99:
                if 0 <= year <= 24:
                    year += 2000
                else:
                    year += 1900
            else:
                # If user enters a four-digit year
                pass

            # Create date object
            birth_date = datetime(year, month, day)

            # Check if the birth date is in the future
            if birth_date > CURRENT_DATE:
                print("Birth date cannot be in the future. Please enter a valid date.")
                continue

            return birth_date
        except ValueError:
            print("Invalid date format. Please enter a date in MM/DD/YY format.")

def main():
    print("Birthday Calculator")
    print("-" * 20)
    print(f"Current date: {CURRENT_DATE.strftime('%A, %B %d, %Y')}\n")

    while True:
        # Get inputs with validation
        name = get_valid_name()
        birth_date = get_valid_birth_date()

        # Display results
        print("\nResults:")
        print("-" * 8)
        print(f"Birthday:  {birth_date.strftime('%A, %B %d, %Y')}")
        print(f"Today:     {CURRENT_DATE.strftime('%A, %B %d, %Y')}")
        print(f"{name} is {calculate_age(birth_date)}.")
        print(f"{name}'s birthday is {calculate_days_to_birthday(birth_date)}.")

        # Continue prompt
        if input("\nContinue? (y/n): ").lower().strip() != 'y':
            print("\nBye!")
            break
        print()

if __name__ == "__main__":
    main()
