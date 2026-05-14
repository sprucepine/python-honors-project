def show_questions(bubblesheet):
    for task in bubblesheet.project.tasks:
        print(f"Question {task.id+1}: {task.answer}")
"""
displays questions from a bubblesheet
args: bubblesheet (BubbleSheet)
returns: None
"""