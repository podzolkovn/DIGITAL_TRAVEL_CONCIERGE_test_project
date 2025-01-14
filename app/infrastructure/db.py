from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing_extensions import AsyncGenerator

from app.core.config import settings

Base = declarative_base()

engine = create_async_engine(
    url=settings.DB_URL
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
