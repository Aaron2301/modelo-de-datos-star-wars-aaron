import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    user_name = Column(String(16), unique = True)
    gender=Column(String(50), nullable=False)
    dob= Column(DateTime(), nullable=False)
    email=Column(String (80), unique=True)
    date_added=Column(DateTime(), nullable=True)
    favorites= relationship('favorites', backref='user', uselist=True)
    favorite_id=Column(Integer, ForeignKey('favorite.id'), nullable=False)

class Favorite (Base):
    __tablename__= 'favorite'
    id=Column(Integer, primary_key=True)
    personaje_id=Column(Integer, ForeignKey('personaje.id'), nullable=False)
    planet_id=Column(Integer, ForeignKey('planet.id'), nullable=False)
    vehicle_id=Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    favorites=relationship('favorites', backref='user', uselist=True)

class Personaje(Base):
    __tablename__= 'personaje'
    id=Column(Integer, primary_key=True)
    name=Column(String(40), nullable=False)
    physical_features=Column(String(800), nullable=False)
    personality=Column(String(200), nullable=False)
    race=Column(String(50), nullable=False)
    age=Column(String(80), nullable=False)

class Planet(Base):
    __tablename__= 'planet'
    id=Column(Integer, primary_key=True)
    name=Column(String(50), nullable=False)
    atmosphere=Column(String(200), nullable=False)
    diameter=Column(String(200), nullable=False)
    dominant_breed=Column(String(60), nullable=False)
    location=Column(String(400), nullable=False)

class Vehicle(Base):
    __tablename__='vehicle'
    id=Column(Integer, primary_key=True)
    name=Column(String(70), nullable=False)
    type=Column(String(100), nullable=False)
    maker=Column(String(50), nullable=False)
    length=Column(String(80), nullable=False)
    crewmembers=Column(String(800), nullable=False)
    pilots=Column(String(200), nullable=False)



    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')