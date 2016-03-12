# Imports for this project
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

# Declaring the User global variable
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

# Declaring the Brand global variable
class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


# Declaring the Item global variable
class Item(Base):
    __tablename__ = 'item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    image = Column(String(250))
    brand = relationship(Brand, cascade="delete")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, cascade="delete")
    

# Function to serialize Data for JSON and XML output 
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'image': self.image,
            'brand_id': self.brand_id,
            'user_id': self.user_id
        }

# Naming the DB file
engine = create_engine('postgresql://catalog:password@localhost/brands')


Base.metadata.create_all(engine)