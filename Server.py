from fastapi import FastAPI
from transformers import AutoTokenizer, T5ForConditionalGeneration
from pydantic import BaseModel

app = FastAPI()


model_name = "IlyaGusev/rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


class Article(BaseModel):
    text: str


@app.post("/predict/")
async def predict(article: Article):
    input_ids = tokenizer(
        [article.text],
        max_length=600,
        add_special_tokens=True,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(input_ids=input_ids, no_repeat_ngram_size=4)[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return {"summary": summary}


@app.get("/")
async def root():
    return {"message": "Hello World"}


def foo(a, b):
    return a + b
