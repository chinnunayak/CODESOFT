#program for To-Do Listg
#This is creates an empty list named "tasks"
tasks = []
#main Program
while True:
    print("To-do list:")
    print("1. Add tasks")
    print("2. view tasks") 
    print("3. Remove tasks")
    print("4. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        #Add Task
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == "2":
        #View Tasks
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
    elif choice =="3":
        #Remove Task
        task_index = int(input("Enter the task number to remove:")) - 1
        if 0 <=task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Remove task: {removed_task}")
        else:
            print("Invalid task number.")
    elif choice =="4":
        #Exit the Program
        break
    else:
        print("Invalid choice. Please select valid Option.")
