from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from fastapi.responses import JSONResponse
from app.schemas.user_schema import UserSchema
class UserService:
    def __init__(self, db: Session):
        self.db = db

    def getAllData(self):
        data = self.db.query(UserModel).all()
        if not data:
            return JSONResponse(
                content={"status": "not found", "message": "Data not found"}, 
                status_code=404
            )
            
        return {
            "status": "success",
            "message": "Success get all data",
            "data": data
        }, 
    
    
    def createData(self, user: UserSchema):
        try:
            new_user = UserModel(
                name=user.name,
                email=user.email
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return {
                "status": "success",
                "message": "Success create data",
                "data": new_user
            }
        except Exception as e:
            return JSONResponse(
                content={"status": "failed", "message": str(e)}, 
                status_code=500
            )
        except Exception as e:
            raise e
    
    
    
