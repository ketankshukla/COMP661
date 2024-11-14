from datetime import datetime, timedelta


def calculate_arrival(departure_date, departure_time, miles, speed):
    """Calculate arrival time based on inputs"""
    # Calculate travel duration
    total_minutes = (miles * 60) // speed
    hours, minutes = divmod(total_minutes, 60)

    # Calculate arrival datetime
    departure = datetime.strptime(f"{departure_date} {departure_time}", "%Y-%m-%d %I:%M %p")
    arrival = departure + timedelta(hours=hours, minutes=minutes)

    return hours, minutes, arrival.strftime('%Y-%m-%d'), arrival.strftime('%I:%M %p')


def get_valid_date():
    while True:
        date = input("Estimated date of departure (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_valid_time():
    while True:
        time = input("Estimated time of departure (HH:MM AM/PM): ").strip()
        try:
            datetime.strptime(time, "%I:%M %p")  # Validate time format
            return time
        except ValueError:
            print("Invalid time format. Please use HH:MM AM/PM.")


def get_valid_miles():
    while True:
        miles_input = input("Enter miles: ").strip()
        try:
            miles = int(miles_input)
            if miles < 0:
                print("Miles cannot be negative. Please enter a positive number.")
                continue
            return miles
        except ValueError:
            print("Please enter a valid integer for miles.")


def get_valid_speed():
    while True:
        speed_input = input("Enter miles per hour: ").strip()
        try:
            speed = int(speed_input)
            if speed <= 0:
                print("Speed must be greater than zero. Please enter a valid speed.")
                continue
            return speed
        except ValueError:
            print("Please enter a valid integer for speed.")


def main():
    print("Arrival Time Estimator")

    while True:
        # Get inputs with validation
        date = get_valid_date()
        time = get_valid_time()
        miles = get_valid_miles()
        speed = get_valid_speed()

        # Calculate and display results
        hours, minutes, arrival_date, arrival_time = calculate_arrival(date, time, miles, speed)

        print("\nEstimated travel time")
        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")
        print(f"Estimated date of arrival: {arrival_date}")
        print(f"Estimated time of arrival: {arrival_time}")

        # Check if user wants to continue
        if input("\nContinue? (y/n): ").lower() != 'y':
            print("Bye!")
            break
        print()


if __name__ == "__main__":
    main()