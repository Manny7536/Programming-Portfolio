import random
import datetime
import threading
import yaml 

def load_file(file_path):

    """This functions Load a YAML file and return its content as a dict and list."""

    with open(file_path) as file:
        data = yaml.safe_load(file)
        # Gets keywords and responses from the YAML file and returns them as a dictionary.
        keyword_responses = data.get("keyword_responses", {})
        # Gets the list of fallback responses from the YAML file and returns it as a list.
        fallback_responses = data.get("fallback_responses", [])
        # Gets the agents from the YAML file and returns them as list.
        agents_name = data.get("agents_name", [])
        return keyword_responses, fallback_responses, agents_name

def get_response(user_input, keyword_responses, fallback_responses, user_name):

    """This functions generates a response based on the user's input by matching keywords 
    or using fallback responses."""

    # Initialize a variable to store multiple responses.
    multiple_response = []
    # Iterate over each keyword and its corresponding response in the dictionary.
    for keyword, responses in keyword_responses.items():
        # Check if the user's input contains the keyword.
        if keyword in user_input.lower():
            # If the keyword is found, append the corresponding response to the list.
            multiple_response.append(responses)
    # If multiple responses prints responses in following format.        
    if multiple_response:
        responses = " ".join(multiple_response)
    else:
        # If no keyword is found, select a random response from the list of fallback responses.
        responses = random.choice(fallback_responses)
    # Return the response and the user's name if random choice is True.
    if random.choice([True, False, False]):
        responses = f"{responses[:-1]}, {user_name}"
    return responses


def log_to_file(file_path, log_entry):

    """Append a log entry to the specified file."""

    with open(file_path, "a") as file:
        # Append the log entry to the file ending with a newline character.
        file.write(log_entry + "\n")


def main():

    """Main function to runs the chatbot and handle user interaction."""
    
    # Define the path to the YAML file and the log file.
    file_path = 'responses.yaml'
    log_file_path = 'chat_conversation.log'

    # Load the keyword responses, fallback responses, and agents from the YAML file.
    keyword_responses, fallback_responses, agents_name = load_file(file_path)
    # Initialize a variable, timer to track user inactivity initiliazed as None.
    inactivity_timer = None
    # Boolean to indicate weather the user has disconnected.
    disconnected = False
    # Randomly select an agent from the list of agents.
    agent_name = random.choice(agents_name)
    # Prompt the user for name and format it.
    name = input("Welcome to college_bot. Enter Your name to start conversation: ").split()
    user_name = " ".join(name.capitalize() for name in name[:1])

    # Log the conversation start details.
    log_to_file(log_file_path, f"Chat started at {datetime.datetime.now()}")
    log_to_file(log_file_path, f"Agent: {agent_name}")
    log_to_file(log_file_path, f"User: {user_name}")

    # Greet the user with their name & agent name
    print(f"Hello, {user_name}! My name is {agent_name}, and I'm here to make your experience as sweet and delightful as a cherry on top. \nHow can I assist you Today?")

    def handle_inactivity():
        """
    This function is called when the user is inactive for a predefined period (20 seconds).
    It sends a message to prompt the user and starts a shorter timer to disconnect the chat if no response is received.
    """
        
        nonlocal inactivity_timer
        # Display the inactivity message
        response = f"{user_name}, are you still there? Please respond!"
        # Send the message to the user
        print(f"\n{agent_name}: {response}")
        # Log the inactivity message
        log_to_file(log_file_path, f"{agent_name}: {response}")
        # Set the inactivity timer to 10 seconds
        inactivity_timer = threading.Timer(10, disconnect_chat)
        # Start the inactivity timer
        inactivity_timer.start()

    def disconnect_chat():

        """ This function disconnects the chat due to prolonged inactivity. 
    It logs the disconnection message and cancels any existing inactivity time.
    """

        nonlocal inactivity_timer
        nonlocal disconnected
        # Indicate that the chat has been disconnected
        disconnected = True 
        # prints a disconnection message
        response = "Chat disconnected due to inactivity."
        print(f"{agent_name}: {response}")
        # Logs the disconnection message
        log_to_file(log_file_path, f"{agent_name}: {response}")
        log_to_file(log_file_path, f"Chat ended at {datetime.datetime.now()}\n")
        # Cancel any existing inactivity timer
        if inactivity_timer:
            inactivity_timer.cancel()

    while not disconnected:

        """Main chat loop that continuously processes user inputs until the chat is disconnected.
    It resets the inactivity timer after every user input and handles special commands."""
        
        # Cancel any previous inactivity timer before starting a new one
        if inactivity_timer:
            inactivity_timer.cancel()
        # Set a timer for inactivity handling (20 seconds)
        inactivity_timer = threading.Timer(20, handle_inactivity)
        inactivity_timer.start()

        # Prompt the user for input
        user_input = input(f"{user_name}: ")
        # Check if disconnected during inactivity
        if disconnected:
            # If disconnected, exit the loop
            break
        # Log the user input
        log_to_file(log_file_path, f"{user_name}: {user_input}")

        # Check for user exit keywords and terminate the chat gracefully
        if any(keyword in user_input.lower().split() for keyword in ["bye", "exit", "end", "quit"]):
            response = (f"Goodbye! Have a great day! {user_name}")
            # Notify the user about ending the chat
            print(f"{agent_name}: {response}")
            # Log the disconnection message
            log_to_file(log_file_path, f"{agent_name}: {response}")
            # Cancel the inactivity timer
            inactivity_timer.cancel()
            # Log the end of the chat
            log_to_file(log_file_path, f"Chat ended at {datetime.datetime.now()}\n")
            break

        # Check for keywords to transfer the user to a different agent.
        if any(keyword in user_input.lower().split() for keyword in ["agent", "different", "someone"]):
            response = "Sure! Let me try to connect you with a different agent."
            # Notify the user about the agent transfer attempt
            print(f"{agent_name}: {response}")
            log_to_file(log_file_path, f"{agent_name}: {response}")

            # Randomly select a new agent from the list
            new_agent = random.choice(agents_name)
            if new_agent != agent_name:
                # Update the current agent's name
                agent_name = new_agent
                response = f"Hello, {user_name}! My name is {agent_name}, How may I assist you today?"
                # Introduce the new agent
                print(f"{agent_name}: {response}")
                log_to_file(log_file_path, f"{agent_name}: {response}")
            else:
                response = f"Sorry {user_name}, other agents are not available right now. How can I assist you today?"
                # Inform the user that no other agent is available
                print(f"{agent_name}: {response}")
                log_to_file(log_file_path, f"{agent_name}: {response}")
            continue

        # Simulate random technical difficulties (5% chance of error occurring)
        if random.randint(1, 20) == 1: 
            response = "We are having some technical difficulties. Please try again later."
            # Notify the user about the issue
            print(response)
            # Log the technical difficulty
            log_to_file(log_file_path, f"Error: {response}")
            # Cancel the inactivity timer
            inactivity_timer.cancel()
            break
        # Generate a response based on user input
        response = get_response(user_input, keyword_responses, fallback_responses, user_name)
        # Print the response to the console
        print(f"{agent_name}: {response}")
        # Log the response to the file
        log_to_file(log_file_path, f"{agent_name}: {response}")

# Run the main function
if __name__ == "__main__":
    main()
