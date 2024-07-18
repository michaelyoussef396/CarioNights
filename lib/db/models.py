from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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

# Define the Customer Table
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Define the Reservation Table
class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    table_number = Column(Integer, ForeignKey('restaurant_tables.id'), nullable=False)

# Define the Restaurant Table
class RestaurantTable(Base):
    __tablename__ = 'restaurant_tables'
    
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    table_number = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)

class RestaurantEmployee(Base):
    __tablename__ = 'restaurant_employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_working = Column(Boolean, default=True)

DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

