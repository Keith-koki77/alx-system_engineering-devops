#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    """
    Create a dictionary to store task data for all employees
    """
    all_employee_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        """
        Filter tasks for the current employee
        """
        employee_tasks = [todo for todo in todos if
                          todo.get("userId") == user_id]

        """
        Create a list to store task data for the current employee
        """
        task_data = []

        for task in employee_tasks:
            task_title = task.get("title")
            completed = task.get("completed")

            """
            Create a dictionary for each task
            """
            task_info = {
                "username": username,
                "task": task_title,
                "completed": completed
            }

            """Append the task info to the list"""
            task_data.append(task_info)

        """
        Add the task data for the current employee to the dictionary
        """
        all_employee_tasks[user_id] = task_data

    """
    Define the file name as todo_all_employees.json
    """
    file_name = "todo_all_employees.json"

    """
    Write the JSON data to the file
    """
    with open(file_name, "w") as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)

    print("Data exported to {}".format(file_name))
