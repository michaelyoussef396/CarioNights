from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
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

# Define the Shisha Table
class Shisha(Base):
    __tablename__ = 'shisha'
    
    id = Column(Integer, primary_key=True)
    head_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Define the Flavor Table
class Flavor(Base):
    __tablename__ = 'flavors'
    
    id = Column(Integer, primary_key=True)
    shisha_id = Column(Integer, ForeignKey('shisha.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    extra_price = Column(Float, nullable=False)
    
    shisha = relationship("Shisha", back_populates="flavors")

Shisha.flavors = relationship("Flavor", order_by=Flavor.id, back_populates="shisha")

DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

