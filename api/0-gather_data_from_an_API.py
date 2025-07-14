#!/usr/bin/python3
"""
Script to fetch an employee's TODO list progress using an API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # More efficient API usage
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_res = requests.get(user_url)
    todos_res = requests.get(todos_url)

    if user_res.status_code != 200:
        print(f"No user found with ID {employee_id}")
        sys.exit(1)

    employee_name = user_res.json().get("name")
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

