## Documentation Guide for Arrival Time Estimator Python Code

This documentation provides a comprehensive overview of the Python code designed to estimate the arrival time based on user inputs, including departure date, departure time, distance in miles, and speed in miles per hour.

### Overview

The program calculates the estimated arrival time for a journey based on the provided parameters. It prompts the user for input, validates it, computes the travel duration, and displays the estimated arrival time.

### Functions

#### `calculate_arrival(departure_date, departure_time, miles, speed)`

**Description:**  
Calculates the estimated arrival time based on the departure date, departure time, distance in miles, and speed in miles per hour.

**Parameters:**
- `departure_date` (str): The date of departure in the format "YYYY-MM-DD".
- `departure_time` (str): The time of departure in the format "HH:MM AM/PM".
- `miles` (int): The total distance to be traveled in miles.
- `speed` (int): The speed of travel in miles per hour.

**Returns:**  
A tuple containing:
- `hours` (int): The number of hours of travel.
- `minutes` (int): The number of minutes of travel.
- `arrival_date` (str): The estimated date of arrival in "YYYY-MM-DD" format.
- `arrival_time` (str): The estimated time of arrival in "HH:MM AM/PM" format.

---

#### `get_valid_date()`

**Description:**  
Prompts the user to input a valid departure date and ensures it is in the correct format.

**Returns:**  
A string representing a valid date in "YYYY-MM-DD" format.

---

#### `get_valid_time()`

**Description:**  
Prompts the user to input a valid departure time and ensures it is in the correct format.

**Returns:**  
A string representing a valid time in "HH:MM AM/PM" format.

---

#### `get_valid_miles()`

**Description:**  
Prompts the user to input a valid number of miles for the journey and ensures it is a non-negative integer.

**Returns:**  
An integer representing the number of miles.

---

#### `get_valid_speed()`

**Description:**  
Prompts the user to input a valid speed for travel and ensures it is a positive integer.

**Returns:**  
An integer representing the speed in miles per hour.

---

### Main Functionality

#### `main()`

**Description:**  
The main function that orchestrates user interaction. It:
1. Displays a welcome message.
2. Repeatedly prompts for user inputs using validation functions.
3. Calls `calculate_arrival()` to compute travel time and arrival details.
4. Displays the estimated travel time and allows users to continue or exit.

---

### Usage

To run this program:

1. Ensure you have Python installed on your machine.
2. Copy the code into a Python file (e.g., `arrival_estimator.py`).
3. Execute the script using Python from your command line or terminal:
   ```bash
   python arrival_estimator.py
   ```
4. Follow the prompts to enter your travel details.

### Example Interaction

```
Arrival Time Estimator
Estimated date of departure (YYYY-MM-DD): 2024-11-15
Estimated time of departure (HH:MM AM/PM): 10:30 AM
Enter miles: 120
Enter miles per hour: 60

Estimated travel time
Hours: 2
Minutes: 0
Estimated date of arrival: 2024-11-15
Estimated time of arrival: 12:30 PM

Continue? (y/n): n
Bye!
```

### Conclusion

This program serves as a simple yet effective tool for estimating travel times based on user-defined parameters. By ensuring proper input validation, it enhances user experience and minimizes errors during data entry.