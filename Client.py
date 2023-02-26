import json
import streamlit as st
import requests as rq

with open("config.json", "r", encoding="UTF8") as f:
    config = json.load(f)

article_text = config["article_text"]
article_text = st.text_area(
    label="Текст:",
    value=article_text,
)
data = {"text": article_text}
headers = {"Content-type": "application/json", "Accept": "text/plain"}

st.write("Краткое содержание:")
summary = rq.post(
    "http://127.0.0.1:8000/predict/", data=json.dumps(data), headers=headers
).json()["summary"]
st.write(summary)
