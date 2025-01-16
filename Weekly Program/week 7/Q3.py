"""This program prompts user to input a country name. If the program already "knows"
the name of the capital city, it displays it. Otherwise it asks the user to
enter it and adds to dict infinetly. if user enters exits the program terminates. """

# Define a dictionary to store country-capital pairs
countries_capitals = {}

# Define a flag to track whether the user wants to exit the program
while True:
    # Prompt the user to enter the name of a country or 'exit' to terminate the program
    country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()

    if country == 'exit':
        print("Exiting the program. Goodbye!")
        break

    # Convert the first letter of each word in the country name to uppercase
    country = country.title()

    if country in countries_capitals:
        # If the country is already known, display its capital
        print(f"The capital city of {country} is {countries_capitals[country]}.")
    else:
        # If the country is unknown, ask the user for its capital
        capital = input(f"I don't know the capital city of {country}. Please enter it: ").strip()
        # Store the capital city in the dictionary
        countries_capitals[country] = capital
        print(f"Thank you! The capital city of {country} has been added as {capital}.")