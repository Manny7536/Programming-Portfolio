"""This program has three functions that takes two word strings as parameters
First function returns sorted list of letters that appear in at least one of the two words.
Second function returns a sorted list of letters that appear in both words.
Third function returns a sorted list of letters that appear in the first word but not in the second word."""


# Define function to return letters that appear in at least one of the two words
def letters_in_at_least_one(word1, word2):
    # Convert the words to sets to remove duplicates, perform union operation, and then convert to sorted.
    return sorted(list(set(word1) | set(word2)))

# Define function to return letters that appear in both words
def letters_in_both(word1, word2):
    # Convert the words to sets to remove duplicates, perform intersection operation,
    # and then convert back to sorted list
    return sorted(list(set(word1) & set(word2)))

# Define function to return letters that appear in either word, but not in both
def letters_in_either_but_not_both(word1, word2):
    # Convert the words to sets to remove duplicates, perform symmetric difference operation, 
    # and then convert back to sorted list
    return sorted(list(set(word1) ^ set(word2)))

# Test the functions
word1 = "Computer"
word2 = "Programming"
print("Letters in at least one of the words:", letters_in_at_least_one(word1, word2))
print("Letters in both words:", letters_in_both(word1, word2))
print("Letters in either word, but not in both:", letters_in_either_but_not_both(word1, word2))