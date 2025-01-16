""" This program prompts a user to enter a temperature in celcius.
Calculates the temperature in Fahrenheit 
and displays corresponding temperature in Fahrenheit to the user. """

# Takes user input for temperature in Celsius.
temperature_celcius = float(input("Enter a temperature in Celsius: "))

# Calculates temperature in Fahrenheit using the formula (°C × 9/5) + 32 = °
temperature_fahrenheit = float((temperature_celcius * 9/5) + 32)

# Displays the calculated temperature in Fahrenheit to the user.
print(f"{temperature_celcius}°C is equivalent to {temperature_fahrenheit}°F.")