from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import database, models, schemas
from .database import get_db
from .routers import authors, posts

# Создаём таблицы в БД (для теста, в продакшене лучше миграции)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Blog App")

templates = Jinja2Templates(directory="../templates")

# Подключаем роутеры
app.include_router(authors.router, prefix="/api/v1", tags=["authors"])
app.include_router(posts.router, prefix="/api/v1", tags=["posts"])

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

