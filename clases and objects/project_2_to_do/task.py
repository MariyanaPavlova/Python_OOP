from project_2_to_do.section import Section

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comment = []
        self.completed = False

    def change_name(self, new_name):
        if self.name != new_name:
            self.name = new_name
            return f'{self.name}'
        else:
            return f"Name cannot be the same."

    def change_due_date(self, new_date):
        if self.due_date != new_date:
            self.due_date = new_date
            return f'{self.due_date}'
        else:
            return f"Date cannot be the same."

    def add_comment(self, comment):
        self.comment.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if len(self.comment) > comment_number:
            self.comment[comment_number] = new_comment
            return f'{"".join(self.comment)}'
        else:
            return f'Cannot find comment.'

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")

print(section.add_task(task))

second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())