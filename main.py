from router import router as tasks_router
from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager


import database as db
import storage

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.delete_tables()
    print("База очищена")
    await db.create_tables()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)





if __name__ == "__main__":
    run("main:app", port=8001, reload=True)