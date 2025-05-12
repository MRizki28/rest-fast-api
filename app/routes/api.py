from fastapi import APIRouter
from app.controllers.user_controller import UserController
class Api:
    def __init__(self):
        self.controller = UserController()
        self.router = APIRouter()
        self.setup_routes()
        
    def setup_routes(self):
        @self.router.get("/user")
        def get_all_data():
            return self.controller.getAllData()
        
    def get_router(self):
        return self.router
    
api = Api().get_router()
        
