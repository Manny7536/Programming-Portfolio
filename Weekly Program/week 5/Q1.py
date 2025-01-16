"""This program uses the sys module to retrieve the platform information and when run
from the command-line prints what operating system platform is being used."""

import sys

def main():
    # Retrieve the platform information using sys module
    platform = sys.platform
    print(f"The operating system platform being used is: {platform}")

# Call the main function to start the program
if __name__ == "__main__":
    main()