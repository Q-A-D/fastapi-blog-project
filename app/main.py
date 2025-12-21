from fastapi import FastAPI
from . import database, models
from .routers import authors, posts

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Blog App")
app.include_router(authors.router, prefix="/api/v1", tags=["authors"])
app.include_router(posts.router, prefix="/api/v1", tags=["posts"])
