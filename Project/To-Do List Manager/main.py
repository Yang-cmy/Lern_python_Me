def show_menu():
    print("\n📝 To-Do List Manager")
    print("Choose an option:")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Delete Task")
    print("[4] Exit")

def add_task(tasks):
        task = input("Enter the task to add : ")
        tasks.append(task)

def view_task(tasks):
    if not tasks:
        print("No task in your list")
    else:
        print("📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks):
    if tasks == 0:
        print("Your Task is empty")
    else:
         task_num = int(input("Enter the task number to delete : "))1
         removed = tasks.pop(task_num - 1)
         print(f"❌ Task '{removed}' deleted.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()


