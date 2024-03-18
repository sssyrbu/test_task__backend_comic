from fastapi import FastAPI
from models.schemas import Comic, User, Rating
import uvicorn


app = FastAPI()

    
@app.post("/api/ratings", summary="", response_model=dict)
def rate(comic_id: Comic, user_id: User):
    pass


@app.get("/api/comics/{comic_id}/rating/", summary="", response_model=dict)
def comic_rating(comic_id: Comic):
    pass


@app.get("/", response_model=dict)
def root():
    return {
        "message": "navigate to /api/docs"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)