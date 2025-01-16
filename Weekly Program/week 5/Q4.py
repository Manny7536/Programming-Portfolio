"""This program takes a URL as a command-line argument and reports
whether or not there is a working website at that address."""

import sys
import requests

# Function to check if a website is working
def check_website(url):
    try:
        # Send a HEAD request to the URL
        response = requests.head(url, timeout=5)
        # Check the status code of the response
        if response.status_code == 200:
            # If the status code is 200, prints website is working.
            print(f"The website at {url} is working.")
        else:
            # If the status code is not 200, prints the status code.
            print(f"The website at {url} returned status code: {response.status_code}")
    # Handle exceptions
    except requests.RequestException as e:
        # If an exception occurs, prints an error message.
        print(f"Error: Could not connect to {url}. Details: {e}")

def main():
    # Check if the user provided a URL as a command-line argument
    if len(sys.argv) != 2:
        # If not, prints usage message and exits.
        print("Usage: python check_website.py <URL>")
        return
    # Get the URL from the command-line argument
    url = sys.argv[1]
    # Call the check_website function with the URL
    check_website(url)

if __name__ == "__main__":
    main()
