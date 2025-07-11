# обновляем код main.py
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# новый маршрут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}
