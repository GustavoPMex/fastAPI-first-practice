# main.py
# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Query


# Instance
app = FastAPI()


# -- Models --
class Champion(BaseModel):
    # Field's Name  | Field's Type
    name: str
    role: str
    difficulty: str
    # Optional Field
    ultimate: Optional[bool] = None

# -- Paths --
# Path operation decorator init
@app.get('/')

#  Home
def home():
    return {"first": "practice"}

# Get LOL champion
@app.get('/champs/{champ_id}')
async def get_champ(champ_id: int):
    return {"champ_id": champ_id}

# Add new LOL champion
@app.post('/champs/new')
def create_champ(champion: Champion = Body(...)):
    return champion


# Query parameters
@app.get('/champs/detail')
def show_champ(
    # Query parameters always should be optionals
    # In this case, we expect a string field and its length should be smaller than 50.
    # Its defaul value is None.
    name: Optional[str] = Query(None, max_length=50),
    # In this case, this query parameter is required
    role: Optional[str] = Query(...)
):
    return {name: role}