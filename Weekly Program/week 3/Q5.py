"""This program prompts user to enter new password.
Validates that the password entered is between 8 and 12 characters long.
Ensure the chosen password in not in the list of common password.
Prompts user again to confirm the password.
Displays "Password set." if the password match.
otherwise an error is displayed and Program continues again in loop.
"""

bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Infinite loop to keep prompting user until valid password is entered.
while True:
    # Prompt user to enter new password.
    password =  input("Enter new password (8-12 characters): ")

    # Validate password length.
    if not (8 <= len(password) <= 12):
        print("Error: Password must be between 8 and 12 characters. Try again.")
        continue
    # Check if password is in list of bad_passwords.
    if password in bad_passwords:
        print("Error: Password is too common. Choose a more secure password.")
        continue

    # Prompt user to confirm password.
    confirm_password = input("Re-enter new password: ")

    # Validate that passwords match.
    if password == confirm_password:
        print("Password Set.")
        break
    
    else:
        print("Error: Password do not match. Try again.")
    