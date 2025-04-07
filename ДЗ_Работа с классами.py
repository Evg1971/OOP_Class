class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": False})

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = True
                return
        print(f"Задача '{task}' не найдена")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                return
        print(f"Задача '{task}' не обнаружена")

    def list_tasks(self):
        for t in self.tasks:
            status = "[x]" if t['status'] else "[ ]"
            print(f"{t['task']} - {status}")


todo = ToDoList()
todo.add_task("Купить телефон")
todo.add_task("Прочитать книгу 'Классы в Python'")
todo.add_task("Зарегистрироваться на 'HH.ru'")
todo.add_task("Записаться на 5 собеседований")
todo.add_task("Посетить 5 собеседований")
todo.list_tasks()
print()
todo.complete_task("Купить телефон")
todo.complete_task("Прочитать книгу 'Классы в Python'")
todo.list_tasks()
print()
todo.remove_task("Купить телефон")
todo.list_tasks()
print()
todo.complete_task("Несуществующая задача")
todo.remove_task("No task")