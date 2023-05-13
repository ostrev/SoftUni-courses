from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for s_task in self.tasks:
            if s_task.name == new_task.name:
                return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for c_task in self.tasks:
            if c_task.name == task_name:
                c_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for cc_task in self.tasks:
            if cc_task.completed:
                count += 1
                self.tasks.remove(cc_task)
        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for v_task in self.tasks:
            result += '\n' + v_task.details()

        return result

