from app.dao.base import BaseDAO
from app.todo.models import Todo
from app.database import async_session_maker


class TodoDAO(BaseDAO):
    model = Todo
    
    @classmethod
    async def update(cls, todo_id: int, **data):
        async with async_session_maker() as session:
            todo_item = await cls.find_by_id(todo_id)
            if todo_item is None:
                return None
            
            for key, value in data.items():
                setattr(todo_item, key, value)
                
            session.add(todo_item)
            await session.commit()
            return todo_item
            