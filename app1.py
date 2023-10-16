# This code will check for the string "You've been hacked!" and, if found, append "This file is no good!" at the start of the file. 
# If the string is not found, it will display a message indicating that the file is safe, with no changes made.

# Prompt for the file location
file_location = input("Enter the path and filename of the text file to check: ")

try:
    # Open the file in read mode
    with open(file_location, 'r') as file:
        # Read the contents of the file into a variable
        file_contents = file.read()

        # Check if the file contains the string "You've been hacked!"
        if "You've been hacked!" in file_contents:
            # Print a message if the string is found
            print("The file has been hacked.")
            
            # Insert the string "This file is no good!" at the start of the file
            file_contents = "This file is no good!\n" + file_contents
            with open(file_location, 'w') as file:
                # Overwrite the file with the updated content
                file.write(file_contents)
        else:
            # Print a message if the string is not found
            print("The file is safe, and no changes were made.")

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File not found. Please check the file location.")
except Exception as e:
    # Handle other potential errors and display an error message
    print(f"An error occurred: {str(e)}")
