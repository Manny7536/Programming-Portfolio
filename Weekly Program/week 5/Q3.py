"""This program that takes a bunch of command-line arguments, and then prints out the shortest argument."""

import sys

def main():
    # Check if there are no arguments provided.
    if len(sys.argv) < 2:
        print("Please provide one or more command-line arguments.")
        return

    # Get all arguments except the program name.
    arguments = sys.argv[1:]

    # Sort arguments by length
    sorted_arguments = sorted(arguments, key=len)

    # Print the shortest argument
    print(f"The shortest argument is: {sorted_arguments[0]}")

if __name__ == "__main__":
    main()