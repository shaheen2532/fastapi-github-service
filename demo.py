from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_func():
    return {"Status": "OK! Server running"}

@app.get("/number/{num}")
def return_num(num: int, q: Union[str, None] = None):
    return {"number": num, "q": q}