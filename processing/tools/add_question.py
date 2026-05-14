
from ..bubblesheet_class import BubbleSheet, Project, Task


def add_question(bubblesheet):
    tasks = bubblesheet.project.tasks
    new_task_id = max((t.id for t in tasks), default=0) + 1
    answer = input("Enter answer for the question (A, B, C, D, E): ").upper()
    while answer not in ["A", "B", "C", "D", "E"]:
        print("Invalid answer. Please enter A, B, C, D, or E.")
        answer = input("Enter answer for the question (A, B, C, D, E): ").upper()
    
    new_task = Task(id=new_task_id, label="", answer=answer, notes="")
    bubblesheet.project.tasks.append(new_task)
    print(f"Question added: {new_task}")

"""
Adds a new question to the BubbleSheet object. The new question will have a unique ID that is one greater than the current maximum ID in the tasks list. The user is prompted to enter the answer for the new question, which must be one of A, B, C, D, or E. The new question is then appended to the tasks list in the BubbleSheet's project.
args: bubblesheet (BubbleSheet)
returns: None
"""