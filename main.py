# main.py
# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, \
                     Field, EmailStr, HttpUrl

# FastAPI
from fastapi import FastAPI, Body, Query, Path


# Instance
app = FastAPI()


# -- Models --
# -- These models are for enum properties o characteristics
class Role(Enum):
    assassin = "assassin"
    fighter = "fighter"
    mage = "mages"
    markman = "markman"
    support = "support"
    tank = "tank"

class Difficulty(Enum):
    low = "low"
    moderate = "moderate"
    high = "high"

class Company(BaseModel):
    name: str = Field(
        ...,
        max_length=50
    )
    email: EmailStr
    website: HttpUrl

class Champion(BaseModel):
    # Field's Name  | Field's Type
    name: str = Field(
        ...,
        max_length=50
    )
    role: Role = Field(
        ...,
    )
    difficulty: Difficulty = Field(
        ...,
    )
    # Optional Field
    ultimate: Optional[str] = Field(
        default=None
    )

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

# Update LOL Champion using two instances
@app.put('/champs/update-champ/{champ_id}')
def update_champ(
    champ_id: int = Path(
        ...,
        title="Champ Id",
        description="Enter the champ's id"
    ),
    champion: Champion = Body(...),
    company: Company = Body(...)
):
    result = champion.dict()
    result.update(company.dict())
    return result

# Add new company
@app.post('/companies/new')
def create_company(
    company: Company = Body(...),
):
    return company


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
    return {"details": {"name": name, "role": role, "difficulty": difficulty}}

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
    return {"details": {"id": champ_id, "name": "example", "role": "example"}}