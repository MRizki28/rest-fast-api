from app.services.user_service import UserService
from app.config.database import SessionLocal
from app.schemas.user_schema import UserSchema

class UserController:
    def __init__(self):
        self.user_service = UserService(SessionLocal())

    def getAllData(self):
        data = self.user_service.getAllData()
        return data
    
    def createData(self, user: UserSchema):
        data = self.user_service.createData(user)
        return data