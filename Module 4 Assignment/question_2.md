### Question 2 - Write a code segment that opens a file for input and prints the number of five-letter words in the file.

## Understanding Word Length Analysis in Python

This document explains how Python handles word length analysis and demonstrates the difference between counting character sequences versus true words.

## The Problem

When analyzing text to find words of a specific length, we need to consider what constitutes a "word". Should sequences like "1,2,3" be counted as a five-letter word? Let's explore this with two different approaches.

## Test Data

Our sample text file (`file.txt`) contains:
```
This is a test file
Hello Student
Testing 1,2,3 - testing !
Python rocks !
```

## Original Code

The original code simply counts any sequence of 5 characters as a word:

```python
with open("file.txt", "r") as file:
    text = file.read()
    words = text.split()
    five_letter_words = [word for word in words if len(word) == 5]
    print(f"Number of five-letter words: {len(five_letter_words)}")
```

This code will count "1,2,3" as a five-letter word because:
1. `split()` separates the text on whitespace, treating "1,2,3" as one unit
2. The length check only counts the number of characters (5 in this case)
3. No distinction is made between letters, numbers, or punctuation

## Enhanced Analysis Code

Here's a modified version that provides detailed analysis of each word:

```python
with open("file.txt", "r") as file:
    text = file.read()
    words = text.split()
    
    print("Analyzing all words:")
    for word in words:
        if len(word) == 5:
            print(f"'{word}' - Length: {len(word)} characters")
            print(f"  - Contains only letters? {word.isalpha()}")
            print(f"  - Contains numbers? {any(char.isdigit() for char in word)}")
            print(f"  - Contains punctuation? {any(not char.isalnum() for char in word)}")
            print()

    # Two different counts for comparison
    five_letter_words = [word for word in words if len(word) == 5]
    five_letter_real_words = [word for word in words if len(word) == 5 and word.isalpha()]
    
    print(f"Number of 5-character sequences: {len(five_letter_words)}")
    print(f"Number of true 5-letter words (letters only): {len(five_letter_real_words)}")
```

## Analysis Results

When we run the enhanced code, we get this output:
```
Analyzing all words:
'Hello' - Length: 5 characters
  - Contains only letters? True
  - Contains numbers? False
  - Contains punctuation? False

'1,2,3' - Length: 5 characters
  - Contains only letters? False
  - Contains numbers? True
  - Contains punctuation? True

'rocks' - Length: 5 characters
  - Contains only letters? True
  - Contains numbers? False
  - Contains punctuation? False

Number of 5-character sequences: 3
Number of true 5-letter words (letters only): 2
```

## Key Findings

1. **Character Sequences vs. True Words**
    - The text contains three 5-character sequences: "Hello", "1,2,3", and "rocks"
    - Only two of these ("Hello" and "rocks") are true words containing only letters

2. **Why "1,2,3" is Special**
    - It's 5 characters long (three numbers and two commas)
    - Contains both numbers and punctuation
    - Is not a true word in the linguistic sense

3. **Choosing the Right Approach**
    - Use `len(word) == 5` to count all 5-character sequences
    - Use `len(word) == 5 and word.isalpha()` to count only true 5-letter words

## Conclusion

The choice between counting all 5-character sequences versus only true words depends on your specific needs. For most linguistic applications, using `isalpha()` to filter out non-letter sequences would be more appropriate.
