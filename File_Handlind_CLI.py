import os
from datetime import datetime


#load task
def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            task_data = line.strip().split("|")
            task = {
                "name": task_data[0],
                "description": task_data[1],
                "due_date": datetime.strptime(task_data[2],"%y%m%d"),
                "priority": task_data[3],
                "completed": task_data[4] == "True"
                }
            task.append(task)
    except FileNotFoundError:
        pass
    return tasks

#save task to file

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            due_date_str = task['due_date'].strftime("%Y-%m-%d") #it is important to convert date into string to save a file
            file.write(f"{task['name']} | {task['description']} | {due_date_str} | {task['priority']} | {task['completed']}\n")

#add task

def add_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = datetime.strptime(input("Enter due date (YYYY-MM-DD): "), "%Y-%m-%d")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    
    task = {
        "name": name,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully.")

#View Task
    
def view_tasks(tasks):
    if not tasks:
        print("No Task Found.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - Due: {task['due_date'].strftime('%Y-%m-%d')} - Priority: {task['priority']}")
        print(f" Description: {task['description']}")
        print(f" Status: {'completed' if task['completed'] else 'Pending'}")
        print()

#Mark Task as Completed
        
def mark_complete(tasks):
    try:
        choice = int(input("Enter the number of task you want to mark as complete: ")) -1
        if 0 <= choice < len(tasks):
            tasks[choice]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid Task number.")
    except ValueError:
        print("Please Enter Valid Task number.")

#Search Task
        
def search_task(tasks):
    keywords = input("Enter Search Keyword: ").lower()
    results = [task for task in tasks if keywords in task["name"].lower() or keywords in task["description"].lower()]

    if results:
        print("Search Results: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} - Due: {task['due_date'].strftime('%Y-%m-%d')} - Priority: {task['priority']}")
            print(f" Description: {task['description']}")
            print(f" Status: {'completed' if task['completed'] else 'Pending'}")
            print()
    else:
        print("No Matching Task Found.")

#Main Function
def main():
    tasks = load_tasks()

    while True:
        print("TASK MANAGER\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Search Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            search_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid Chooice. Please Try Again.")
if __name__ == "__main__":
    main()            
            
    
