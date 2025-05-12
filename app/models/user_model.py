from app.config.database import Base 
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__ = "tb_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    email = Column(String(50),  index=True, nullable=False)
    