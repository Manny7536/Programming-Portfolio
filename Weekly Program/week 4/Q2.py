"""This program has a function that takes a single string as its parameter, 
and returns the number of uppercase letters, and the number of lowercase letters
 in the string and a short program to test the function."""

# Function to count uppercase and lowercase letters in a string
def count_letters(text):
    # Count the number of uppercase letters using list comprehension and the isupper method.
    uppercase_count = sum(1 for i in text if i.isupper())

    # Count the number of uppercase letters using list comprehension and the isupper method.
    lowercase_count = sum(1 for i in text if i.islower())

    # Returns the count as tupple (uppercase_count, lowercase_count)
    return uppercase_count, lowercase_count

def test():
    # Short program to test the function
    text = "Hello, My name is Subash Shah."
    uppercase, lowercase = count_letters(text)
    print(f"Test string: '{text}'")
    print(f"Number of uppercase letters: {uppercase}")
    print(f"Number of lowercase letters: {lowercase}")

# Run the program.
if __name__ == "__main__":
    test()  