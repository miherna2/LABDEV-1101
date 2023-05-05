# LABDEV-1101 - Task 4: Using Python Requests to Consume the Data and Create a Report

### Introduction
This Python script demonstrates how to use the ThousandEyes API to retrieve a list of agents and export their details to a CSV file. The script prompts the user to provide their email, API token, and Account Group Identifier (AID), which are used to authenticate the API request. The script then sends an HTTP GET request to the ThousandEyes API to retrieve a list of agents associated with the provided AID.

The response from the API is in JSON format, which is parsed to extract the relevant information about each agent. The script then writes this data to a new row in a CSV file called **agents_details.csv** using the **csv.DictWriter** class.


### Prerequisites
* Python 3.x
* **requests** module
* **csv** module
* **getpass¨ module


### How to use
1. Download the script.
2. In this environment the required modules are pre-installed. However, in different environments it will be required to install the modules by running **pip install requests csv getpass** in your terminal.
3. Open a terminal and navigate to the directory where the script is saved.
4. Run the script by typing **python agent_details.py** and pressing Enter.
5. Follow the prompts to provide your email, API token, and AID.
6. The script will create a new CSV file called agents_details.csv in the same directory as the script and write the agent details to it.


**Note**: You will need valid credentials for the ThousandEyes API to use this script. 

### Further Information
ThousandEyes API documentation: **https://developer.thousandeyes.com/v6/**    
**requests** module documentation: **https://docs.python-requests.org/en/master/**    
**csv** module documentation: **https://docs.python.org/3/library/csv.html**    
**getpass** module documentation: **https://docs.python.org/3/library/getpass.html**    
