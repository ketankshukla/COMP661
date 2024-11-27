### Question 3 - Write a code segment that opens a file for input and prints the number of five-letter words in the file.

## Listing Directory Contents in Python

This guide explains how to list all items (files and directories) in the current working directory using Python's `os` module.

## Code Example

```python
import os

items = os.listdir()
print("Items in the current directory:")
for item in items:
    print(item)
```

## Code Breakdown

1. `import os`:
    - Imports Python's built-in `os` module
    - This module provides functions for interacting with the operating system
    - Includes functionality for file and directory operations

2. `items = os.listdir()`:
    - `os.listdir()` returns a list of entries in the current working directory
    - When called with no arguments, it uses the current directory
    - Returns both files and directories
    - The returned names are in arbitrary order

3. `print("Items in the current directory:")`:
    - Prints a header message for the list of items

4. `for item in items: print(item)`:
    - Iterates through each item in the list
    - Prints each item name on a new line

## Example Output in my case will be

```
accounts.txt
file.txt
question_1.md
question_1.png
question_1.py
question_2.md
question_2.png
question_2.py
question_3.md
question_3.py
question_4.md
question_4.py
question_6.md
question_6.py
```

## Key Points

- `os.listdir()` shows both files and directories
- Directory entries are shown without their trailing slash
- Hidden files (starting with '.') are included in the list
- The order of items is not guaranteed
- By default, it lists the current working directory
- You can specify a different directory by passing a path to `os.listdir(path)`

## Common Variations

1. List items in a specific directory:
```python
items = os.listdir('/path/to/directory')
```

2. Get full paths of items:
```python
items = [os.path.join(os.getcwd(), item) for item in os.listdir()]
```

3. Filter for only files:
```python
files = [item for item in os.listdir() if os.path.isfile(item)]
```

4. Filter for only directories:
```python
directories = [item for item in os.listdir() if os.path.isdir(item)]
```
