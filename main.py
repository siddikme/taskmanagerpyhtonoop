from datetime import datetime

database = []
class User:
    id_counter = 0 

    def __init__(self, user, task_name, due_date, description, is_done=False):
        User.id_counter += 1
        self.id = User.id_counter
        self.user = user
        self.task_name = task_name
        self.due_date = due_date
        self.description = description
        self._is_done = is_done

    def __str__(self):
        return f"description: {self.description} Due-date: {self.due_date} task: {self.task_name} complaited: {self._is_done}"

class Usermanager:
    def register(self):
        username = input("Username: ") 
        task_name = input("Task name: ")
        due_date = input("Due date: ")
        description = input("Description: ")
        new_task = User(username, task_name, due_date, description)
        database.append(new_task)
        print(f"Task added for user '{username}'")

    def login(self):
        username = input("Enter your username: ")
        user_tasks = [task for task in database if task.user == username]
        
        if user_tasks:
            print(f"Tasks for user '{username}':")
            for task in user_tasks:
                print(task)
        else:
            print(f"No tasks found for '{username}'")

    def get_task_by_id(self, id):
        for task in database:
            if task.id == id:
                return task
       

    def get_all_tasks(self):
        for task in database:
            print(task)

    def edit_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            task.task_name = input("New task name: ")
            task._is_done = True
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            database.remove(task)
            print("Task deleted successfully.")
        else:
            print("Task not found.")

obj = Usermanager()

while True:
    user_input = int(input("1. Add a task\n2. Login to view tasks\n3. Show all tasks\n4. Edit task by ID\n5. Delete task by ID\n6. Exit\nChoose an option: "))
    if user_input == 1:
        obj.register()
    elif user_input == 2:
        obj.login()
    elif user_input == 3:
        obj.get_all_tasks()
    elif user_input == 4:
        obj.edit_task(int(input("Please enter task id to edit: ")))
    elif user_input == 5:
        obj.delete_task(int(input("Please enter task id to delete: ")))
    elif user_input == 6:
        print("Exiting.")
        break
    else:
        print("Please enter a number between 1 and 6.")
