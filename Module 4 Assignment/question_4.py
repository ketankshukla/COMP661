import os

filename = input("Enter the filename: ")
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("File contents:")
        print(file.read())
else:
    print("Error: File does not exist.")
