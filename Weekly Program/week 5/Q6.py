"""This program takes the name of a file as a command-line argument, and
creates a backup copy of that file renaming it."""

import sys
import shutil

def main():
    # checks if the user has provided the required arguments.
    if len(sys.argv) != 2:
        # if not, prints the usage and exits.
        print("Usage: python backup_file.py <file_path>")
        return
    # gets the file name from the user and store on variable.
    original_file_path = sys.argv[1]

    # Stores file name in backup variable adding .backup
    backup_file_path = + "backup-" + original_file_path 

    try:
        # Try to copy the file to the backup location
        shutil.copyfile(original_file_path, backup_file_path)

        # If the copy is successful, prints a success message.
        print(f"Backup created successfully: {backup_file_path}")
    except FileNotFoundError:
        # If the file does not exist, prints an error message.
        print(f"Error: The file '{original_file_path}' was not found.")
    except Exception as e:
        # If any other error occurs, prints the error message.
        print(f"An error occurred: {e}")

# Call the main function
if __name__ == "__main__":
    main()