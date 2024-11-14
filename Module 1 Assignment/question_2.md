## Documentation Guide for Birthday Calculator Python Code

This documentation provides a detailed overview of the Python code designed to calculate a person's age and the number of days until their next birthday based on user input.

### Overview

The program allows users to input their name and birth date, calculates the user's age in years or days, and determines how many days remain until their next birthday. It ensures proper input validation and displays the results in a user-friendly format.

### Constants

- `CURRENT_DATE`: A constant that holds the current date with the time set to midnight (00:00:00).

### Functions

#### `calculate_age(birth_date)`

**Description:**  
Calculates the age of the user based on their birth date. It returns the age in years if the user is 2 years old or older; otherwise, it returns the age in days.

**Parameters:**
- `birth_date` (datetime): The user's birth date.

**Returns:**  
A string indicating the user's age in either "X years old" or "X days old".

---

#### `calculate_days_to_birthday(birth_date)`

**Description:**  
Calculates how many days remain until the user's next birthday.

**Parameters:**
- `birth_date` (datetime): The user's birth date.

**Returns:**  
A string indicating how many days until the next birthday, including special cases for today, tomorrow, and yesterday.

---

#### `get_valid_name()`

**Description:**  
Prompts the user to input their name and ensures that it is not empty.

**Returns:**  
A string representing a valid name.

---

#### `get_valid_birth_date()`

**Description:**  
Prompts the user to input a valid birth date in MM/DD/YY format. It validates the format and checks that the date is not in the future.

**Returns:**  
A `datetime` object representing a valid birth date.

---

### Main Functionality

#### `main()`

**Description:**  
The main function that manages user interaction. It:
1. Displays a welcome message and the current date.
2. Repeatedly prompts for user inputs using validation functions.
3. Calls `calculate_age()` and `calculate_days_to_birthday()` to compute age and upcoming birthday details.
4. Displays the results and allows users to continue or exit.

---

### Usage

To run this program:

1. Ensure you have Python installed on your machine.
2. Copy the code into a Python file (e.g., `birthday_calculator.py`).
3. Execute the script using Python from your command line or terminal:
   ```bash
   python birthday_calculator.py
   ```
4. Follow the prompts to enter your name and birth date.

### Example Interaction

```
Birthday Calculator
--------------------
Current date: Wednesday, November 13, 2024

Enter name: John Doe
Enter birthday (MM/DD/YY): 05/15/90

Results:
--------
Birthday:  Saturday, May 15, 1990
Today:     Wednesday, November 13, 2024
John Doe is 34 years old.
John Doe's birthday is in 154 days.

Continue? (y/n): n

Bye!
```

### Conclusion

This program serves as an interactive tool for calculating age and determining how many days are left until a birthday. By implementing thorough input validation, it enhances user experience while minimizing errors during data entry.