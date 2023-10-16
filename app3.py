# This code checks for the string "You've been hacked!" and, if found, moves the file into a subfolder named "Quarantine" located in the same directory as the original file.
# If the string is not found, it will indicate that the file is safe, with no changes made.

import os

# Prompt for the file location
file_location = input("Enter the path to the text file: ")

try:
    # Open the file in read mode
    with open(file_location, 'r') as file:
        # Read the contents of the file into a variable
        file_contents = file.read()

    # Check if the file contains the string "You've been hacked!"
    if "You've been hacked!" in file_contents:
        # Close the file before moving it
        file.close()

        # Print a message if the string is found
        print("The file has been hacked.")

        # Define the path to the "Quarantine" subfolder
        quarantine_folder = os.path.join(os.path.dirname(file_location), "Quarantine")

        # Create the "Quarantine" subfolder if it doesn't exist
        if not os.path.exists(quarantine_folder):
            os.mkdir(quarantine_folder)

        # Get the file's base name (without the path)
        file_name = os.path.basename(file_location)

        # Define the new path for the file in the "Quarantine" subfolder
        new_file_path = os.path.join(quarantine_folder, file_name)

        # Move the file to the "Quarantine" subfolder
        os.rename(file_location, new_file_path)

    else:
        # Print a message if the string is not found
        print("The file is safe, and no changes were made.")

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File not found. Please check the file location.")
except Exception as e:
    # Handle other potential errors and display an error message
    print(f"An error occurred: {str(e)}")
