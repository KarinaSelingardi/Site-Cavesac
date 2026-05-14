import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Volunteer(Base):
    __tablename__ = 'volunteers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

@st.cache_resource
def get_db_session():
    engine = create_engine('sqlite:///ong_volunteers.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()