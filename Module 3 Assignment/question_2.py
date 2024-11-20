# Input Text
input_text = (
    "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked "
    "if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked"
)

# Convert text to lowercase and split into words
words = input_text.lower().split()

# Count the frequency of each word
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Collect words with counts larger than one
duplicate_words = [word for word in frequency if frequency[word] > 1]

# Sort the words alphabetically
duplicate_words.sort()

# Print the header with proper formatting so the headers are aligned with their content
print(f"{'WORD':<12}{'COUNT':^9}")

# Print each word and its count and include formatting in the output
for word in duplicate_words:
    print(f"{word:<12}{frequency[word]:>5}")
