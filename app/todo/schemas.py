from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False  
    
class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    

class Todo(TodoBase):
    message: str
    id: int
    
    model_config = ConfigDict(from_attributes=True)
    
class TodoDelete(BaseModel):
    message: str