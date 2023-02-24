class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        else:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name):
        for j in self.tasks:
            if j.name == task_name:
                j.completed = True
                return f'Completed task {task_name}'
        else:
            return f'Could not find task with the name {task_name}'

    def clean_section(self):
        tasks_count = 0

        for i in self.tasks:
            if i.completed:
                tasks_count += 1
                self.tasks.remove(i)

        return f"Cleared {tasks_count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"

        for i in self.tasks:
            result += "\n"
            result += i.details()

        return result