def show_questions(bubblesheet):
    questions = []
    for task in bubblesheet.project.tasks:
        questions.append(f"Question {task.id}: {task.label}")
"""
displays questions from a bubblesheet
args: bubblesheet (BubbleSheet)
returns: questions (list of str)
"""