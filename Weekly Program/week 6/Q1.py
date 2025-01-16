"""This program has a function that accepts a positive integer as a parameter and then 
returns a representation of that number in binary (base 2)"""

# Define a function to convert decimal to binary
def decimal_to_binary(decimal):
    # Check if the input is a positive integer
    if decimal == 0:
        # If the number is 0, return 0
        return "0"
    
    binary = ""
    # Loop until the number is 0
    while decimal > 0:
        # Append the remainder of the number divided by 2 to the binary string
        binary = str(decimal % 2) + binary
        # Update the number by dividing it by 2
        decimal = decimal // 2
    # Return the binary representation of the number
    return binary
    
# Define function to get user input
def get_user_input():
    while True:
        try:
            # Prompt user to enter a non-negative decimal number
            decimal = int(input("Enter a non-negative decimal number: "))
            if decimal >= 0:
                return decimal
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")

# Function to display result
def display_result(decimal):
    # Convert decimal to binary and display the result
    binary_representation = decimal_to_binary(decimal)
    print("The binary representation of the decimal number is:", binary_representation)

# Main program
def main():
    decimal_number = get_user_input()
    display_result(decimal_number)

# Run the program
if __name__ == "__main__":
    main()
