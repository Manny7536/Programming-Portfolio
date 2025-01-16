"""This program prompts user to enter new password and re-enter new password again.
If both entered passwords matches, prints "Password Set"
Else prints error message."""

# Input for new password.
password = input("Enter new password: ")

# Input to confirm password.
confirm_password = input("Re-enter new password: ")

#Check if both password match
if password == "" and confirm_password == "":
    print("Error: Nothing was entered.")
elif password == confirm_password:
    print("Password Set.")
else:
    print("Error: Password do not match.")