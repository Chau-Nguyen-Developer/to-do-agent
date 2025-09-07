import json
import os

# load_tasks - reads from json
def load_tasks():
    try:
        with open("tasks.json", 'r', encoding='utf-8') as file:
            raw = file.read()
            # print("Raw file content: ")
            # print(raw)
            data = json.loads(raw)
            # print(data)
            return data
    except FileNotFoundError:
        print("Error. File not found")
    except json.JSONDecodeError:
        print("Error. Could not decode JSON from file. Check if it is valid JSON file.")



# save_tasks - writes to json
def save_tasks(myTask):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(myTask, file, indent=4)
        print("Finished saving tasks.")

#add_task(myTask) --> adds a task
def add_task(myTask):
    tasks = load_tasks() #1. Load existing
    new_number = len(tasks) + 1
    tasks.append({"number": new_number, "task": myTask, "done": False})
    save_tasks(tasks)
    print("Finished adding task: {myTask}")

#show_tasks() --> prints tasks
def show_tasks():
    tasks = load_tasks()
    print(tasks)

#complete_task(task_number)-->mark a task as done 

#main function
def main():
    load_tasks()
    show_tasks()
    add_task("Doing laundry.")
    print("Just add a task.\n")
    show_tasks()

if __name__ == "__main__":
    main()

