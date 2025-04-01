def read_and_modify_file(input_file, output_file, modification_function):
    """
    Reads content from input_file, applies modification_function, and writes to output_file
    """
    try:
        # Read from the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Apply the modification
        modified_content = modification_function(content)
        
        # Write to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"Successfully read from '{input_file}', modified content, and wrote to '{output_file}'")
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to access '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return False

def get_file_with_error_handling():
    """
    Asks the user for a filename and handles errors if it doesn't exist or can't be read
    """
    while True:
        filename = input("Enter the filename to read: ")
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"Successfully read file '{filename}'")
                print("Content:")
                print("-" * 40)
                print(content)
                print("-" * 40)
                return filename
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            retry = input("Would you like to try another file? (y/n): ")
            if retry.lower() != 'y':
                print("Exiting file reading operation.")
                return None
        
        except PermissionError:
            print(f"Error: You don't have permission to access '{filename}'.")
            retry = input("Would you like to try another file? (y/n): ")
            if retry.lower() != 'y':
                print("Exiting file reading operation.")
                return None
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            retry = input("Would you like to try another file? (y/n): ")
            if retry.lower() != 'y':
                print("Exiting file reading operation.")
                return None

# Example usage for Part 1: Read and write modified file
# For demonstration, let's create a sample file first
with open("sample.txt", "w") as sample_file:
    sample_file.write("Hello, master!\nThis is a sample file.\nPython file handling is fun with a coffee!")

# Define a modification function (convert to uppercase)
def to_uppercase(text):
    return text.upper()

# Read, modify, and write to a new file
read_and_modify_file("sample.txt", "modified_sample.txt", to_uppercase)

# Try with a non-existent file to demonstrate error handling
read_and_modify_file("nonexistent_file.txt", "output.txt", to_uppercase)

print("\n--- Part 2: Interactive File Reading with Error Handling ---")
print("Note: In this demo, we'll simulate the input. In a real program, it would wait for user input.")

# For demonstration purposes, we'll simulate the interactive part
# In a real scenario, this would use the get_file_with_error_handling() function
print("Simulating user entering 'nonexistent.txt':")
print("Enter the filename to read: nonexistent.txt")
print("Error: The file 'nonexistent.txt' was not found.")
print("Would you like to try another file? (y/n): y")

print("\nSimulating user entering 'sample.txt':")
print("Enter the filename to read: sample.txt")
print("Successfully read file 'sample.txt'")
print("Content:")
print("-" * 40)
with open("sample.txt", "r") as f:
    print(f.read())
print("-" * 40)