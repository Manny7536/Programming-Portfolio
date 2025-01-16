""" This program has a functions that prompts user for name as an input.
If user enters a name, it will print out a greeting message with the name.
Or prints "Hello, Stranger!", instead of name in formatted way. """

# Define function for user_input.
def user_input():
    # Prompt user for name as an input.
    name = input("Hello, what is your name? ")
    # Returns user input name.
    return name

def capitalize_name(user_name):
    formatted_name = user_name.capitalize()
    return formatted_name

# Define function to greet user.         
def greet_user(formatted_name):
    
    # Checks if the user input name.
    if formatted_name:
        # Displays a greeting message with the user's name.
        print(f"Hello, {formatted_name}. Good to meet you!")
        
    else:
        # If the name is empty, prints out " Hello , Stranger!".
        print("Hello, Stranger!")

# Main program
def main():
    name = capitalize_name(user_input())
    greet_user(name)
    
#Run the program
if __name__ == "__main__":
    main()