The code counts the number of duplicate words in a given sentence. 
It treats uppercase and lowercase letters the same and assumes there is no punctuation in the sentence. 
Words that appear more than once are considered duplicates, and the script outputs these words along with 
their counts.

Here are the steps:

---

## 1. Input text

```python
# Input Text
input_text = ("Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked "
              "if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked")
```

- The variable `input_text` contains the sentence we want to analyze.

---

## 2. Convert text to lowercase and split into words

```python
# Convert text to lowercase and split into words
words = input_text.lower().split()
```

- `input_text.lower()` converts all characters in the text to lowercase. This ensures that words like "Peter" and "peter" are considered the same.
- `.split()` divides the text into a list of words based on whitespace.
- The resulting list `words` contains all the words in lowercase.

```python
['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', 'a', 'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked', 'if', 'peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers', 'where', 'is', 'the', 'peck', 'of', 'pickled', 'peppers', 'peter', 'piper', 'picked']
```

## 3. Count the frequency of each word

```python
# Count the frequency of each word
frequency = {}
for word in words:
  frequency[word] = frequency.get(word, 0) + 1
```

- An empty dictionary `freq` is initialized to store word counts.
- The `for` loop iterates over each `word` in the `words` list.
- `freq.get(word, 0)` checks if the `word` is already in the dictionary:
    - If it is, it retrieves its current count.
    - If not, it returns `0`.
- The count of the `word` is then incremented by `1`.

**Example of `frequency` dictionary after execution:**

```python
{
 'peter': 4,
 'piper': 4,
 'picked': 4,
 'a': 3,
 'peck': 4,
 'of': 4,
 'pickled': 4,
 'peppers': 4,
 'if': 1,
 'where': 1,
 'is': 1,
 'the': 1
}
```

## 4. Collect words with counts larger than one

```python
# Collect words with counts larger than one
duplicate_words = [word for word in frequency if frequency[word] > 1]
```

- A list comprehension creates a new list `duplicate_words`.
- It includes all words from `freq` where the count is greater than `1`.
- These are the words that have duplicates in the text.

**Resulting `duplicate_words` List:**

```python
['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']
```

## 5. Sort the words alphabetically

```python
# Sort the words alphabetically
duplicate_words.sort()
```

- The `duplicate_words` list is sorted in alphabetical order using the `.sort()` method.
- Sorting enhances readability in the final output.

**Sorted `duplicate_words` list:**

```python
['a', 'of', 'peck', 'peppers', 'peter', 'picked', 'pickled', 'piper']
```

## 6. Print the header

```python
# Print the header
print(f"{'WORD':<12}{'COUNT':^9}")
```

- Prints the header of the output table.
- "WORD" and "COUNT" are the column titles.
- The spacing ensures alignment with the data that will be printed next.
- I decided to use what I learnt from the column formatting in Comp660

---

## 7. Print Each Word and Its Count

```python
# Print each word and its count
for word in duplicate_words:
  print(f"{word:<12}{frequency[word]:>5}")
```

- Iterates over each `word` in the `duplicate_words` list.
- `{frequency[word]}` outputs the count of the word from the `frequency` dictionary.
- Prints each word and its corresponding count on a new line.

## Complete output

When you run the code, the console displays:

```
WORD       COUNT
a            3
of           4
peck         4
peppers      4
peter        4
picked       4
pickled      4
piper        4
```

- Each word that appears more than once is listed with its count.
- The words are in alphabetical order.
- The counts reflect the number of times each word appears in the input text.
