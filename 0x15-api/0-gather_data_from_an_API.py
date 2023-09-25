#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Make a GET request to retrieve user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Employee not found.")
        return

    employee_name = user_data['name']

    # Make a GET request to retrieve user's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the employee's TODO list progress
    print(
        f"Employee {employee_name} is done with tasks "
        f"({completed_tasks}/{total_tasks}):"
    )
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure the employee ID is an integer
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
