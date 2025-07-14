#!/usr/bin/python3
"""
Exports all TODO tasks of a given user to a CSV file.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    api_base = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_res = requests.get("{}/users/{}".format(api_base, user_id))
    if user_res.status_code != 200:
        print("User not found.")
        sys.exit(1)
    username = user_res.json().get("username")

    # Fetch user's todos
    todos_res = requests.get("{}/users/{}/todos".format(api_base, user_id))
    todos = todos_res.json()

    # Write to CSV file named <user_id>.csv
    with open("{}.csv".format(user_id), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])

