# """This program prompts user for six different temperature in celcius.
# It has a function that converts celcius to fahrenheit.
# Displays max, min and mean from 6 different fahrenheit as a result."""

from statistics import mean

# Define function to prompt user to enter temperature in Celsius
def user_input():
    temperatures = []
    for i in range(6):
        while True:
            # Prompt user to enter temperature in Celsius
            temperature = input(f"Enter temperature {i + 1} in Celsius (e.g., 32C): ").upper()
            if temperature.endswith('C'):
                try:
                    # Validates the numeric part.
                    float(temperature[:-1])
                    # Append the temperature to the list including 'C'.
                    temperatures.append(temperature)
                    break
                except ValueError:
                    # If the number part is not valid, prompt the user to enter again
                    print("Invalid input. Please enter a valid number followed by 'C'.")
            else:
                # If input does not end with 'C', prompt user to enter again
                print("Invalid input. Please enter the temperature in the correct format (e.g., 25C).")
    return temperatures

# Define function to convert celcius to farenheit
def celcius_to_fahrenheit(temperature):
    # Remove 'C' from the input and convert to float
    temperature = float(temperature[:-1])
    # Convert celcius to farenheit using formula.
    fahrenheit = (temperature*9/5)+32
    # Returns the equivalent temperature in fahrenheit 
    return fahrenheit

# Main program
def main():
    temperatures = user_input()
    fahrenheit_temperatures = [celcius_to_fahrenheit(i) for i in temperatures]
    print(f"Temperatures in Fahrenheit: {fahrenheit_temperatures}")
    # Calculate and display maxmium, minimum and mean of the fahrenheit temperatures using built in-function.
    maxmimum_temperature = max(fahrenheit_temperatures)
    minimum_temperature = min(fahrenheit_temperatures)
    mean_temperature = mean(fahrenheit_temperatures)
    print(f"Maximum temperature: {maxmimum_temperature}F")
    print(f"Minimum temperature: {minimum_temperature}F")
    print(f"Mean temperature: {mean_temperature}F")

# Run program
if __name__ == "__main__":
    main()
