### Question 1 - Write a code segment that opens a file named file.txt for input and prints the number of lines in that file.

## Reading Lines from a File in Python

This code demonstrates how to read and count the number of lines in a text file using Python.

## Code Example

```python
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
```

## Code Explanation

Let's break down how this code works:

1. `with open("file.txt", "r") as file`:
    - Opens the file named "file.txt" in read mode ("r")
    - Uses a context manager (`with`) that automatically closes the file when done

2. `lines = file.readlines()`:
    - `readlines()` reads all lines from the file into a list
    - Each line in the file becomes an element in the `lines` list
    - Each line includes the newline character (`\n`) at the end

3. `print(f"Number of lines: {len(lines)})`:
    - `len(lines)` counts the number of elements in the list
    - Uses an f-string to format the output message

## Example Output

If `file.txt` contains:
```
This is a test file
Hello Student
Testing 1,2,3 - testing !
Python rocks !
```

The code will output:
```
Number of lines: 4
```

## Key Points

- `readlines()` loads the entire file into memory at once
- Each line includes the trailing newline character
- Empty lines in the file are also counted
- The file is automatically closed after the `with` block
