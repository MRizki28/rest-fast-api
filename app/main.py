# app/main.py

from fastapi import FastAPI
from app.config.database import DB_URL
from app.routes.api import api
import uvicorn

class App:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()
        self.log_database_url()

    def setup_routes(self):
        self.app.include_router(api, prefix="/api/v1")
        @self.app.get("/")
        def read_root():
            return {"message": "Server is running"}
        

    def log_database_url(self):
        print(f"DB_URL: {DB_URL}")

def get_app():
    return App().app

app = get_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8888)
