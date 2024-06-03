import csv
import requests
import os

# Function to fetch data from API
def fetch_data(api_url, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(api_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None

# Function to filter US Cloud agents
def filter_us_cloud_agents(agents):
    return [agent for agent in agents if agent['agentType'] == 'cloud' and agent['countryId'] == 'US']

# Function to write data to CSV
def write_to_csv(filtered_agents, filename='us_cloud_agents.csv'):
    if not filtered_agents:
        print("No data to write to CSV.")
        return
    # Collect all possible fieldnames
    fieldnames = set()
    for agent in filtered_agents:
        fieldnames.update(agent.keys())
    fieldnames = list(fieldnames)
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_agents)

def main():
    aid = 'YOUR_ACCOUNT_GROUP_ID'  # Replace with actual Account Group ID
    auth_token = 'YOUR_AUTH_TOKEN'  # Replace with your actual authorization token
    api_url = f'https://api.thousandeyes.com/v7/agents?aid={aid}'

    # Fetch data from API
    data = fetch_data(api_url, auth_token)
    if data is None:
        print("Failed to fetch data from the API. Exiting the script.")
        return  # Exit the main function if data fetching failed

    # Filter US Cloud agents
    agents = data.get('agents', [])
    us_cloud_agents = filter_us_cloud_agents(agents)

    # Determine the path to the Desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop_path, 'us_cloud_agents.csv')

    # Write filtered data to CSV
    if us_cloud_agents:
        write_to_csv(us_cloud_agents, file_path)
        print(f"CSV report created successfully with {len(us_cloud_agents)} US Cloud agents.")
    else:
        print("No US Cloud agents found.")

if __name__ == "__main__":
    main()
