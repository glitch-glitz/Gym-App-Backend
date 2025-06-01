from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
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
