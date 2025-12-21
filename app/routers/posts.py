from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/posts", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/posts", response_model=list[schemas.PostResponse])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).offset(skip).limit(limit).all()
    return posts

@router.get("/posts/{post_id}", response_model=schemas.PostResponse)
def read_post(post_id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
