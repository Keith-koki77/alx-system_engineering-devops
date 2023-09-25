#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    """ Create a list to store task data"""
    task_data = []

    for todo in todos:
        task_title = todo.get("title")
        completed = todo.get("completed")

        """Create a dictionary for each task"""
        task_info = {
            "task": task_title,
            "completed": completed,
            "username": username
        }

        """Append the task info to the list"""
        task_data.append(task_info)

    """
    Create a dictionary with the user ID as
    the key and the task data as the value
    """
    user_task_data = {
        user_id: task_data
    }

    """Define the file name as USER_ID.json"""
    file_name = "{}.json".format(user_id)

    """Write the JSON data to the file"""
    with open(file_name, "w") as json_file:
        json.dump(user_task_data, json_file, indent=4)

    print("Data exported to {}".format(file_name))
