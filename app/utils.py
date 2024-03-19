from models import db_models 
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def add_user_rate_to_db(db: Session, user_id: int, comic_id: int, value: float) -> None:
    existing_rating = db.query(db_models.Rating).filter_by(user_id=user_id, comic_id=comic_id).first()
    if existing_rating:
        existing_rating.value = value
    else:
        new_rating = db_models.Rating(comic_id=comic_id, user_id=user_id, value=value)
        db.add(new_rating)

    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise


def update_comic_rating(db: Session, comic_id: int) -> None:
    existing_comic = db.query(db_models.Comic).filter_by(id=comic_id).first()
    existing_comic_rating = db.query(db_models.Rating).filter_by(comic_id=comic_id).all()
    average_existing_comic_rating = sum([comic_rate.value for comic_rate in existing_comic_rating]) / len(existing_comic_rating)
    average_existing_comic_rating = round(average_existing_comic_rating, 2)
    if existing_comic:
        existing_comic.rating = average_existing_comic_rating
    else:
        new_comic = db_models.Comic(id=comic_id, rating=average_existing_comic_rating)
        db.add(new_comic)

    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise