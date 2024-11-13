from sqlalchemy import Table, Column, Integer, String,  MetaData, Boolean
from  sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

metadata_obj = MetaData()

class TodoItem(Base):
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title:Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)