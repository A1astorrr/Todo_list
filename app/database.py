import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,  # при true позволяет видеть все запросы в консоли
    # pool_size=5, # кол-во подключений к бд
    # max_overflow=10, # доп. слоты для подключения
)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class  Base(DeclarativeBase):
    pass