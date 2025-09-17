todo_list = []
def show_tasks():
    if not todo_list:
        print("You Have No Task Yet")
    else:
        for (i),task in enumerate(todo_list,1):
            print(f"{i}.task")
def add_task():
    task=input("Enter task to be added")
    todo_list.append(task)
    print("New Task Added")

def removetaskusing():
    index= input("Enter the number you want to delete")
    if 0<index<=len(todo_list):
        removed_task=todo_list.pop(index-1)
        print(f"Deleted{removed_task}")
    else:
        print("Invalid Task Number")

def showie():
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter Option From 1-4")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        removetaskusing()
    elif choice == "4":
        print("Goodbye")
        
    else:
        print("Enter a vaild Option")
        showie()
showie()

 
