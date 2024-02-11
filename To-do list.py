def display_list(todo_list):
    if not todo_list:
        print("You haven't added any tasks yet.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(todo_list):
    task = input("Enter your task: ")
    todo_list.append(task)
    print("Task added!")

def update_task(todo_list):
    display_list(todo_list)
    choice = int(input("Enter the task number to update: "))
    if 0 < choice <= len(todo_list):
        new_task = input("Enter the new task: ")
        todo_list[choice - 1] = new_task
        print("Task updated!")
    else:
        print("Invalid choice.")

def delete_task(todo_list):
    display_list(todo_list)
    choice = int(input("Enter the task number to delete: "))
    if 0 < choice <= len(todo_list):
        task = todo_list.pop(choice - 1)
        print(f"Task '{task}' deleted!")
    else:
        print("Invalid choice.")

def main():
    todo_list = []

    while True:
        print("\nMenu:")
        print("1. Display to-do list")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            update_task(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
