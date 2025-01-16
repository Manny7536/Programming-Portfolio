""" This program prompts user for name as an input.
If user enters a name, it will print out a greeting message with the name.
Or prints "Hello, Stranger!", instead of name. """

# Input name from the user.
name = input("Hello, what is your name? ")

# Checks for user input name.
if name:
    # Displays a greeting message with the user's name.
    print(f"Hello, {name}. Good to meet you !")
    
else:
    # If the name is empty, print out " Hello , Stranger!".
    print("Hello, Stranger!")