"""This program has a function that takes a message parameter and returns encrypted message and interval of 
characters in message."""

import random
import string

# Function to encrypt a message
def encrypt_message(message):
    # Randomly generate an interval between 2 and 20
    interval = random.randint(2, 20)

    # Create a list to store the encrypted message
    encrypted_message = []

    # Iterate over each character in the message
    for i, char in enumerate(message):
        # Add random characters to the encrypted message
        for _ in range(interval - 1):
            encrypted_message.append(random.choice(string.ascii_letters))
        # Add the message character
        encrypted_message.append(char)

    # Join the list into a single string
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

# Short program to test the function
def test_encrypt_message():
    
    test_message = input("Enter a message to encrypt: ")
    encrypted_message, interval = encrypt_message(test_message)
    print(f"Original message: {test_message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Interval used: {interval}")

# Run the test
test_encrypt_message()