"""This program prompts user for input.
Validates if user input is a number less 12 inclusive.
If user input is negative number "Times Table" is printed for that number from 12 to 0.
Otherwise displays "Times Table" for that number from 0 t0 12."""

# Infinite loop to keep prompting user until valid password is entered.
while True:
    try:
        # Prompt the user to enter a number.
        number = int(input("Enter a number that is less than or equal to 12: "))

        # Check if the number is within the valid range.
        if (number <= 12) :
            break
            
        else:
            # Inform the user if the number is out of range.
            print("Please enter a number less than or equal to 12.")
                 
    except ValueError:
        # Handle the error if the input is not a valid integer.
        print("Error: Invalid input. Please enter a number.")

# Checks if user input is positive number.
if number >= 0:
    # Loop to display "Times table" for positive number.
    for i in range(13):
        print(f"{i} * {number} = {i*number}")
        
else:
    # Loop to display "Times table" for negative number.
    for j in range(12,-1,-1):
        print(f"{j} * {number} = {j*number}")