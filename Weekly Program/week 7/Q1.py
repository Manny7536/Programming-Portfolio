"""This program has function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string"""

# Define a function to get unique letters from a string
def unique_character(user_text):
    # Converts the string to a set to remove duplicates, Sort the list of unique characters and returns it. 
    return sorted(list(set(user_text)))

# Test the function with a string
print(unique_character("cheese"))