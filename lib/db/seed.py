from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Drink

# Database setup
DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_drink(name, main_category, sub_category=None, description=None, price_glass=None):
    drink = Drink(
        name=name, 
        main_category=main_category, 
        sub_category=sub_category, 
        description=description, 
        price_glass=price_glass
    )
    session.add(drink)
    session.commit()

def seed_drinks():
    # Juices
    add_drink("Mango Juice", "Cold Drinks", "Juices", "A refreshing tropical drink made from ripe mangoes.", 10.0)
    add_drink("Pineapple Juice", "Cold Drinks", "Juices", "A sweet and tangy juice made from fresh pineapples.", 8.0)
    add_drink("Orange Juice", "Cold Drinks", "Juices", "A classic and zesty juice made from freshly squeezed oranges.", 8.0)
    add_drink("Guava Juice", "Cold Drinks", "Juices", "A delicious and exotic juice made from ripe guavas.", 10.0)
    
    # Milkshakes
    add_drink("Strawberry Milkshake", "Cold Drinks", "Milkshakes", "A creamy milkshake made with fresh strawberries and ice cream.", 10.0)
    add_drink("Caramel Milkshake", "Cold Drinks", "Milkshakes", "A rich and indulgent milkshake with caramel syrup and ice cream.", 10.0)
    add_drink("Chocolate Milkshake", "Cold Drinks", "Milkshakes", "A decadent milkshake made with chocolate syrup and ice cream.", 10.0)
    
    # Other Cold Drinks
    add_drink("Iced Coffee", "Cold Drinks", None, "A refreshing cold coffee drink served over ice.", 8.0)
    add_drink("Iced Chocolate", "Cold Drinks", None, "A chilled chocolate drink served over ice.", 8.0)
    add_drink("Lemon Lime Bitters", "Cold Drinks", None, "A tangy and refreshing drink with a blend of lemon, lime, and bitters.", 8.0)
    add_drink("Redbull", "Cold Drinks", None, "An energy drink to give you a boost.", 8.0)
    add_drink("Awswan Hibiscus Cold Tea (Karkadeh)", "Cold Drinks", None, "A traditional Egyptian cold tea made from hibiscus flowers.", 6.0)
    add_drink("Peach Iced Tea", "Cold Drinks", None, "A sweet and fruity iced tea flavored with peaches.", 6.0)
    add_drink("Coke", "Cold Drinks", None, "A classic carbonated soft drink.", 6.0)
    add_drink("Coke Zero", "Cold Drinks", None, "A sugar-free version of the classic carbonated soft drink.", 6.0)
    add_drink("Lemonade", "Cold Drinks", None, "A refreshing drink made from fresh lemons, water, and sugar.", 6.0)
    add_drink("Fanta Raspberry", "Cold Drinks", None, "A fruity and fizzy raspberry-flavored soft drink.", 6.0)

if __name__ == "__main__":
    seed_drinks()
    print("Seeding completed.")
    session.close()
