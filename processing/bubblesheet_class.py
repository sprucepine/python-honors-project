from pathlib import Path
from pydantic import BaseModel
from typing import List
import json

class Task(BaseModel):
    id: int
    label: str
    answer: str
    notes: str

class Project(BaseModel):
    name: str
    tasks: List[Task]

class BubbleSheet(BaseModel):
    format: str
    version: int
    exportedAt: str
    project: Project

# Load & Save (2 lines!)
def load_bubblesheet(filename: str) -> BubbleSheet:
    filename = Path(filename).stem
    with open(f'data/{filename}.bubblesheet', 'r') as file:
        return BubbleSheet.model_validate_json(file.read())
    # open(f'data/{filename}.bubblesheet', 'w').write(bubblesheet.model_dump_json(indent=2))