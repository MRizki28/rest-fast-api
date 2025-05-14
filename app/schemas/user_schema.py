from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(..., max_length=50  )
    
    