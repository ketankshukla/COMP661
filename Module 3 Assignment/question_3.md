The following are three unique real-world examples of objects that can be stored in a Python dictionary.

These examples illustrate how dictionaries can map unique identifiers (keys) to associated data (values),
making data retrieval efficient and intuitive in real-world applications.

1. **Phone directory:**
    - **Key:** Person's name (e.g., `"Alice Johnson"`)
    - **Value:** Phone number (e.g., `"+1-555-1234"`)

   ```python
   phone_directory = {
       "Alice Johnson": "+1-555-1234",
       "Bob Smith": "+1-555-5678",
       "Charlie Brown": "+1-555-8765"
   }
   ```

2. **Language translation:**
    - **Key:** Word in english (e.g., `"hello"`)
    - **Value:** Translation in another language (e.g., `"hola"` in Spanish)

   ```python
   english_to_spanish = {
       "hello": "hola",
       "goodbye": "adios",
       "please": "por favor",
       "thank you": "gracias"
   }
   ```

3. **Product inventory system:**
    - **Key:** Product ID or SKU (e.g., `"SKU1001"`)
    - **Value:** Product details (e.g., `{ "name": "Wireless Mouse", "price": 29.99, "stock": 150 }`)

   ```python
   inventory = {
       "SKU1001": { "name": "Wireless Mouse", "price": 29.99, "stock": 150 },
       "SKU1002": { "name": "Bluetooth Keyboard", "price": 49.99, "stock": 85 },
       "SKU1003": { "name": "HD Monitor", "price": 199.99, "stock": 40 }
   }
   ```