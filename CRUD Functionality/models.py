from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    items = relationship("items", back_populates="owner")
    
class Item(Base):
    __tablename__="items"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String,index=True)
    owner_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("users", back_populates="items")
