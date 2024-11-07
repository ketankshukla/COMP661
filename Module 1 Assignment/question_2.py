from datetime import datetime
from dateutil import parser, relativedelta

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


def main():
    print("Birthday Calculator")
    print("-" * 20)
    print(f"Current date: {CURRENT_DATE.strftime('%A, %B %d, %Y')}\n")

    while True:
        # Get inputs (assuming valid format)
        name = input("Enter name: ").strip()
        birth_date = parser.parse(input("Enter birthday (MM/DD/YY): "))

        # Adjust year for two-digit input
        if birth_date.year > CURRENT_DATE.year:
            birth_date = birth_date.replace(year=birth_date.year - 100)

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
