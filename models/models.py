# Importation des modules
from sqlalchemy        import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Table, Enum
from sqlalchemy.orm    import relationship
from app.core.database import Base
from datetime          import datetime
from datetime          import datetime, timezone
from enum              import Enum as PyEnum


# Définir une énumération Python pour les statuts AD
class AdStatus(PyEnum):
    PENDING     = "pending"
    IN_PROGRESS = "in_progress"
    REJECTED    = "rejected"
    PAUSED      = "paused"
    TERMINATED  = "terminated"


# Table d'association pour la relation many-to-many
association_table = Table(
    'association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('studio_id', Integer, ForeignKey('studios.id')),
    Column('game_id', Integer, ForeignKey('games.id'))
)



###########################################################
#                       USER                              #
###########################################################
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
    created_at           = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at           = Column(DateTime, onupdate=datetime.now(timezone.utc))
    experience           = Column(Integer, default=0)

    roblox_id            = Column(String(255), nullable=True)
    roblox_username      = Column(String(255), nullable=True)
    roblox_token         = Column(String(255), nullable=True)

    epic_games_id        = Column(String(255), nullable=True)
    epic_games_username  = Column(String(255), nullable=True)
    epic_games_token     = Column(String(255), nullable=True)

    # Relationships
    orders               = relationship("Order", back_populates="user")
    devices              = relationship("Device", back_populates="user")
    ads                  = relationship("Ad", back_populates="user")
    reviews              = relationship("Review", back_populates="user")
    orders               = relationship("Order", back_populates="user")
    studios              = relationship("Studio", secondary=association_table, back_populates="admins")



###########################################################
#                       GAME                              #
###########################################################
class Game(Base):
    __tablename__ = "games"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    image_url = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    rating = Column(Float, nullable=False)

    visits = Column(Integer, default=0)
    plays = Column(Integer, default=0)
    ratings = Column(Integer, default=0)

    # Ajout de la clé étrangère pour lier à la table studios
    studio_id = Column(Integer, ForeignKey('studios.id'))

    # Relation avec Studio
    studio = relationship("Studio", back_populates="games")
    ads = relationship("Ad", back_populates="game")
    reviews = relationship("Review", back_populates="game")


###########################################################
#                       STUDIO                            #
###########################################################
class Studio(Base):
    __tablename__ = "studios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(800), nullable=False)
    image_url = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    rating = Column(Float, nullable=False)
    color = Column(String(255), nullable=False)

    # Clé étrangère vers User (créateur)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Relation inverse avec Game
    games   = relationship("Game", back_populates="studio")
    admins  = relationship("User", secondary=association_table, back_populates="studios")
    creator = relationship("User")  # Pour représenter le créateur



###########################################################
#                      REVIEW                             #
###########################################################
class Review(Base):
    __tablename__        = "reviews"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    user_id              = Column(Integer, ForeignKey('users.id'))
    id_game              = Column(Integer, ForeignKey('games.id'))
    id_ad                = Column(Integer, ForeignKey('ads.id'))
    rating               = Column(Float, nullable=False)
    content              = Column(String(500), nullable=False)

    # Relationships
    user                 = relationship("User", back_populates="reviews")
    game                 = relationship("Game", back_populates="reviews")
    ad                   = relationship("Ad", back_populates="reviews")


###########################################################
#                      PRODUCT                            #
###########################################################
class Product(Base):
    __tablename__        = "products"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    name                 = Column(String(255), nullable=False)
    description          = Column(String(255), nullable=False)
    image_url            = Column(String(255), nullable=False)
    price                = Column(Float, nullable=False)
    stock                = Column(Integer, nullable=False)
    currency             = Column(String(255), nullable=False)

    # Relationships
    orders               = relationship("Order", back_populates="product")



###########################################################
#                      ORDER                              #
###########################################################
class Order(Base):
    __tablename__        = "orders"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    user_id              = Column(Integer, ForeignKey('users.id'))
    id_product           = Column(Integer, ForeignKey('products.id'))
    date                 = Column(DateTime, nullable=False)
    type                 = Column(String(255), nullable=False)

    # Relationships
    user                 = relationship("User", back_populates="orders")
    product              = relationship("Product", back_populates="orders")



###########################################################
#                        AD                               #
###########################################################
class Ad(Base):
    __tablename__ = "ads"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    status = Column(Enum(AdStatus), nullable=False, default=AdStatus.PENDING)
    amount = Column(Float, nullable=False)
    link = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=True)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, nullable=True)

    plays   = Column(Integer, default=0)
    views   = Column(Integer, default=0)
    visits  = Column(Integer, default=0)
    ratings = Column(Integer, default=0)


    # Relationships
    user = relationship("User", back_populates="ads")
    game = relationship("Game", back_populates="ads")
    reviews = relationship("Review", back_populates="ad")



###########################################################
#                      DEVICE                             #
###########################################################
class Device(Base):
    __tablename__        = "devices"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    user_id              = Column(Integer, ForeignKey("users.id"), nullable=False)
    ip                   = Column(String(255), nullable=False)
    bonner_token         = Column(String(255), nullable=True)
    name                 = Column(String(255), nullable=False)
    uptime               = Column(Float, default=0.0)
    status               = Column(Boolean, default=True)

    # Relationships
    user                 = relationship("User", back_populates="devices")
    works                = relationship("Work", back_populates="device")



###########################################################
#                       WORK                              #
###########################################################
class Work(Base):
    __tablename__        = "works"

    # Columns
    id                   = Column(Integer, primary_key=True, index=True)
    date                 = Column(DateTime, nullable=False)
    id_device            = Column(Integer, ForeignKey("devices.id"), nullable=False)
    uptime_amount        = Column(Float, default=0.0)

    # Relationships
    device               = relationship("Device", back_populates="works")