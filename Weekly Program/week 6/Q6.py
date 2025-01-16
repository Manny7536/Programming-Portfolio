"""This program has a function that accepts encrypted message as parameter and returns
decrypted message so human can understand it."""

# Function to decrypt a message
def decrypt_message(encrypted_message):
    # Extract the characters from the encrypted message at the specified interval
    decrypted_message = encrypted_message.replace("xy","")
    return decrypted_message

# Short program to test the function
def test_decrypt_message():
    encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
    decrypted_message = decrypt_message(encrypted_message)
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

# Run the test
test_decrypt_message()


