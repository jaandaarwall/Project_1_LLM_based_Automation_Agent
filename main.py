# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "requests",
# ]
# ///


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class Task(BaseModel):
    task: str

@app.get("/")
async def print_hello():
    return {"message": "hello"}


@app.post("/run")
async def run_task(task: Task):
    file_name = task.task + ".txt"
    with open(file_name, "w") as f:
        f.write(f"Task {task.task} completed.")
    return {"message": f"Task {task.task} is being executed."}

@app.get("/read")
async def read_file(path: str):
    if os.path.exists(path):
        with open(path, "r") as f:
            return {"content": f.read()}
    return {"error": "File not found"}


if __name__ =='__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0',port=8000)

