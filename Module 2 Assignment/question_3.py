def display_menu():
    print("\nCOMMAND MENU")
    print("list    - Display all contacts")
    print("view    - View a contact")
    print("add     - Add a contact")
    print("del     - Delete a contact")
    print("exit    - Exit program")


def list_contacts(contacts):
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. {contact[0]}")


def view_contact(contacts):
    number = int(input("Number: "))
    if 1 <= number <= len(contacts):
        contact = contacts[number - 1]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Phone: {contact[2]}")
    else:
        print("Invalid contact number")


def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    print(f"{name} was added.")


def delete_contact(contacts):
    number = int(input("Number: "))
    if 1 <= number <= len(contacts):
        contact = contacts.pop(number - 1)
        print(f"{contact[0]} was deleted.")
    else:
        print("Invalid contact number")


def main():
    print("Contact Manager")

    # Initial contacts data
    contacts = [
        ["Marilyn Monroe", "MarilynMonroe@hollywood.com", "+11 22 3333 4444"],
        ["Abraham Lincoln", "AbrahamLincoln@whitehouse.org", "+22 33 4567 4587"],
    ]

    while True:
        display_menu()
        command = input("\nCommand: ").lower()

        if command == "list":
            list_contacts(contacts)
        elif command == "view":
            view_contact(contacts)
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            delete_contact(contacts)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
