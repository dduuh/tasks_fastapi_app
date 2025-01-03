from fastapi import FastAPI
from db.db import drop_tables, create_tables
from contextlib import asynccontextmanager
from routes.tasks import task
from routes.users import user

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('DB is cleared')
    await create_tables()
    print('DB is ready to work')
    yield
    print('Disconnected')

app = FastAPI(lifespan=lifespan, docs_url='/docs')

app.include_router(
    task,
    prefix='/api',
    tags=['Tasks']
)

app.include_router(
    user,
    prefix='/api',
    tags=['Users']
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
