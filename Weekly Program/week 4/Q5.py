"""This program has two functions that converts temperature measured in degrees
centigrade into the equivalent in fahrenheit and vice-versa."""

# Define a function to convert celcius to fahrenheit
def celcius_to_fahrenheit(celcius):
    # Returns the equivalent temperature in fahrenheit
    return (celcius * 9/5) + 32

# Define a function to convert fahrenheit to centigrade
def fahrenheit_to_celcius(fahrenheit):
    # Returns the equivalent temperature in celcius
    return (fahrenheit - 32) * 5/9

#Program to check both function.
print("Converts celcius to fahrenheit.")
temperature_in_celcius = [0,38.5,-2,]
for i in temperature_in_celcius:
    print(f"{i}°C is equal to {celcius_to_fahrenheit(i)}°F")

print("Converts fahrenheit to celcius.")
temperature_in_fahrenheit = [32,101.3,28.4]
for i in temperature_in_fahrenheit:
    print(f"{i}°F is equal to {fahrenheit_to_celcius(i):.2f}°C")


