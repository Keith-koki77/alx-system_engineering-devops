#!/usr/bin/python3
"""
 Python script to export data in the CSV format
"""

import requests
import sys
import csv

if __name__ == "__main__":

    """
    Get the user ID from command line arguments
    """
    user_id = sys.argv[1]

    """
    Define the base URL for the REST API
    """
    url = "https://jsonplaceholder.typicode.com/"

    """
    Fetch user data using the user ID
    """
    user = requests.get(url + "users/{}".format(user_id)).json()

    """
    Extract the username from the user data
    """
    username = user.get("username")

    """
    Fetch the user's TODO list using the user ID
    """
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    """
    Open a CSV file for writing with the user ID as the file name
    """
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        """
        Create a CSV writer object
        """
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        """
        Iterate through each TODO item and write it to the CSV file
        """
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
