# Phone Directory
phone_directory = {
    "Alice Johnson": "+1-555-1234",
    "Bob Smith": "+1-555-5678",
    "Charlie Brown": "+1-555-8765",
}

# Language Translation Glossary
english_to_spanish = {
    "hello": "hola",
    "goodbye": "adios",
    "please": "por favor",
    "thank you": "gracias",
}

# Product Inventory System
inventory = {
    "SKU1001": {"name": "Wireless Mouse", "price": 29.99, "stock": 150},
    "SKU1002": {"name": "Bluetooth Keyboard", "price": 49.99, "stock": 85},
    "SKU1003": {"name": "HD Monitor", "price": 199.99, "stock": 40},
}

# Print all dictionaries
print("Phone Directory:")
for name, phone in phone_directory.items():
    print(f"{name}: {phone}")

print("\nEnglish to Spanish Translation Glossary:")
for english_word, spanish_word in english_to_spanish.items():
    print(f"{english_word} -> {spanish_word}")

print("\nProduct Inventory:")
for sku, details in inventory.items():
    print(
        f"{sku}: Name: {details['name']}, Price: ${details['price']:.2f}, Stock: {details['stock']}"
    )
