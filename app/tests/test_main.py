from fastapi.testclient import TestClient
from main import app, get_db
from .testdb import Base, engine, TestingSessionLocal


Base.metadata.create_all(bind=engine)

client = TestClient(app)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_rate_comic():
    response = client.post("/api/ratings", json={"comic_id": 1, "user_id": 1, "value": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Вы оценили комикс"
    assert data["user"] == 1
    assert data["comic"] == 1
    assert data["value"] == 5


# def test_get_comic_rating():
#     comic_id = 2
#     # imitate a comic rating
#     client.post("/api/ratings", json={"comic_id": comic_id, "user_id": 2, "value": 4.5})

#     response = client.get(f"/api/comics/{comic_id}/rating/")
#     assert response.status_code == 200
#     data = response.json()
#     assert "comic_rating" in data


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "message": "navigate to /api/docs"}
