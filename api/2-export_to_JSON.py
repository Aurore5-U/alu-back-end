#!/usr/bin/python3
"""
Exports all TODO tasks of a given user to a JSON file.
Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...] }
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        api_endpoint = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]

        # Get user data
        user_response = requests.get("{}/users/{}".format(api_endpoint, user_id))
        if user_response.status_code != 200:
            print("User not found.")
            sys.exit(1)
        username = user_response.json().get("username")

        # Get TODOs
        todo_response = requests.get("{}/users/{}/todos".format(api_endpoint, user_id))
        todo_data = todo_response.json()

        # Build the task list
        tasks = []
        for task in todo_data:
            tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            })

        # Dump to JSON file
        data = {user_id: tasks}
        with open("{}.json".format(user_id), 'w') as json_file:
            json.dump(data, json_file)

