import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"


def read_items():
    items = []
    try:
        with open(ITEMS_FILENAME) as file:
            for line in file:
                line = line.strip()
                items.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{ITEMS_FILENAME}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading items: {e}")
    return items


def read_inventory():
    inventory = []
    try:
        with open(INVENTORY_FILENAME) as file:
            for line in file:
                line = line.strip()
                inventory.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{INVENTORY_FILENAME}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading inventory: {e}")
    return inventory


def write_inventory(inventory):
    try:
        with open(INVENTORY_FILENAME, "w") as file:
            for item in inventory:
                file.write(item + "\n")
    except Exception as e:
        print(f"An error occurred while writing inventory: {e}")


def display_title():
    print("The Wizard Inventory program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()


def walk(inventory):
    items = read_items()
    if not items:
        print("No items available to find. Check your items file.")
        return
    try:
        item = random.choice(items)
        print("While walking down a path, you see " + item + ".")
        choice = input("Do you want to grab it? (y/n): ")
        if choice.lower() == "y":
            if len(inventory) >= 4:
                print("You can't carry any more items. Drop something first.\n")
            else:
                inventory.append(item)
                print("You picked up " + item + ".\n")
                write_inventory(inventory)
    except Exception as e:
        print(f"An error occurred during the walk: {e}")


def show(inventory):
    if not inventory:
        print("Your inventory is empty.\n")
        return
    try:
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
        print()
    except Exception as e:
        print(f"An error occurred while showing the inventory: {e}")


def drop_item(inventory):
    try:
        number = int(input("Number: "))
        if number < 1 or number > len(inventory):
            print("Invalid item number.\n")
        else:
            item = inventory.pop(number - 1)
            print("You dropped " + item + ".\n")
            write_inventory(inventory)
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    except Exception as e:
        print(f"An error occurred while dropping the item: {e}")


def main():
    try:
        display_title()
        display_menu()
        inventory = read_inventory()
        while True:
            command = input("Command: ").strip().lower()
            if command == "walk":
                walk(inventory)
            elif command == "show":
                show(inventory)
            elif command == "drop":
                drop_item(inventory)
            elif command == "exit":
                break
            else:
                print("Not a valid command. Please try again.\n")
        print("Bye!")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
