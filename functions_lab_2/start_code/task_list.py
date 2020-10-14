
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# task 1

def incompleted_tasks(tasks):
    list_of_incomplete = []
    for task in tasks:
        if task["completed"] == False:
            list_of_incomplete.append(task)
    return list_of_incomplete

print(incompleted_tasks(tasks))

# task 2 

def completed_tasks(tasks):
    list_of_complete = []
    for task in tasks:
        if task["completed"] == True:
            list_of_complete.append(task)
    return list_of_complete

print(completed_tasks(tasks))

# task 3

def description_tasks(list):
    list_of_description = []
    for task in list:
        list_of_description.append(task["description"])
    return list_of_description

print(description_tasks(tasks))

# task 4

def get_tasks_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] > time:
            tasks.append(task)
    return tasks
print(get_tasks_longer_than(tasks, 20))

# task 5

def get_task_by_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
print(get_task_by_description(tasks, "Walk Dog"))

# task 6

def mark_task_complete(list, description):
    for task in list:
        if task["description"] == description:
            task["completed"] = True
print(tasks)
mark_task_complete(tasks,"Feed Cat")
print(tasks)

# task 7 

def create_task(list, task_to_add):
    list.append(task_to_add)

print(tasks)
create_task(tasks, { "description": "Make Lunch", "completed": True, "time_taken": 30 })
print(tasks)

# task 9

print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")