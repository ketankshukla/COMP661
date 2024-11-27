with open("file.txt", "r") as file:
    text = file.read()
    words = text.split()

    print("Analyzing all words:")
    for word in words:
        if len(word) == 5:
            print(f"'{word}' - Length: {len(word)} characters")
            print(f"  - Contains only letters? {word.isalpha()}")
            print(f"  - Contains numbers? {any(char.isdigit() for char in word)}")
            print(
                f"  - Contains punctuation? {any(not char.isalnum() for char in word)}"
            )
            print()

    # Two different counts for comparison
    five_letter_words = [word for word in words if len(word) == 5]
    five_letter_real_words = [
        word for word in words if len(word) == 5 and word.isalpha()
    ]

    print(f"Number of 5-character sequences: {len(five_letter_words)}")
    print(
        f"Number of true 5-letter words (letters only): {len(five_letter_real_words)}"
    )
