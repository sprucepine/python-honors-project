def normalize_ids(bubblesheet):
    index = 0
    for task in bubblesheet.project.tasks:
        task.id = index
        index += 1
    return bubblesheet

"""
Normalizes task IDs in a BubbleSheet object to be sequential starting from 0. Many inputs from Bubblesheets on the Web may have non-sequential or duplicate IDs, which can cause issues when adding new questions. This function ensures that all task IDs are unique and sequential.
args: bubblesheet (BubbleSheet)
returns: BubbleSheet with normalized task IDs"""