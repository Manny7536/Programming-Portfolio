"""This program takes values from the command line and converts temperature readings 
from Celsius to Fahrenheit 
and calculates the maximum, minimum, and mean temperatures and displays the result."""

import sys
from statistics import mean

# Define function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temperature):
    # Remove 'C' from the input and convert to float
    temperature = float(temperature[:-1])
    # Convert Celsius to Fahrenheit using formula
    fahrenheit = (temperature * 9 / 5) + 32
    # Returns the equivalent temperature in Fahrenheit
    return fahrenheit

# Main program
def main():
    # Check if the user provided temperature readings as command-line arguments
    if len(sys.argv) < 2:
        # If not, print usage message and exit
        print("Please provide temperature readings in Celsius as command-line arguments (e.g., 25C 32C).")
        return
    # Get the temperature readings from the command-line arguments
    temperatures = sys.argv[1:]

    # List to store the converted temperatures in Fahrenheit
    fahrenheit_temperatures = []

    # Iterate over the temperature readings
    for temp in temperatures:
        # Check if the temperature reading ends with 'C'
        if temp.endswith('C'):
            try:
                # Validate and convert the temperature
                fahrenheit_temperatures.append(celsius_to_fahrenheit(temp))
            except ValueError:
                # Handle invalid temperature format
                print(f"Invalid temperature format: {temp}. Please provide a valid number followed by 'C'.")
                return
        else:
            # Handle invalid temperature format
            print(f"Invalid temperature format: {temp}. Please provide a valid number followed by 'C'.")
            return
    # Print the converted temperatures
    print(f"Temperatures in Fahrenheit: {fahrenheit_temperatures}")

    # Calculate and print the maximum, minimum, and mean temperatures
    max_temperature = max(fahrenheit_temperatures)
    min_temperature = min(fahrenheit_temperatures)
    mean_temperature = mean(fahrenheit_temperatures)

    # Print the calculated values
    print(f"Maximum temperature: {max_temperature}F")
    print(f"Minimum temperature: {min_temperature}F")
    print(f"Mean temperature: {mean_temperature}F")

# Run program
if __name__ == "__main__":
    main()