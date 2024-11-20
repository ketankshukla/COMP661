Strings and tuples are immutable data structures in Python.

### 1. **Strings**
- **Immutable:**  
  Strings in Python are immutable, meaning their contents cannot be altered after they are created. 
  Any operation that seems to modify a string actually creates a new string.
    - Example:
      ```python
      my_string = "hello"
      new_string = my_string.upper()  # Creates a new string
      print(my_string)  # Output: "hello"
      print(new_string)  # Output: "HELLO"
      ```

### 2. **Tuples**
- **Immutable:**  
  Tuples are immutable because their elements cannot be changed after the tuple is created. However, if a tuple contains mutable elements (like a list), the mutable elements can be altered, but the tuple structure itself remains unchanged.
    - Example:
      ```python
      my_tuple = (1, 2, 3)
      # my_tuple[0] = 99  # This would raise a TypeError
      print(my_tuple)  # Output: (1, 2, 3)
  
      my_tuple_with_list = ([1, 2], 3)
      my_tuple_with_list[0].append(99)  # Modify the list inside the tuple
      print(my_tuple_with_list)  # Output: ([1, 2, 99], 3)
      ```


Dictionaries and lists are mutable data structures in Python.

### 3. **Dictionaries**
- **Mutable:**  
  Dictionaries in Python are mutable because you can add, modify, or remove key-value pairs after the dictionary is created.
    - Example:
      ```python
      my_dict = {"key1": "value1"}
      my_dict["key2"] = "value2"  # Adds a new key-value pair
      print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}
      ```

### 4. **Lists**
- **Mutable:**  
  Lists are mutable because their elements can be changed in place, and items can be added or removed.
    - Example:
      ```python
      my_list = [1, 2, 3]
      my_list[0] = 99  # Modify an element
      print(my_list)  # Output: [99, 2, 3]
      my_list.append(4)  # Add an element
      print(my_list)  # Output: [99, 2, 3, 4]
      ```
