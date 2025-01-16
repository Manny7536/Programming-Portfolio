import sys
import os
from collections import defaultdict
from statistics import mean
from tabulate import tabulate
import matplotlib.pyplot as plt

def read_driver_info(file_path):

    """This function reads drivers info from file and returns a dictionary for drivers info."""

    # Initialize a dictionary to store drivers info
    driver_info = {}
    # Read from file.
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into driver id and info
            parts = line.strip().split(',')
            # Store the driver info in the dictionary accrodingly.
            driver_info[parts[1]] = {
                'number': parts[0],
                'name': parts[2],
                'team': parts[3]
            }
    # Return the dictionary of drivers info
    return driver_info

def read_lap_times(file_path):

    """This function reads lap times from file and returns a dictionary for lap times."""

    # Read from file
    with open(file_path, 'r') as file:
        # Read each line in the file
        lines = file.readlines()
    # Initialize a variable to store race location.
    location = lines[0]
    # Initialize a dictionary to store lap times.
    lap_times = defaultdict(list)
    # Read each line in the file excluding the first line.
    for line in lines[1:]:
        # Split the line into driver id and lap time.
        driver_code = line[:3]
        # Store the lap times infloat.
        lap_time = float(line[3:])
        # Store the lap time in the dictionary accrodingly.
        lap_times[driver_code].append(lap_time)
    # Return the dictionary of lap times for each driver.
    lap_count = {driver: len(times) for driver, times in lap_times.items()}
    # Return the dictionary of lap times for each driver and the lap count for each driver.
    return location, lap_times, lap_count

def display_results(location, lap_times, driver_info, lap_count):

    """This function displays the results of the race."""
    # Calculate the fastest lap time for each driver.
    fastest_times = {driver: min(times) for driver, times in lap_times.items()}
    # Calculate the average lap time for each driver.
    average_times = {driver: mean(times) for driver, times in lap_times.items()}
    # Calculate the overall average lap time across all drivers.
    overall_average = mean([time for times in lap_times.values() for time in times])
    # Sort drivers by their fastest lap time.
    sorted_fastest_times = sorted(fastest_times.items(), key=lambda x: x[1])
    # Get the driver with their fastest lap time.
    top_driver_time = sorted_fastest_times[0]
    
    # Initalize a empty list to store the results.
    table = []

    # Loop through the sorted drivers and store the results in the list.
    for driver, time in sorted_fastest_times:
        info = driver_info.get(driver, {'name': 'Unknown', 'team': 'Unknown'})
        table.append([driver, info['name'], info['team'], time, average_times[driver], lap_count[driver]])
        
    # Display the result.
    print("\n")
    print(f"Overall Drivers Average Time: {overall_average:.3f}\tTop Driver Code & Time: [{top_driver_time[0]}: {top_driver_time[1]}]\tRace Location: {location}")
    print(tabulate(table, headers=["Driver Code", "Name", "Team", "Fastest Time", "Average Time", "Lap Count"], tablefmt="fancy_grid"))

def plot_driver_lap_times(lap_times):

    """ This function plots the lap times for each driver."""
    
    # Iterate over the lap times for each driver.
    for driver, lap_times in lap_times.items():
        # Plot the lap times using matplotlib.
        plt.figure(figsize=(10, 5))
        plt.plot(lap_times, marker='o', color= "green", label=f"Driver {driver}")
        plt.title(f'Lap Timings for {driver}', fontsize=14, fontweight='bold')
        plt.xlabel('Lap Count', fontsize=12, fontweight='bold')
        plt.ylabel('Lap Time (seconds)', fontsize=12, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()


def main():

    """ This function is the main function of the program."""

    # Checks if the user has provided the required arguments.
    if len(sys.argv) != 2:
        # If not, print the usage and exit the program.
        print("Usage: python main.py <lap_times_file>")
        return
    
    # Get the file name from the command line argument.
    lap_times_file = sys.argv[1]
    # Read the file and store the data in a dictionary.
    driver_info_file = 'F1_DRIVERS.TXT'
    
    # Read the driver info from the file.
    if not os.path.exists(lap_times_file):
        # If the file does not exist, print an error message and exit the program.
        print(f"Error: File '{lap_times_file}' not found.")
        return
    driver_info = read_driver_info(driver_info_file)
    location, lap_times, lap_count = read_lap_times(lap_times_file)
    display_results(location, lap_times, driver_info, lap_count)
    plot_driver_lap_times(lap_times)

# Call the main function.
if __name__ == "__main__":
    main()

