"""This program has a function  that takes a string parameter 
and returns it with the last character removed.
(If the string contains one or fewer characters, returns it unchanged.)"""

# Define function to remove last character of a string.
def remove_last_character(text):

    # Checks if the string has at least two characters.
    if len(text) <= 1:
        # Returns the string unchanged if it has one or fewer characters.
        return(text)
    else:
        # Returns the string with the last character removed.
        return text[:-1]

# Test the function with some examples.
def test():
    test_string = ["Hello", "I", "", "am", "Subash", "Shah","..."]
    for i in test_string:
        print(remove_last_character(i))

# Run program
if __name__ == "__main__":
    test()

    



