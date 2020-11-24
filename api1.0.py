# post请求
from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import en_core_web_sm
en_core_web_sm.load()

nlp = spacy.load("en_core_web_sm")
app = FastAPI()


@app.get('/test/a={a}/b={b}')
def calculate(a: int=None, b: int=None):
    c = a + b
    res = {"res":c}
    return res

@app.get('/')
def hello():
    return "Hello1"

class Item(BaseModel):
    POS: str = None


@app.post('/test')
def calculate(request_data: Item):
    if request_data.POS:
        doc =nlp(request_data.POS)
        result = {}
        for token in doc:
            result[token.text] = token.pos_
        return result
    return "error"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080,
                workers=1)
