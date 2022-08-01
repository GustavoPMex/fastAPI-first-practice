# main.py
from fastapi import FastAPI

# Instancia de la clase FastAPI
app = FastAPI()

# Path operation decorator
@app.get("/")
# Path operation function
def home():
    return {"first": "practice"}