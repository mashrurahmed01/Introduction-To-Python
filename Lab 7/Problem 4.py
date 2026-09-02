import os

file_path = "sample.txt"

try:

    try:
        with open(file_path, "x") as file:
            file.write("Hello Python\n")
        print("File created successfully")

    except FileExistsError:
        print("File already exists")

    with open(file_path, "w") as file:
        file.write("This is the first line.\n")
        file.write("This file is created using Python.\n")
    print("File written successfully")

    with open(file_path, "r") as file:
        data = file.read()
    print("\nFile contents:")
    print(data)

    with open(file_path, "a") as file:
        file.write("This line was appended.\n")
    print("Content appended successfully")

    with open(file_path, "r") as file:
        data = file.read()
    print("\nUpdated file contents:")
    print(data)

except Exception as e:
    print("An unexpected error occurred:", e)