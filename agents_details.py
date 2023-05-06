# Import the 'csv' module for reading and writing CSV files
import csv
# Import the 'getpass' function from the 'getpass' module for securely reading a user's input
from getpass import getpass
# Import the 'requests' module for making HTTP requests
import requests

# Prompt the user for their email and store the result in a variable
EMAIL = input("Provide email: ")
# Prompt the user for their API token and store the result in a variable (using the getpass function for security)
TOKEN = input("Provide Token: ")
# Prompt the user for the AID (account ID) and store the result in a variable
AID = input("Provide aid: ")
# Define a dictionary of HTTP headers to be sent with the API request
HEADERS = {"content-type": "application/json"}
# Construct the URL for the API request using the provided AID
URL = f"https://api.thousandeyes.com/v6/agents.json?aid={AID}"
# Make an HTTP GET request to the API using the 'requests' module, passing in the authentication credentials and headers
API_CALL = requests.get(URL, auth=(EMAIL, TOKEN), headers=HEADERS)
# Extract the JSON response from the API call
RESPONSE = API_CALL.json()
# Extract the 'agents' list from the JSON response and store it in a variable
AGENTS = RESPONSE.get("agents")


# Open a new CSV file in write mode with the name 'agents_details.csv'
with open("agents_details.csv", mode="w", encoding="utf-8", newline="") as csv_file:

    # Define the field names for the CSV file
    fields = [
        "agent_id",
        "agent_name",
        "country_id",
        "ip_address",
        "location",
    ]

    # Create a new CSV writer object with the specified field names
    writer = csv.DictWriter(csv_file, fieldnames=fields)

    # Write the header row to the CSV file using the field names
    writer.writeheader()

    # Loop through the list of agents and write each one to a new row in the CSV file
    for agent in AGENTS:

        # Extract the relevant data for each agent
        agent_id = agent.get("agentId")
        agent_name = agent.get("agentName")
        country_id = agent.get("countryId")
        ip_address = agent.get("ipAddresses")
        ip_address = " - ".join(ip_address)
        location = agent.get("location")

        # Write the agent data to a new row in the CSV file using a dictionary
        writer.writerow(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
                "country_id": country_id,
                "ip_address": ip_address,
                "location": location,
            }
        )
