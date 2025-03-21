from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
import secrets

# Create FastAPI instance
app = FastAPI()

# Basic auth setup
security = HTTPBasic()
USER_CREDENTIALS = {
    "admin": "admin"  # Simple in-memory username/password for demonstration
}

# In-memory database (list of items)
db = []

# Pydantic model for CRUD operations
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Dependency for authentication
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, USER_CREDENTIALS.get("admin", ""))
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return credentials.username

# Routes
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the FastAPI CRUD with Basic Auth"}

@app.post("/items/", response_model=Item, tags=["CRUD"])
def create_item(item: Item, username: str = Depends(authenticate)):
    # Check if item with same ID already exists
    if any(existing_item["id"] == item.id for existing_item in db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    db.append(item.dict())
    return item

@app.get("/items/", response_model=List[Item], tags=["CRUD"])
def read_items(username: str = Depends(authenticate)):
    return db

@app.get("/items/{item_id}", response_model=Item, tags=["CRUD"])
def read_item(item_id: int, username: str = Depends(authenticate)):
    for item in db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item, tags=["CRUD"])
def update_item(item_id: int, updated_item: Item, username: str = Depends(authenticate)):
    for index, item in enumerate(db):
        if item["id"] == item_id:
            db[index] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", tags=["CRUD"])
def delete_item(item_id: int, username: str = Depends(authenticate)):
    for index, item in enumerate(db):
        if item["id"] == item_id:
            del db[index]
            return {"message": f"Item with ID {item_id} deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', port=11001, reload=True)