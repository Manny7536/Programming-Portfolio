"""This program has a function that returns True, if a given integer is a prime number,
and False otherwise. There is also a test function that tests the function with a list of numbers."""

# Define a function to check if a number is prime.
def is_prime(number):
    count = 0
    # Loop to iterate from 2 to the number (inclusive)
    for i in range(2,number+1):

        # If number is divisible by i, increment count
        if number % i == 0:
            count+=1

    # Prime numbers are greater than 1
    if number <= 1:
        return False
    
    # If count is 1, it means number has no divisors other than 1 and itself.
    if count == 1:
        return True
    else:
        return False
    
# Function to test the is_prime function with various numbers      
def test_is_prime():
    test_numbers = [2, 3, 4, 17, 20, 23, 29, 35]
    for num in test_numbers:
        result = is_prime(num)
        print(f"Is {num} a prime number? {result}")

# Run the test
test_is_prime()