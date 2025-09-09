from database.db import create_all_tables
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from routes import rag_router

load_dotenv()

app = FastAPI()



@app.on_event("startup")
async def startup_event():
    await create_all_tables()
    print("All tables created")

app.include_router(rag_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
