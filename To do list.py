'''
print("\n\t---- WELLCOME TO MY TO DO LIST PYTHON PROGRAM ----")

def task():
    tasks = []

    user_input = int(input("\n\t How many tasks do you want to add: "))
    for i in range(1, user_input +1):
        task_names = input(f"\tEnter Task {i}= ")
        tasks.append(task_names)

    print(f"Todays tasks are {tasks}")

    while True:
        opretion = int(input(f"Press\n1. add\n2. delete\n3. update\n4. View\n5. Exit\n"))

        if opretion == 1:
            add = input("Enter the task you want to add = ").capitalize
            tasks.append(add)

        elif opretion == 2:
            delet = input("Enter the task you want to delete = ").capitalize
            if delet in tasks:
                ind = tasks.index(delet)
                del tasks [ind]
                
                print(f"Task {delet} has been deleted from {tasks}")

        elif opretion == 3:
            update = input("Enter the task you want to update = ").capitalize
            if update in tasks:
                up = input("New task")
                ind = tasks.index(update)
                tasks[ind] = up

                print(f"Updated task {up}")

        elif opretion == 4:
            print(f"Your tasks\t{tasks}")

        elif opretion == 5:
            print("---- THANKS FOR VISITING MY CODE ----")
            break
        else :
            print("Invalid input")

task()

'''
# ---------------------------------------------------------------------------------------------------



def task():
    
    print("\n\t----> WELLCOME TO MY TO DO LIST PYTHON PROGRAM <----")
    tasks = []

    user_input = int(input("\n\t How many tasks do you want to add: "))
    for i in range(1, user_input +1):
        task_names = input(f"\tEnter Task {i}= ")
        tasks.append(task_names)

    print(f"Todays tasks are {tasks}")

    while True:
        operation = int(input(f"Press\n1. add\n2. delete\n3. update\n4. View\n5. Exit\n6. Save to file\n"))

        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)

        elif operation == 2:
            delete = input("Enter the task you want to delete = ")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                
                print(f"Task {delete} has been deleted from {tasks}")

        elif operation == 3:
            update = input("Enter the task you want to update = ")
            if update in tasks:
                up = input("New task: ")
                ind = tasks.index(update)
                tasks[ind] = up

                print(f"Updated task {up}")

        elif operation == 4:
            print(f"Your tasks\t{tasks}")

        elif operation == 5:
            print("---- THANKS FOR VISITING MY CODE ----")
            break

        elif operation == 6:
            path = input("Enter the directory path where you want to save the file: ")
            name = input("Rename the file : ")
            full_path = (f"{path}/{name}.txt")

        else:
            print("Invalid input")

task()