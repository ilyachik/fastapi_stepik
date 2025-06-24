# обновляем код main.py
from fastapi import FastAPI

from app.config import load_config
from app.logger import logger


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# новый маршрут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


# main.py (продолжение)


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}


config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False
