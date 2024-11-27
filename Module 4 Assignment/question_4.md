### Question 4 - Write a code segment that prompts the user for a file. If the file does not exist then the program should print an error. Otherwise, the program should print its contents.

## Reading Files with Error Handling in Python

This guide explains how to safely read a file by first checking if it exists, using Python's `os` module and file handling capabilities.

## Code Example

```python
import os

filename = input("Enter the filename: ")
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("File contents:")
        print(file.read())
else:
    print("Error: File does not exist.")
```

## Code Breakdown

### 1. Module Import
```python
import os
```
- Imports the `os` module
- Provides functions for interacting with the operating system
- Used here for checking file existence

### 2. User Input
```python
filename = input("Enter the filename: ")
```
- Prompts the user to enter a filename
- Stores the input in the `filename` variable
- Input can be a relative or absolute path

### 3. File Existence Check
```python
if os.path.exists(filename):
```
- Uses `os.path.exists()` to check if the file exists
- Returns `True` if the file exists, `False` otherwise
- Prevents errors from trying to open non-existent files

### 4. File Reading
```python
with open(filename, "r") as file:
    print("File contents:")
    print(file.read())
```
- Opens the file in read mode ("r")
- Uses a `with` statement for proper file handling
- Reads and prints the entire file contents
- File is automatically closed after the `with` block

### 5. Error Handling
```python
else:
    print("Error: File does not exist.")
```
- Executes if the file doesn't exist
- Provides a user-friendly error message
- Prevents the program from crashing

## Example Usage

```
# Example 1: File exists
Enter the filename: example.txt
File contents:
Hello, this is a test file.
It has multiple lines.
The end.

# Example 2: File doesn't exist
Enter the filename: nonexistent.txt
Error: File does not exist.
```

## Key Points

1. **Safety Features**
    - Checks file existence before attempting to read
    - Uses `with` statement for automatic file closure
    - Provides clear error messages

2. **File Handling**
    - Opens file in read-only mode
    - Reads entire file contents at once
    - Preserves line breaks in output

3. **User Interaction**
    - Takes filename from user input
    - Shows clear prompts and messages
    - Handles both success and error cases

## Common Variations

1. **Reading line by line:**
```python
if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
```

2. **Adding path validation:**
```python
if os.path.exists(filename) and os.path.isfile(filename):
    # proceed with file reading
```

3. **Including file size check:**
```python
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    # proceed with non-empty file
```

## Best Practices

1. **Error Handling**
    - Always check if file exists before opening
    - Use try-except blocks for additional error handling
    - Provide clear error messages

2. **File Operations**
    - Use `with` statement for file operations
    - Close files properly (automatic with `with`)
    - Use appropriate file modes ("r" for reading)

3. **User Experience**
    - Provide clear prompts and messages
    - Handle both success and failure cases
    - Give meaningful feedback

## Common Issues and Solutions

1. **File Path Issues**
    - Use raw strings for Windows paths: `r"C:\path\to\file.txt"`
    - Use `os.path.join()` for path construction
    - Handle both relative and absolute paths

2. **Encoding Issues**
```python
with open(filename, "r", encoding="utf-8") as file:
    # handles text encoding explicitly
```

3. **Large File Handling**
```python
with open(filename, "r") as file:
    for line in file:  # reads line by line instead of all at once
        print(line.strip())
```
