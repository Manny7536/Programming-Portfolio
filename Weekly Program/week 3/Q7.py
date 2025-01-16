"""This program prompts user for input.
Validates if user input is a number between 0 to 12 inclusive.
Displays "Times Table" for that number from 0 t0 12."""

# Infinite loop to keep prompting user until valid password is entered.
while True:
    try:
        # Prompt the user to enter a number.
        number = int(input("Enter a number between 0 and 12: "))

        # Check if the number is within the valid range.
        if (0 <= number <= 12):
            break
            
        else:
            # Inform the user if the number is out of range.
            print("Please enter a number between 0 and 12 inclusive.")
                 
    except ValueError:
        # Handle the error if the input is not a valid integer.
        print("Error: Invalid input. Please enter a number.")

# Loop to generate and display the "Times table".
for i in range(13):
    print(f"{i} * {number} = {i*number}")