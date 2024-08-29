from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    email                = Column(String(255), unique=True, index=True, nullable=False)
    username             = Column(String(255), unique=True, index=True, nullable=False)
    password             = Column(String(255), nullable=False)
    balance              = Column(Float, default=0.0)
    token                = Column(String(255), nullable=True)
    refresh_token        = Column(String(255), nullable=True)
    daily_reward_claimed = Column(Boolean, default=False)
    expiration_date      = Column(DateTime, nullable=True)
    is_admin             = Column(Boolean, default=False)
    is_banned            = Column(Boolean, default=False)
    created_at           = Column(DateTime, default=DateTime.utcnow)
    updated_at           = Column(DateTime, onupdate=DateTime.utcnow)
    experience           = Column(Integer, default=0)

    roblox_id            = Column(String(255), nullable=True)
    roblox_username      = Column(String(255), nullable=True)
    roblox_token         = Column(String(255), nullable=True)

    epic_games_id        = Column(String(255), nullable=True)
    epic_games_username  = Column(String(255), nullable=True)
    epic_games_token     = Column(String(255), nullable=True)

    # Relationships
    transfers            = relationship("Transfer", back_populates="user")
    devices              = relationship("Device", back_populates="user")
    ads                  = relationship("Ad", back_populates="user")
    studios              = relationship("Studio", back_populates="members")
    reviews              = relationship("Review", back_populates="user")
    orders               = relationship("Order", back_populates="user")



class Game(Base):
    __tablename__        = "games"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    name                 = Column(String(255), nullable=False)
    description          = Column(String(255), nullable=False)
    image_url            = Column(String(255), nullable=False)
    link                 = Column(String(255), nullable=False)
    rating               = Column(Float, nullable=False)

    # Relationships
    studio               = relationship("Studio", back_populates="games")
    
class Studio(Base):
    __tablename__        = "studios"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    name                 = Column(String(255), nullable=False)
    description          = Column(String(255), nullable=False)
    image_url            = Column(String(255), nullable=False)
    link                 = Column(String(255), nullable=False)
    rating               = Column(Float, nullable=False)
    color                = Column(String(255), nullable=False)

    # Relationships
    games                = relationship("Game", back_populates="studio")
    ads                  = relationship("Ad", back_populates="studio")
    admins               = relationship("User", back_populates="studios")


class Review(Base):
    __tablename__        = "reviews"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    id_user              = Column(Integer, ForeignKey('users.id'))
    id_game              = Column(Integer, ForeignKey('games.id'))
    rating               = Column(Float, nullable=False)
    content              = Column(String(255), nullable=False)

    # Relationships
    user                 = relationship("User", back_populates="reviews")
    game                 = relationship("Game", back_populates="reviews")


class Product(Base):
    __tablename__        = "products"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    name                 = Column(String(255), nullable=False)
    description          = Column(String(255), nullable=False)
    image_url            = Column(String(255), nullable=False)
    price                = Column(Float, nullable=False)
    stock                = Column(Integer, nullable=False)

    # Relationships
    orders               = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__        = "orders"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    id_user              = Column(Integer, ForeignKey('users.id'))
    id_product           = Column(Integer, ForeignKey('products.id'))
    date                 = Column(DateTime, nullable=False)
    quantity             = Column(Integer, nullable=False)
    type                 = Column(String(255), nullable=False)

    # Relationships
    user                 = relationship("User", back_populates="orders")
    product              = relationship("Product", back_populates="orders")


class Ad(Base):
    __tablename__ = "ads"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    id_user              = Column(Integer, ForeignKey("users.id"), nullable=False)
    id_game              = Column(Integer, ForeignKey("games.id"), nullable=True)
    id_studio            = Column(Integer, ForeignKey("studios.id"), nullable=True)
    status               = Column(Boolean, default=True)
    amount               = Column(Float, nullable=False)
    link                 = Column(String(255), nullable=False)
    title                = Column(String(255), nullable=False)
    image_url            = Column(String(255), nullable=True)
    start_date           = Column(DateTime, nullable=False)
    end_date             = Column(DateTime, nullable=True)

    # Relationships
    user                 = relationship("User", back_populates="ads")
    game                 = relationship("Game", back_populates="ads")
    studio               = relationship("Studio", back_populates="ads")


class Device(Base):
    __tablename__        = "devices"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    id_user              = Column(Integer, ForeignKey("users.id"), nullable=False)
    ip                   = Column(String(255), nullable=False)
    bonner_token         = Column(String(255), nullable=True)
    name                 = Column(String(255), nullable=False)
    uptime               = Column(Float, default=0.0)
    status               = Column(Boolean, default=True)

    # Relationships
    user                 = relationship("User", back_populates="devices")
    works                = relationship("Work", back_populates="device")


class Work(Base):
    __tablename__        = "works"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    date                 = Column(DateTime, nullable=False)
    id_device            = Column(Integer, ForeignKey("devices.id"), nullable=False)
    uptime_amount        = Column(Float, default=0.0)

    # Relationships
    device               = relationship("Device", back_populates="works")