### Question 6 -  In the accounts.txt file:

- update the name 'Zoltar' to 'Robert'
- create a tempfile with the new data
- remove accounts.txt file from the directory
- rename the tempfile to a new file called myaccounts.txt

## I got really creative with this one! 

## Interactive File Content Management System

## Overview
This Python script provides an interactive system for managing file content, specifically designed to handle account information stored in text files. The system allows users to replace names in files, display file contents, and reset files to their original state.

## Code Structure

### 1. Required Imports and Setup
```python
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("\nFile Content Management System")
    print("-" * 30)
```

### 2. File Access Helper
```python
def wait_for_file_access(filename, max_attempts=10):
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(filename, "r"):
                return True
        except:
            time.sleep(0.1)
            attempts += 1
    return False

def cleanup_temp_files():
    if os.path.exists("tempfile.txt"):
        try:
            os.remove("tempfile.txt")
        except:
            pass
```

### 3. Core Functions

#### Name Replacement Function
```python
def replace_name():
    try:
        # Step 1: Create temp file with replacements
        print(" Reading from accounts.txt")
        with open("accounts.txt", "r") as infile:
            content = infile.read()
            
        with open("tempfile.txt", "w") as tempfile:
            tempfile.write(content.replace("Zoltar", "Robert"))
        print(" Created temporary file with replacements")
        
        # Step 2: Remove existing files
        if os.path.exists("myaccounts.txt"):
            os.remove("myaccounts.txt")
            print(" Removed existing myaccounts.txt")

        if os.path.exists("accounts.txt"):
            os.remove("accounts.txt")
            print(" Removed original accounts.txt")

        # Step 3: Rename temp file
        if wait_for_file_access("tempfile.txt"):
            os.rename("tempfile.txt", "myaccounts.txt")
            print(" Renamed temporary file to myaccounts.txt")
            print(" Temporary file deleted")
            print(" Name replacement complete")
            
            # Display the new content
            print("\nContents of myaccounts.txt:")
            print("-" * 25)
            with open("myaccounts.txt", "r") as file:
                print(file.read())
            print("-" * 25)
    except Exception as e:
        print(f"Error during replacement: {e}")
        cleanup_temp_files()
```

#### Reset Function
```python
def reset_files():
    # Original content for creating accounts.txt if needed
    original_content = """100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32"""

    # Delete myaccounts.txt if it exists
    if os.path.exists("myaccounts.txt"):
        try:
            os.remove("myaccounts.txt")
            print(" Removed myaccounts.txt")
        except Exception as e:
            print(f"Error removing myaccounts.txt: {e}")

    # Only create accounts.txt if it doesn't exist
    if not os.path.exists("accounts.txt"):
        try:
            with open("accounts.txt", "w") as file:
                file.write(original_content)
            print(" Created accounts.txt file with original content")
        except Exception as e:
            print(f"Error creating accounts.txt: {e}")
    else:
        print(" Original accounts.txt file is already in place")
        print("\nCurrent content of accounts.txt:")
        print("-" * 25)
        with open("accounts.txt", "r") as file:
            print(file.read())
        print("-" * 25)
```

#### Display Function
```python
def display_file_content(filename):
    try:
        if os.path.exists(filename):
            print(f"\nCurrent content of {filename}:")
            print("-" * 25)
            with open(filename, "r") as file:
                print(file.read())
            print("-" * 25)
        else:
            print(f"File {filename} does not exist.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
```

### 4. Main Program Loop
```python
def main():
    while True:
        print_header()
        print("\nMenu Options:")
        print("1. Replace names")
        print("2. Display files")
        print("3. Reset files")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            replace_name()
        elif choice == "2":
            display_file_content("accounts.txt")
            display_file_content("myaccounts.txt")
        elif choice == "3":
            reset_files()
        elif choice == "4":
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

## Features

### 1. Name Replacement
- Replace "Zoltar" with "Robert" in the account records
- Uses a safe replacement process with temporary files
- Displays detailed progress messages for each operation
- Shows the modified file content after replacement

### 2. File Display
- Views the contents of both original and modified account files
- Presents file contents in a clear, formatted manner
- Handles file reading errors gracefully

### 3. Reset Functionality
- Removes the modified file (myaccounts.txt)
- Preserves the original file (accounts.txt) if it exists
- Creates accounts.txt with default content only if it doesn't exist
- Shows the current state of files after reset

### 4. Error Handling
- Manages file access issues
- Cleans up temporary files in case of errors
- Provides clear error messages
- Includes waiting mechanisms to handle file system timing

## File Structure
- `accounts.txt`: Original file containing account records
- `myaccounts.txt`: Modified file with replaced names
- `tempfile.txt`: Temporary file used during the replacement process (automatically cleaned up)

## Default File Content
```
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32
```

## Usage Guide

### Main Menu Options
1. **Replace Names**: Replaces "Zoltar" with "Robert" in the account records
2. **Display Files**: Shows the contents of existing account files
3. **Reset Files**: Restores the original file state
4. **Exit**: Closes the application

### Example Operations

#### 1. Replacing Names
When you select option 1, the system will show:
```
Reading from accounts.txt
Created temporary file with replacements
Removed existing myaccounts.txt (if it exists)
Removed original accounts.txt
Renamed temporary file to myaccounts.txt
Temporary file deleted
Name replacement complete

Contents of myaccounts.txt:
-------------------------
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Robert -32.16
500 Kathleen 24.32
-------------------------
```

#### 2. Displaying Files
When you select option 2, the system will show the contents of any existing account files:
```
Current content of accounts.txt:
-------------------------
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32
-------------------------

Current content of myaccounts.txt:
-------------------------
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Robert -32.16
500 Kathleen 24.32
-------------------------
```

#### 3. Resetting Files
When you select option 3, the system will:
```
Removed myaccounts.txt
Original accounts.txt file is already in place

Current content of accounts.txt:
-------------------------
100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32
-------------------------
```
Or if accounts.txt doesn't exist:
```
Removed myaccounts.txt
Created accounts.txt file with original content
```

#### 4. Exiting the Program
When you select option 4, the system will:
```
Thank you for using the program. Goodbye!
```

## Implementation Details

### Safety Features
- Uses temporary files for safe replacements
- Implements file access checks
- Includes timing delays to prevent file access conflicts
- Cleans up temporary files automatically

### Error Prevention
- Checks file existence before operations
- Validates file access permissions
- Handles file operation exceptions
- Provides clear feedback for all operations

## Notes
- The system maintains data integrity by using temporary files
- All operations are clearly logged to the console
- File contents are displayed after major operations for verification
- The reset function preserves the original file when possible
