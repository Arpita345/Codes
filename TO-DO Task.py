class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"[{'Completed' if self.completed else 'Pending'}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = not self.tasks[task_number - 1].completed
            print("Task updated!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number!")

def main():
    todo_list = ToDoList()
    while True:
        choice = input("\nTo-Do List Application\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit\nEnter your choice: ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            todo_list.update_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
