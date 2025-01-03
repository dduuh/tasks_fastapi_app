from sqlalchemy import select
from db.db import sessionDep, Users
from schemas.schemas import SUsersAdd

async def get_users(session: sessionDep):
    query = select(Users)
    res = await session.execute(query)
    users = res.scalars().all()
    return users

async def create_user(user: SUsersAdd, session: sessionDep):
    new_user = Users(
        username=user.username,
        password=user.password
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return {"Success": 200, "Message": "New user created!"}