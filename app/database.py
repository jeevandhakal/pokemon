from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = create_async_engine(settings.database_url, echo=settings.debug)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
