
from ..bubblesheet_class import BubbleSheet, Project, Task


def add_question(bubblesheet):
    print(max(bubblesheet.project.tasks))
    new_task_id = len(bubblesheet.project.tasks) + 1  # Simple way to generate a new task ID
    answer = input("Enter answer for the question (A, B, C, D, E): ").upper()
    while answer not in ["A", "B", "C", "D", "E"]:
        print("Invalid answer. Please enter A, B, C, D, or E.")
        answer = input("Enter answer for the question (A, B, C, D, E): ").upper()
    
    new_task = Task(id=new_task_id, label="", answer=answer, notes="")
    bubblesheet.project.tasks.append(new_task)
    print(f"Question added: {new_task}")