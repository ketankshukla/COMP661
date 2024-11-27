import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    clear_screen()
    print("=" * 50)
    print("           File Name Replacement Tool")
    print("=" * 50)
    print()


def wait_for_file_access(filename, timeout=5):
    """Wait until a file is accessible or timeout is reached"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Try to open the file in append mode
            with open(filename, "a"):
                return True
        except:
            time.sleep(0.1)  # Wait 100ms before trying again
    return False


def cleanup_temp_files():
    """Clean up any temporary files that might be left over"""
    if os.path.exists("tempfile.txt"):
        try:
            os.remove("tempfile.txt")
        except:
            pass


def reset_files():
    # Original content for creating accounts.txt if needed
    original_content = """100 Mary 34.58
200 Alison 345.67
300 Marc 3.00
400 Zoltar -32.16
500 Kathleen 24.32"""

    # Delete myaccounts.txt if it exists
    if os.path.exists("myaccounts.txt"):
        try:
            os.remove("myaccounts.txt")
            time.sleep(0.1)  # Wait a bit after deletion
            print(" Removed myaccounts.txt")
        except Exception as e:
            print(f"Error removing myaccounts.txt: {e}")

    # Only create accounts.txt if it doesn't exist
    if not os.path.exists("accounts.txt"):
        try:
            with open("accounts.txt", "w") as file:
                file.write(original_content)
            print(" Created accounts.txt file with original content")
        except Exception as e:
            print(f"Error creating accounts.txt: {e}")
    else:
        print(" Original accounts.txt file is already in place")
        print("\nCurrent content of accounts.txt:")
        print("-" * 25)
        try:
            with open("accounts.txt", "r") as file:
                print(file.read())
            print("-" * 25)
        except Exception as e:
            print(f"Error reading accounts.txt: {e}")


def replace_name():
    cleanup_temp_files()  # Clean up any leftover temp files

    try:
        # Step 1: Create temp file with replacements
        print(" Reading from accounts.txt")
        with open("accounts.txt", "r") as infile:
            content = infile.read()

        with open("tempfile.txt", "w") as tempfile:
            tempfile.write(content.replace("Zoltar", "Robert"))
        print(" Created temporary file with replacements")
        time.sleep(0.1)  # Wait a bit after writing

        # Step 2: Remove existing files
        if os.path.exists("myaccounts.txt"):
            os.remove("myaccounts.txt")
            time.sleep(0.1)  # Wait after deletion
            print(" Removed existing myaccounts.txt")

        if os.path.exists("accounts.txt"):
            os.remove("accounts.txt")
            time.sleep(0.1)  # Wait after deletion
            print(" Removed original accounts.txt")

        # Step 3: Rename temp file
        if wait_for_file_access("tempfile.txt"):
            os.rename("tempfile.txt", "myaccounts.txt")
            print(" Renamed temporary file to myaccounts.txt")
            print(" Temporary file deleted")
            print(" Name replacement complete")

            # Display the contents of the new file
            print("\nContents of myaccounts.txt:")
            print("-" * 25)
            with open("myaccounts.txt", "r") as file:
                print(file.read())
            print("-" * 25)
        else:
            print("Error: Could not access temporary file")

    except Exception as e:
        print(f"Error during replacement: {e}")
        # Clean up temp file if it exists
        if os.path.exists("tempfile.txt"):
            try:
                os.remove("tempfile.txt")
                print(" Cleaned up temporary file")
            except:
                pass


def display_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"\nContents of {filename}:")
        print("-" * 40)
        print(content)
        print("-" * 40)
    except FileNotFoundError:
        print(f"\nFile {filename} does not exist.")
    except Exception as e:
        print(f"\nError reading {filename}: {e}")


def main():
    while True:
        print_header()
        print("Options:")
        print("1. Replace 'Zoltar' with 'Robert'")
        print("2. Display current files")
        print("3. Reset to original state")
        print("4. Exit")
        print()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            replace_name()
        elif choice == "2":
            display_file_content("accounts.txt")
            display_file_content("myaccounts.txt")
        elif choice == "3":
            reset_files()
        elif choice == "4":
            cleanup_temp_files()  # Clean up before exiting
            # Clean up temp file if it exists
            if os.path.exists("tempfile.txt"):
                try:
                    os.remove("tempfile.txt")
                except:
                    pass
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
