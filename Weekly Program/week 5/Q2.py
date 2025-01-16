"""This program when run from the command line, reports how many number of arguments were provided"""

import sys

def main():
    # Get the number of arguments provided to the program by deducting the program name.
    number_arguments = len(sys.argv) -1
    # Return the number of arguments
    return number_arguments

print(f"Number of arguments provided: {main()}")

# Call the main function to start the program
if __name__ == "__main__":
    main()

