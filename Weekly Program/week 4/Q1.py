"""This program has a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise."""

# Function to validate if a number is within the range of 0 to 100.
def validate_integer (number):
    # Returns True if the number ib between 0 to 100 inclusive, otherwise False.
    return 0 <= number <= 100

def test():
    # List of test numbers to validate. 
    test_number = [1,0,-20,89,100,101,-9999]

    #Loop through each number in the test_number list.
    for number in test_number:
        # Calls the validate integer function to checkif the number is within the range.
        result = validate_integer(number)

        # Prints the result (True or False) along with number.
        print(f"{number} : {result}")

if __name__ == "__main__":
    # Call the test function when the script is run directly.
    test()




