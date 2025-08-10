from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3")
new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_session() -> AsyncSession:
    async with new_session() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_db_session)]


class Model(DeclarativeBase):
    pass

async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)