# main.py
# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Query, Path


# Instance
app = FastAPI()


# -- Models --
class Champion(BaseModel):
    # Field's Name  | Field's Type
    name: str
    role: str
    difficulty: str
    # Optional Field
    ultimate: Optional[str] = None

# -- Paths --
# Path operation decorator init
@app.get('/')

#  Home
def home():
    return {"first": "practice"}


# Add new LOL champion
@app.post('/champs/new')
def create_champ(
    champion: Champion = Body(...),
):
    return champion


# Path operations
# -- Be careful with the path order --

# Query parameters
@app.get('/champs/detail')
def show_champ(
    # Query parameters always should be optionals
    # In this case, we expect a string field and its length should be smaller than 50.
    # Its defaul value is None.
    name: Optional[str] = Query(
        None,
        max_length=50,
        title = "Champ's name",
        description = "Enter the champ's name"
    ),
    # In this case, this query parameter is required
    role: Optional[str] = Query(
        ...,
        title = "Champ's role",
        description = "Enter the champ's role"
    ),
    difficulty: Optional[str] = Query(
        ...,
        title = "Champ's difficulty",
        description = "Enter the champ's difficulty"
    )
):
    return {'details': {'name': name, 'role': role, 'difficulty': difficulty}}

# Path parameters
@app.get('/champs/detail/{champ_id}')
def show_champ_by_id(
    # Example; gt equals greater than
    champ_id: int = Path(
        ...,
        gt=0,
        title = "Champ's id",
        description = "Enter the champ's id"
    )
):
    return {'details': {'id': champ_id, 'name': 'example', 'role': 'example'}}