import random

# Generate 10 random letters
random_letters = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)]
print("Original list:", random_letters)

# a. Sort in ascending order
ascending_order = sorted(random_letters)
print("Ascending order:", ascending_order)

# b. Sort in descending order
descending_order = sorted(random_letters, reverse=True)
print("Descending order:", descending_order)

# c. Unique values in ascending order
unique_sorted = sorted(set(random_letters))
print("Unique values sorted:", unique_sorted)
