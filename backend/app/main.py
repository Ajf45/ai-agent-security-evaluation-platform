from fastapi import FastAPI
from app.api.routes import router
from app.core.database import engine, Base
from app.models import db_models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Agent Security Evaluation Platform")

app.include_router(router)