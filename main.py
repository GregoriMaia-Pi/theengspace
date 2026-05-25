from fastapi import FastAPI
from database import engine
from models import Base
from requirements.requirement_routes import router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "TheEngSpace API is running"}