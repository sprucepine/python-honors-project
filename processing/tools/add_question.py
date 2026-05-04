
from ..bubblesheet_class import BubbleSheet, Project, Task


def add_question(bubblesheet):
    question_text = input("Enter the text for the new question: ")
    new_task_id = len(bubblesheet.project.tasks) + 1  # Simple way to generate a new task ID
    new_task = Task(id=new_task_id, label=question_text, answer="", notes="")
    bubblesheet.project.tasks.append(new_task)
    print(f"Question added: {new_task}")