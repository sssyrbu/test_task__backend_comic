from database import Base, SessionLocal, engine
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils import add_user_rate_to_db, update_comic_rating, fetch_comic_rating
import uvicorn


Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/api/ratings", summary="Оценить комикс", response_model=dict)
def rate(comic_id: int, user_id: int, value: int | float, db: Session = Depends(get_db)):
    if (value < 1) or (value > 5):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Оценка комикса должна быть от 1 до 5."
        )
    add_user_rate_to_db(db, user_id, comic_id, value)
    update_comic_rating(db, comic_id)
    return {
        "message": "Вы оценили комикс",
        "user": user_id,
        "comic": comic_id,
        "value": value
    }


@app.get("/api/comics/{comic_id}/rating/", summary="Узнать рейтинг комикса", response_model=dict)
def get_comic_rating(comic_id: int, db: Session = Depends(get_db)):
    comic_rating = fetch_comic_rating(db, comic_id)
    if comic_rating:
        return {"comic_rating": comic_rating}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Комикса с данным айди не существует"
        )


@app.get("/", response_model=dict)
def root():
    return {
        "message": "navigate to /api/docs"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)