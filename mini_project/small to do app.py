import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    def from_dict(data):
        return Task(
            task_id=data["id"],
            title=data["title"],
            completed=data["completed"]
        )
class TodoApp:
    def __init__(self, file="todo.json"):
        self.file = file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        
        if os.path.exists(self.file):
            with open(self.file, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            self.tasks = []
    def save_tasks(self):
        with open(self.file, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
    def add_task(self, title):
        new_id = self.tasks[-1].id + 1 if self.tasks else 1
        task = Task(new_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):

        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "finished" if task.completed else "not finished"
            print(f"ID: {task.id} Title: {task.title} Status: {status}")

    def update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                print("1. Change Title")
                print("2. Toggle Completion Status")
                choice = input("Choose option: ")

                if choice == "1":
                    new_title = input("Enter new title: ")
                    task.title = new_title
                elif choice == "2":
                    task.completed = not task.completed
                else:
                    print("Invalid option")
                    return
                self.save_tasks()
                print("Task updated successfully!")
                return
        print("Task not found.")
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully!")
                return
        print("Task not found.")
def final():
    app = TodoApp()
    while True:
        print("\n--- TODO APP ---")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            app.add_task(title)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            app.update_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            app.delete_task(task_id)
        elif choice == "5":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    final()
