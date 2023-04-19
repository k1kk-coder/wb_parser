from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker
from config import db_host, db_name, db_pass, db_port, db_user


DATABASE_URL: str = (f"postgresql+asyncpg://"
                     f"{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
Base: DeclarativeMeta = declarative_base()


engine: AsyncEngine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
