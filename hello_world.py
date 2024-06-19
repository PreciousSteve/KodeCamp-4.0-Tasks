# Create a simple API that returns a "Hello, World!" message when accessed.
from fastapi import FastAPI 

app = FastAPI()

@app.get("/greet")
def read():
    return {"Hello, world"}