from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os
from datetime import datetime

Base = declarative_base()

# Define the Drinks Table
class Drink(Base):
    __tablename__ = 'drinks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    main_category = Column(String, nullable=False)
    sub_category = Column(String, nullable=True)
    description = Column(String, nullable=True)  
    price_glass = Column(Float, nullable=True)  
    price_bottle = Column(Float, nullable=True)

class Food(Base):
    __tablename__ = 'foods'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    main_category = Column(String, nullable=False)
    sub_category = Column(String, nullable=True)
    description = Column(String, nullable=True)  
    price = Column(Float, nullable=False)

# Define the ShishaHead Table
class ShishaHead(Base):
    __tablename__ = 'shisha_heads'
    
    id = Column(Integer, primary_key=True)
    head_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Define the ShishaFlavor Table
class ShishaFlavor(Base):
    __tablename__ = 'shisha_flavors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    extra_price = Column(Float, nullable=False)

# Define the Reservation Table
class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    table_number = Column(Integer, ForeignKey('restaurant_tables.id'), nullable=False)
    table = relationship("RestaurantTable", back_populates="reservations")

# Define the RestaurantTable Table
class RestaurantTable(Base):
    __tablename__ = 'restaurant_tables'
    
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    table_number = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)
    
    orders = relationship("Order", back_populates="table")
    payment_requests = relationship("PaymentRequest", back_populates="table")
    reservations = relationship("Reservation", back_populates="table")



class RestaurantEmployee(Base):
    __tablename__ = 'restaurant_employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_working = Column(Boolean, default=True)

# Define the Waiting List Table
class WaitingList(Base):
    __tablename__ = 'waiting_list'
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    num_people = Column(Integer, nullable=False)
    reason = Column(String, nullable=False, server_default='Seating')
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default='Waiting')

# Define the Feedback Table
class Feedback(Base):
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    feedback = Column(String, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, ForeignKey('restaurant_tables.id'), nullable=False)
    item_type = Column(String, nullable=False)  # 'ShishaHead', 'Drink', or 'Food'
    item_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1)
    timestamp = Column(DateTime, default=datetime.utcnow)

    table = relationship("RestaurantTable", back_populates="orders")

# Database configuration
dirname = os.path.dirname(__file__)
DATABASE_URL = f"sqlite:///{dirname}/cario_nights.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
