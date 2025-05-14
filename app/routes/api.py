from fastapi import APIRouter
from app.controllers.user_controller import UserController
from app.schemas.user_schema import UserSchema

class Api:
    def __init__(self):
        self.controller = UserController()
        self.router = APIRouter()
        self.setup_routes()
        
    def setup_routes(self):
        @self.router.get("/user")
        def get_all_data():
            return self.controller.getAllData()
        
        @self.router.post("/user/create")
        def create_data(user: UserSchema):
            return self.controller.createData(user)
        
    def get_router(self):
        return self.router
    
api = Api().get_router()
        
