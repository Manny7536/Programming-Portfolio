"""This program prompts user to enter new password.
Validates the condition that the password entered is between 8 and 12 characters long.
Prompts user again to confirm the password.
If the password matches, "Password set" is displayed otherwise an error is displayed.
"""

# Infinite loop to keep prompting user until valid password is entered.
while True:
    # Prompt user to enter new password.
    password =  input("Enter new password (8-12 characters): ")

    # Validate password length.
    if not (8 <= len(password) <= 12):
        print("Error: Password must be between 8 and 12 characters. Try again.")
        continue

    # Prompt user to confirm password.
    confirm_password = input("Re-enter new password: ")

    # Check if passwords match.
    if password == confirm_password:
        print("Password Set.")
    
    else:
        print("Error: Password do not match.")
    break