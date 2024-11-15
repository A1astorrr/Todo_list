from fastapi import APIRouter, Depends
from app.todo.dao import TodoDAO
from app.todo.schemas import Todo, TodoCreate, TodoDelete, TodoUpdate
from app.exceptions import NotDeletedById,TodoNotCreated, TodoNotUpdate


router = APIRouter(
    prefix="/todos",
    tags=["Список дел"],
)

@router.get("/id/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    return await TodoDAO.find_by_id(todo_id)

@router.get("/", response_model=list[Todo])
async def read_todos(skip: int = 0, limit: int = 100):
    todos = await TodoDAO.find_all()
    return todos[skip : skip + limit]
    
@router.post("/", response_model=TodoCreate)
async def create_todo(todo: TodoCreate):
    created =  await TodoDAO.add(**todo.dict())
    if created is None:
        raise TodoNotCreated
    return created

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    updated = await TodoDAO.update(todo_id, **todo_update.dict(exclude_unset=True))
    if updated is None:
        raise TodoNotUpdate
    return updated, {"message":"Запись успешно обновлена"}
    
@router.delete("/{todo_id}", response_model=TodoDelete)
async def delete_todo(todo_id: int):
    deleted = await TodoDAO.delete(id=todo_id)
    if deleted is None:
        raise NotDeletedById
    return {"message": "Запись удалена"}
    
