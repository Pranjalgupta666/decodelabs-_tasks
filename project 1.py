tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n----- Your Tasks -----")
            for i, task in enumerate(tasks, start=1):
                status = "✔ Completed" if task["completed"] else "⏳ Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                print(f"🗑 Deleted: {removed['task']}")
            except:
                print("Invalid task number!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                num = int(input("Enter task number completed: "))
                tasks[num - 1]["completed"] = True
                print("🎉 Task marked as completed!")
            except:
                print("Invalid task number!")

    elif choice == "5":
        print("Thank you for using To-Do List Manager!")
        break

    else:
        print("Invalid choice! Please try again.")