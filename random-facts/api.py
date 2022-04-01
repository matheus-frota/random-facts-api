from random import randint
from uuid import uuid1

from fastapi import FastAPI

app = FastAPI()

facts = ['In 1897, Indiana state legislators tried to pass a bill that would have legally redefined the value of pi as 3.2.',
         'F. Scott Fitzgerald\'s full name is Francis Scott Key Fitzgerald. He was named after his distant relative Francis Scott Key, who wrote the words to "The Star-Spangled Banner."',
         'St. Patrick wasn\'t Irish: He was born to Roman parents in either Scotland, England, or Wales.'
         ]

@app.get('/')
def home():
    return """Olá, você está utilizando a API geradora de fatos
    reais... Ou será que não?
    """


@app.get('/facts')
def show_facts():
    return {
        "uuid": uuid1(),
        "content": facts[randint(0, 2)]
    }
