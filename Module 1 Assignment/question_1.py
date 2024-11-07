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


def main():
    print("Arrival Time Estimator")

    while True:
        # Get inputs
        date = input("Estimated date of departure (YYYY-MM-DD): ").strip()
        time = input("Estimated time of departure (HH:MM AM/PM): ").strip()
        miles = int(input("Enter miles: "))
        speed = int(input("Enter miles per hour: "))

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
