from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the Drinks Table
class Drink(Base):
    __tablename__ = 'drinks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    main_category = Column(String, nullable=False)
    sub_category = Column(String, nullable=True)
    description = Column(String, nullable=True)  # Description of the drink
    price_glass = Column(Float, nullable=True)  # Price per glass
    price_bottle = Column(Float, nullable=True)  # Price per bottle


DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

