"""This program has a function that takes an integer as its parameter and returns the
factors of that integer. There is also a test function with list of numbers."""

# Define a function to find factors of an integer.
def find_factors(number):
    
    # Initilize an empty list to store factors of an integer.
    factors = []

    # Iterate over all numbers from 1 to the given number (inclusive).
    for i in range(1, number + 1):
        # Check if i is a factor of the number
        if number % i == 0:
            # Add i to the list of factors
            factors.append(i)
    # Return the list of factors
    return factors

# Short program to test the function
def test_find_factors():
    test_numbers = [15, 28, 50, 1]
    for num in test_numbers:
        factors = find_factors(num)
        print(f"The factors of {num} are: {factors}")

# Run the test
test_find_factors()