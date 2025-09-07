import json
import os

# load_tasks - reads from json
def load_tasks():
    try:
        with open("tasks.json", 'r', encoding='utf-8') as file:
            # raw = file.read()
            # # print("Raw file content: ")
            # # print(raw)
            # data = json.loads(raw)
            # print(data)
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error. File not found")
    except json.JSONDecodeError:
        print("Error. Could not decode JSON from file. Check if it is valid JSON file.")



# save_tasks - writes to json
def save_tasks(my_task):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(my_task, file, indent=4)
        print("JSON file got updated successfully.")

#add_task(myTask) --> adds a task
def add_task(my_task):
    tasks = load_tasks() #1. Load existing
    new_number = len(tasks) + 1
    tasks.append({"number": new_number, "task": my_task, "done": False})
    save_tasks(tasks)
    print("Finished adding task: ", my_task)

#remove_task(task_number) (function that helps remove task if accidently put the task in)
def remove_task(task_number):
    updated_tasks =[]
    tasks = load_tasks()
    for t in tasks:
        if t["number"] != task_number:
            updated_tasks.append(t)
    print("Removed successfully task ", task_number)
    save_tasks(updated_tasks)
    return updated_tasks



#show_tasks() --> prints tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Currently have no tasks. Brain, let me give some tasks. What is a rational action now?")
    else:
        for t in tasks:
            if t["done"]: 
                status = "\u2713"
            else:
                status = "\u2717"
            print(f"{t['number']}.{t['task']}[{status}]")

#complete_task(task_number)-->mark a task as done 
def complete_task(task_number):
    tasks = load_tasks()
    tasks[task_number]["done"] = True;
    save_tasks(tasks)
    print("Completed task ", task_number)

#main function
def main():
    load_tasks()
    print("CURRENT TASKS")
    show_tasks()
    # print("ADD ONE MORE TASK")
    # add_task("Clearing the table.")
    # print("CURRENT TASKS AFTER ADDING")
    # show_tasks()
    # print("REMOVE TASK 2")
    # remove_task(2)
    # print("CURRENT TASKS ABOUT REMOVING TASK 1")
    # show_tasks()
    complete_task(3)
    show_tasks()


if __name__ == "__main__":
    main()

