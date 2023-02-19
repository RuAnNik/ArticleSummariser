import json
import streamlit as st
import requests as rq

article_text = "Впрочем, иногда странам удаётся вести конфликты более мирным путём. Например, Канада и Дания не могут поделить маленький остров Ханс, который вы можете видеть на иллюстрации. Поэтому на острове ведётся Hans Island так называемая «интеллигентная война». Раз в несколько месяцев туда прибывают военно‑морские силы Канады, устанавливают на острове флаг своего государства, поглощают заранее оставленный противником на острове запас крепких напитков, отмечают взятие острова и с победой отбывают."
article_text = st.text_area(label= "Текст:", value=article_text, )
data = {'text': article_text}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

st.write("Краткое содержание:")
summary = rq.post("http://127.0.0.1:8000/predict/", data=json.dumps(data), headers=headers).json()["summary"]
st.write(summary)