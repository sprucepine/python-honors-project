from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logic import process_data

app = FastAPI()

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