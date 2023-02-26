import Server
from fastapi.testclient import TestClient
from Server import app
import json

with open("config.json", "r", encoding="UTF8") as f:
    config = json.load(f)


def test_foo():
    assert Server.foo(1, 2) == 3


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict():
    article_text = config["test_article_text"]
    data = {"text": article_text}
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    response = client.post("/predict/", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"summary": config["test_summary_text"]}
