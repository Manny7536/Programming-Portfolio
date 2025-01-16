"""This program prompts user to enter temperature in celcius,
It has a function that converts the temperature in celcius to farenheit.
Displays the farenheit temperature as a result."""

#  Define function to prompt user to enter temperature in celcius.
def user_input():
    while True:
        # Prompt user to enter temperature in celcius
        temperature = input("Enter temperature in celcius example(32C): ").upper()
        try:
            # Check if the input is a number and ends with letter 'C'
            if temperature.endswith('C'):
                # Convert the input to float and return it
                float(temperature[:-1])
                # Returns user input temperature.
                return temperature
            else:
                # If input is not a number or does not end with 'C', prompt user to enter again
                print("Ivalid input. Please enter the temperature in the correct format (e.g., 25C)")
        except ValueError:
            # If input is not a number, prompt user to enter again
            print("Invalid input. Please enter a valid number")

# Define function to convert celcius to farenheit
def celcius_to_fahrenheit(temperature):
    # Remove 'C' from the input and convert to float
    temperature = float(temperature[:-1])
    # Convert celcius to farenheit using formula.
    fahrenheit = (temperature*9/5)+32
    # Returns the equivalent temperature in fahrenheit 
    return fahrenheit

# Define function to display result
def display_result(temperature,fahrenheit):
    # Display the farenheit temperature as a result
    print(f"{temperature} celcius is equal to {fahrenheit:.2f}F")

# Main program.
def main():
    temperature = user_input()
    fahrenheit = celcius_to_fahrenheit(temperature)
    display_result(temperature,fahrenheit)

# Run program
if __name__ == "__main__":
    main()