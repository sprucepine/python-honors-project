from fastapi import FastAPI
from logic import process_data

app = FastAPI()

@app.get("/api/process")
def handle_request(text: str):
    # Just calls your logic function and returns the result
    return process_data(text)