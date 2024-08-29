from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    pseudo = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    balance = Column(Float, default=0.0)
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    daily_reward_claimed = Column(Boolean, default=False)
    expiration_date = Column(DateTime, nullable=True)

    transfers = relationship("Transfer", back_populates="user")
    devices = relationship("Device", back_populates="user")
    ads = relationship("Ad", back_populates="user")


class Transfer(Base):
    __tablename__ = "transfer"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="transfers")


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Boolean, default=True)
    amount = Column(Float, nullable=False)
    link = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="ads")


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    ip = Column(String(255), nullable=False)
    bonner_token = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    uptime = Column(Float, default=0.0)
    status = Column(Boolean, default=True)

    user = relationship("User", back_populates="devices")
    works = relationship("Work", back_populates="device")


class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    id_device = Column(Integer, ForeignKey("devices.id"), nullable=False)
    uptime_amount = Column(Float, default=0.0)

    device = relationship("Device", back_populates="works")