## Random Letter Generator and Sorting Guide

This Python program demonstrates various sorting operations on randomly generated letters using list comprehension and built-in sorting functions.

## Code Components

**Random Letter Generation**
```python
import random
random_letters = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]
```
This code:
- Imports the random module for letter generation
- Uses list comprehension to create 10 random letters
- Selects letters from the lowercase alphabet string
- Stores results in `random_letters` list

## Sorting Operations

**Ascending Order Sort**
```python
ascending_order = sorted(random_letters)
```
- Creates a new list with letters arranged A to Z
- Preserves the original list
- Uses the built-in `sorted()` function

**Descending Order Sort**
```python
descending_order = sorted(random_letters, reverse=True)
```
- Creates a new list with letters arranged Z to A
- Uses the `reverse=True` parameter
- Maintains original list integrity

**Unique Sorted Values**
```python
unique_sorted = sorted(set(random_letters))
```
- Converts list to set to remove duplicates
- Sorts remaining unique letters
- Returns a new list in ascending order

## Sample Output
```python
Original list: ['p', 'k', 'w', 'a', 'k', 'z', 'b', 'x', 'p', 'q']
Ascending order: ['a', 'b', 'k', 'k', 'p', 'p', 'q', 'w', 'x', 'z']
Descending order: ['z', 'x', 'w', 'q', 'p', 'p', 'k', 'k', 'b', 'a']
Unique values sorted: ['a', 'b', 'k', 'p', 'q', 'w', 'x', 'z']
```

## Key Features

- Demonstrates three different sorting approaches
- Shows how to remove duplicates using `set()`
- Uses non-destructive sorting with `sorted()`
- Implements list comprehension for random generation
- Provides both ascending and descending sort examples