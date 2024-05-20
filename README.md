# LABDEV-1101 - Task 4: Modifying the Interval of Multiple Tests Using Python Requests

## Introduction
This Python script is designed to automate the process of modifying the interval of multiple tests using the ThousandEyes API. It allows users to update the interval settings for a batch of tests quickly and efficiently. The script requires the user's email, API token, and Account Group Identifier (AID) for authentication. It sends an HTTP GET request to the ThousandEyes API to retrieve a list of tests associated with the AID.

The script then parses the JSON response to extract the relevant details of each test. Users can specify the new interval, and the script will iterate over the list of tests, sending HTTP PUT requests to update their intervals accordingly. This bulk update saves time and ensures consistency across tests.

## Prerequisites
- Python 3.x
- requests module
- csv module
- getpass module

## How to Use
1. Download the script.
2. Ensure that the required modules are installed. If not, install them by running `pip install requests csv getpass` in your terminal.
3. Open a terminal and navigate to the directory containing the script.
4. Execute the script by typing `python modify_test_intervals.py` and press Enter.
5. Follow the on-screen prompts to enter your email, API token, and AID.
6. The script will process the list of tests and update their intervals as specified.

Note: Valid ThousandEyes API credentials are necessary to utilize this script successfully.

## Further Information
- [ThousandEyes API documentation](https://developer.thousandeyes.com/)
- [requests module documentation](https://docs.python-requests.org/en/master/)
- [csv module documentation](https://docs.python.org/3/library/csv.html)
- [getpass module documentation](https://docs.python.org/3/library/getpass.html)
