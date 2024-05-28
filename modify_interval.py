import requests

# Prompt the user to provide an access token and account ID to use the API
TOKEN = input("Provide Token: ")
AID = input("Provide aid: ")

# Set up the headers for the HTTP requests, including the content type, accepted response format, and authorization token
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/hal+json",
    "Authorization": f"Bearer {TOKEN}",
}

# Define a function to get a list of test IDs from the ThousandEyes API
def get_test_ids(headers, aid):
    # Construct the URL with the account ID parameter
    url = f"https://api.thousandeyes.com/v7/tests?aid={aid}"
    # Send a GET request to the API and parse the JSON response
    response = requests.get(url, headers=headers).json()
    # Extract the list of tests from the response
    tests = response.get("tests")
    # Get the test ID from each test in the list
    test_ids = [test.get("testId") for test in tests]
    return test_ids

# Define a function to modify tests by sending a PUT request to the API
def modify_test(headers, test_ids, aid):
    # Define the payload to modify the test interval and add a description
    payload = '{"interval": 120, "description": "API Modification"}'
    # Loop through each test ID and send a PUT request to modify the test configuration
    for test_id in test_ids:
        # Construct the URL for the specific test ID with the account ID parameter
        url = f"https://api.thousandeyes.com/v7/tests/http-server/{test_id}?aid={aid}"
        # Send a PUT request with the payload and print the response text
        response = requests.put(url, headers=headers, data=payload)
        print(response.text)

# Define the main function to orchestrate the API calls
def main():
    # Get the list of test IDs using the provided headers and account ID
    test_ids = get_test_ids(HEADERS, AID)
    # Modify each test with the new interval and description
    change_interval = modify_test(HEADERS, test_ids, AID)

# If this script is executed as the main program, run the main function
if __name__ == "__main__":
    main()
