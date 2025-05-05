from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
model = pipeline("sentiment-analysis", model="model/")


class InputText(BaseModel):
    text: str


@app.post("/predict")
def predict(input: InputText):
    result = model(input.text)[0]
    return {"label": result["label"], "score": result["score"]}
