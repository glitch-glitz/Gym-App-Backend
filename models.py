from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, create_engine, Text
# from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime


# 1. create an engine that connects to our db
engine = create_engine('sqlite:///gym-app.db', echo = True)

# 2. create a session
Session = sessionmaker(bind=engine)

# 3. for fastapi, we need to create a method/function that returns the session
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()


Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    passport = Column(Text)
    weight = Column(Float, nullable=True)
    bmi = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    # subscriptions = relationship('Subscription', back_populates='member', cascade="all, delete-orphan")
    # check_ins = relationship('CheckIn', back_populates='member', cascade="all, delete-orphan")


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    plan_name = Column(String, nullable=False)  # e.g., "Monthly", "Annual"
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    # member = relationship('Member', back_populates='subscriptions')


class CheckIn(Base):
    __tablename__ = 'check_ins'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    check_in_time = Column(DateTime, default=datetime.utcnow)

    # member = relationship('Member', back_populates='check_ins')