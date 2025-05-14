from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

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
    
    
    
