#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    """Define the base URL for the REST API"""
    url = "https://jsonplaceholder.typicode.com/"

    """
    Get the user information by making a GET request
    to the "/users" endpoint
    """
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    """
    Get the TODO list for the user by making a GET
    request to the "/todos" endpoint
    """
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    """
    Create a list of completed task titles by filtering the TODO list
    """
    complete = [t.get("title") for t in todos if t.get("completed") is True]

    """
    Print a summary of the user's completed tasks
    """
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))

    """
    Print the titles of completed tasks with indentation
    """
    [print("\t {}".format(c)) for c in complete]
