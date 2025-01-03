from sqlalchemy import select
from db.db import sessionDep, Tasks
from schemas.schemas import STaskAdd

async def create_task(task: STaskAdd, session: sessionDep):
    new_task = Tasks(
        name=task.name,
        description=task.description
    )
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)

    return {"Success": 200,
            "Message": "Task has successfully created!"}

async def get_tasks(session: sessionDep):
    query = select(Tasks)
    res = await session.execute(query)
    tasks = res.scalars().all()
    return tasks