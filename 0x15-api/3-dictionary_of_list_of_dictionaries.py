#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
import requests
from sys import argv


def fetch_employee_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todos_url = f'{base_url}users/{employee_id}/todos'

    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    if response_user.status_code != 200:
        print(f"Failed to fetch user data for ID {employee_id}")
        return None, None

    user_data = response_user.json()
    todos_data = response_todos.json()

    return user_data, todos_data


def generate_employee_json(employee_id, user_data, todos_data):
    if not user_data or not todos_data:
        return None

    username = user_data.get('username', 'user name not found')

    records = {
        employee_id: [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos_data
        ]
    }

    return records


def save_to_json_file(data, filename):
    if not data:
        return

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(argv) != 1:
        print("Usage: python script.py")
    else:
        all_records = {}
        for employee_id in range(1, 11):  # Assuming employee IDs from 1 to 10
            user_data, todos_data = fetch_employee_data(employee_id)
            employee_json_data = generate_employee_json(
                employee_id, user_data, todos_data)
            if employee_json_data:
                all_records.update(employee_json_data)

        if all_records:
            save_to_json_file(all_records, 'todo_all_employees.json')
