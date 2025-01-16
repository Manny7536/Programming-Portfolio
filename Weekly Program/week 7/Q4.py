"""This program has a function that takes a message string as a parameter,
and returns the count of six most common letters of that message."""

from collections import Counter


def frequency_analysis(message):
    # Convert the message to lower case to ignore case sensitivity
    message = message.lower()
    
    # Filter out non-alphabet characters
    filtered_message = ''.join(filter(str.isalpha, message))
    
    # Count the frequency of each letter
    letter_counts = Counter(filtered_message)
    
    # Get the six most common letters
    most_common_letters = letter_counts.most_common(6)    
    return most_common_letters

# Test the function
def test_frequency_analysis():
    message = "I like programming and I love coding in python."
    result = frequency_analysis(message)
    for letter, count in result:
        print(f"Letter: '{letter}', Count: {count}")

# Run the test
test_frequency_analysis()