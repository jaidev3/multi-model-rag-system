from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import aiosqlite

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./database.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    try:
        async with SessionLocal() as db:
            yield db
            print("Database connection established")
    except Exception as e:
        print(f"Database connection failed: {e}")
        await db.rollback()
    finally:
        await db.close()
        print("Database connection closed")

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("All tables created")
