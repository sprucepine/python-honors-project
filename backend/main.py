from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from logic import get_items, process_data, save_items_order

app = FastAPI()


class TaskItem(BaseModel):
    id: int
    label: str


class ReorderPayload(BaseModel):
    items: list[TaskItem]

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8080"],  # Vite dev server ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/process")
def handle_request(text: str):
    # Just calls your logic function and returns the result
    return process_data(text)


@app.get("/api/tasks")
def fetch_tasks():
    return {"items": get_items()}


@app.post("/api/tasks/reorder")
def reorder_tasks(payload: ReorderPayload):
    try:
        updated_items = save_items_order([item.model_dump() for item in payload.items])
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"items": updated_items}