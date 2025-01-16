"""This program has a function that takes string as parameter and returns 
reversed string which is a very simple form of encryption. """

# Define function to reverse string.
def text_encryption(text):
    # Removes all spaces from a given string.
    new_text = "".join(text.split())
    # Reverse the string using slicing.
    return new_text[::-1]

# Define function for user input.
def user_input():
    #Prompts user to enter a string and removes spaces from string.
    text = str(input("Enter the text message you want to encrypt: "))
    # Returns text removing spaces
    return(text)

# Main function
def main():
    text = user_input()
    encrypted_text=text_encryption(text)
    print (f"Encrypted text: {encrypted_text}")

# Run program
if __name__ == "__main__":
    main()