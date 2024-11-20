## Contact Manager Program Guide

This Python program implements a command-line contact management system with various functions to handle contact information.

## Core Functions

**Menu Display Function**
```python
def display_menu():
    print("\nCOMMAND MENU")
    print("list    - Display all contacts")
    print("view    - View a contact")
    print("add     - Add a contact")
    print("del     - Delete a contact")
    print("exit    - Exit program")
```
Displays available commands for user interaction.

**Contact Listing Function**
```python
def list_contacts(contacts):
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. {contact[0]}")
```
- Uses enumerate to display numbered contacts
- Shows only contact names
- Starts numbering from 1 instead of 0

**Contact Viewing Function**
```python
def view_contact(contacts):
    number = int(input("Number: "))
    if 1 <= number <= len(contacts):
        contact = contacts[number-1]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Phone: {contact[2]}")
    else:
        print("Invalid contact number")
```
- Takes user input for contact number
- Validates input range
- Displays full contact details if valid

**Contact Addition Function**
```python
def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    print(f"{name} was added.")
```
- Collects contact information
- Adds new contact to list
- Confirms addition with message

**Contact Deletion Function**
```python
def delete_contact(contacts):
    number = int(input("Number: "))
    if 1 <= number <= len(contacts):
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.")
    else:
        print("Invalid contact number")
```
- Removes contact by number
- Validates input range
- Confirms deletion with message

## Main Program Structure

**Initial Setup**
```python
contacts = [
    ["Marilyn Monroe", "MarilynMonroe@hollywood.com", "+11 22 3333 4444"],
    ["Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"]
]
```
- Initializes with two default contacts
- Uses nested list structure
- Stores name, email, and phone for each contact

**Main Loop**
```python
while True:
    display_menu()
    command = input("\nCommand: ").lower()
    # Command processing
```
- Continuously runs until exit
- Processes user commands
- Converts input to lowercase

## Program Features

- Command-line interface
- Data persistence during runtime
- Input validation
- Error handling
- Case-insensitive commands
- Formatted output display

## Data Structure
Each contact is stored as a list within the main contacts list:
- Index 0: Name
- Index 1: Email
- Index 2: Phone number