

def create_and_write_file():
    try:
        
        with open("my_file.txt", "w") as file:
            file.write("This is line 1: Hello, World!\n")
            file.write("This is line 2: The number is 42\n")
            file.write("This is line 3: Python file handling\n")
        print("File created and initial lines written.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File write operation complete.")

def read_file():
    try:
        
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nFile Contents:\n")
            print(content)
    except FileNotFoundError:
        print("File not found: Please ensure 'my_file.txt' exists.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    finally:
        print("File read operation complete.")

def append_to_file():
    try:
        
        with open("my_file.txt", "a") as file:
            file.write("This is line 4: Appending new content\n")
            file.write("This is line 5: Another number 100\n")
            file.write("This is line 6: End of file.\n")
        print("Additional lines appended.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File append operation complete.")


create_and_write_file()
read_file()
append_to_file()
read_file()  
