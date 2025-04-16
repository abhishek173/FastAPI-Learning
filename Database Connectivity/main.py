from fastapi import FastAPI
import models
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def hello():
    return {"hello", "world" }