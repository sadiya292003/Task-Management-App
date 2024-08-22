def task():
    tasks = []  # Initialize an empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many tasks you want to add = "))  # Get number of tasks to add
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")  # Get task name
        tasks.append(task_name)

    while True:
        print(f"Today's tasks are: {tasks}")
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))

        if operation == 1:
            add = input("Enter Task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
    
                tasks[ind] = up
                print(f"Updated task to '{up}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task '{del_val}' has been deleted...")
            else:
                print(f"Task '{del_val}' not found.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid Input. Please enter a number between 1 and 5.")

# Call the function to run the app
task()