from fastapi import FastAPI
from api.auth import router as auth_router
from db.database import engine
from models import users

users.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)