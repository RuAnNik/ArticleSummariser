import Server
from fastapi.testclient import TestClient
from Server import app 
import json

def test_root(): 
    assert Server.foo(1, 2) == 3

client = TestClient(app)

def test_root():
    response = client.get("/") 
    assert response.status_code == 200 
    assert response.json() == {"message": "Hello World"}
    
def test_predict():
    article_text = "Впрочем, иногда странам удаётся вести конфликты более мирным путём. Например, Канада и Дания не могут поделить маленький остров Ханс, который вы можете видеть на иллюстрации. Поэтому на острове ведётся Hans Island так называемая «интеллигентная война». Раз в несколько месяцев туда прибывают военно‑морские силы Канады, устанавливают на острове флаг своего государства, поглощают заранее оставленный противником на острове запас крепких напитков, отмечают взятие острова и с победой отбывают."
    data = {'text': article_text}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = client.post("/predict/", json=data, headers=headers) 
    assert response.status_code == 200 
    assert response.json() == {"summary": "Канада и Дания не могут поделить маленький остров Ханс, на котором ведётся «интеллигентная война». Впрочем, иногда странам удаётся вести конфликты более мирным путём."}