from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Drink

# Database setup
DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_drink(name, main_category, sub_category=None, description=None, price_glass=None, price_bottle=None):
    existing_drink = session.query(Drink).filter_by(name=name).first()
    if existing_drink is None:
        drink = Drink(
            name=name, 
            main_category=main_category, 
            sub_category=sub_category, 
            description=description, 
            price_glass=price_glass, 
            price_bottle=price_bottle
        )
        session.add(drink)
        session.commit()
    else:
        print(f"Drink {name} already exists. Skipping.")

def seed_cold_drinks():
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

def seed_hot_drinks():
    # Hot Drinks
    add_drink("Egyptian Sahlab", "Hot Drinks", "Sweet Drink", "A traditional Egyptian sweet drink made from milk and flavored with rose water and nuts.", 8.0)
    add_drink("Hot Chocolate", "Hot Drinks", None, "A rich and creamy hot chocolate drink.", 7.0)
    
    # Coffee Subcategory
    add_drink("Chai Latte", "Hot Drinks", "Coffee", "A spiced tea latte made with steamed milk.", 7.0)
    add_drink("Dirt Chai Latte", "Hot Drinks", "Coffee", "A chai latte with a shot of espresso.", 7.0)
    add_drink("Espresso", "Hot Drinks", "Coffee", "A strong and rich coffee shot.", 5.0)
    add_drink("Latte", "Hot Drinks", "Coffee", "A classic coffee drink made with espresso and steamed milk.", 5.0)
    add_drink("Cappuccino", "Hot Drinks", "Coffee", "A coffee drink made with espresso, steamed milk, and foam.", 5.0)
    add_drink("Flat White", "Hot Drinks", "Coffee", "A smooth and velvety coffee made with espresso and steamed milk.", 5.0)
    add_drink("Long Black", "Hot Drinks", "Coffee", "A coffee drink made by pouring a double-shot of espresso over hot water.", 5.0)
    add_drink("Mocaccino", "Hot Drinks", "Coffee", "A coffee drink made with espresso, chocolate, and steamed milk.", 5.0)
    add_drink("Turkish Coffee", "Hot Drinks", "Coffee", "A traditional Turkish coffee made with finely ground coffee beans.", 5.0)
    
    # Tea Subcategory
    tea_varieties = [
        "Egyptian Mint Tea", "Black Tea", "Spearmint Tea", "Peppermint Tea", 
        "Chamomile Tea", "Green Tea", "Honey and Vanilla Tea", 
        "Blue and Blackcurrant Tea", "Strawberry, Loganberry and Raspberry Tea", 
        "Orange and Pomegranate Tea", "Mango and Strawberry Tea", "Green Tea with Jasmine"
    ]
    
    for tea in tea_varieties:
        add_drink(tea, "Hot Drinks", "Tea", f"A flavorful and soothing cup of {tea.lower()}.", 5.0)

def seed_bws_drinks():
    # Beers
    add_drink("Corona", "BWS", "Beers", "A refreshing Mexican beer with a hint of lime.", 11.0)
    add_drink("Stella", "BWS", "Beers", "A premium Belgian lager with a crisp taste.", 11.0)
    add_drink("Crown Lager", "BWS", "Beers", "A smooth Australian lager with a rich flavor.", 11.0)
    add_drink("Asahi", "BWS", "Beers", "A Japanese beer with a clean, crisp taste.", 11.0)
    add_drink("Peroni", "BWS", "Beers", "An Italian beer with a light and refreshing flavor.", 11.0)
    
    # Ciders
    add_drink("Strawberry & Lime Cider", "BWS", "Ciders", "A sweet and tangy cider with strawberry and lime flavors.", 12.0)
    add_drink("Wild Berries Cider", "BWS", "Ciders", "A fruity cider with a mix of wild berry flavors.", 12.0)
    add_drink("Mango Raspberry Cider", "BWS", "Ciders", "A tropical cider with mango and raspberry flavors.", 12.0)
    add_drink("Passionfruit Cider", "BWS", "Ciders", "A refreshing cider with passionfruit flavors.", 12.0)
    
    # Sparkling Wines
    add_drink("T Gallant Prosecco DOC", "BWS", "Sparkling Wine", "A light and crisp prosecco with floral notes.", 12.0, 46.0)
    add_drink("Jacob's Creek Trilogy", "BWS", "Sparkling Wine", "A well-balanced sparkling wine with fruity flavors.", 11.0, 39.0)
    
    # White Wines
    add_drink("Squealing Pig Sauvignon Blanc", "BWS", "White Wine", "A vibrant sauvignon blanc with tropical fruit flavors.", 12.0, 46.0)
    add_drink("Tread Softly Pinot Grigio", "BWS", "White Wine", "A light and refreshing pinot grigio with citrus notes.", 11.0, 42.0)
    add_drink("St Huberts The Stag Chardonnay", "BWS", "White Wine", "A rich chardonnay with notes of stone fruit and oak.", 11.0, 42.0)
    add_drink("Zonin Moscato Veneto", "BWS", "White Wine", "A sweet and floral moscato with a light fizz.", 10.0, 38.0)
    add_drink("Brown Brothers Moscato", "BWS", "White Wine", "A refreshing moscato with sweet and fruity flavors.", 9.0, 32.0)
    
    # Rose Wines
    add_drink("Prestige d'Adimant Rose", "BWS", "Rose Wine", "A crisp and refreshing rose with notes of red berries.", 14.0, 48.0)
    add_drink("Saint Louis de Provence Estadon Rose", "BWS", "Rose Wine", "A delicate rose with flavors of strawberry and peach.", 12.0, 44.0)
    
    # Red Wines
    add_drink("Pepperjack Barossa Shiraz", "BWS", "Red Wine", "A full-bodied shiraz with rich berry flavors.", 12.0, 46.0)
    add_drink("Wynns Coonawarra Cab Shiraz Merlot", "BWS", "Red Wine", "A blend of cabernet, shiraz, and merlot with dark fruit flavors.", 11.0, 44.0)
    add_drink("Devils Corner Pinot Noir", "BWS", "Red Wine", "A smooth pinot noir with flavors of cherry and spice.", 11.0, 44.0)
    add_drink("St Hallett Gamekeeper's Barossa Shiraz", "BWS", "Red Wine", "A vibrant shiraz with flavors of blackberry and plum.", 11.0, 32.0)
    add_drink("El Valiente Spanish Tempranillo", "BWS", "Red Wine", "A rich tempranillo with flavors of dark berries and oak.", 10.0, 42.0)
    
    # Spirits
    spirits = [
        ("Jack Daniel's", "A popular Tennessee whiskey with a smooth flavor.", 8.0, 60.0),
        ("Johnnie Walker Black Label", "A rich and complex blended Scotch whisky.", 10.0, 70.0),
        ("Absolut Vodka", "A smooth and pure Swedish vodka.", 7.0, 50.0),
        ("Grey Goose Vodka", "A premium French vodka with a smooth finish.", 12.0, 80.0),
        ("Bombay Sapphire Gin", "A popular gin with a balanced blend of botanicals.", 8.0, 60.0),
        ("Tanqueray Gin", "A classic gin with a crisp and refreshing taste.", 9.0, 65.0),
        ("Bacardi Superior Rum", "A light and smooth white rum.", 7.0, 45.0),
        ("Captain Morgan Spiced Rum", "A spiced rum with a rich and smooth flavor.", 8.0, 55.0),
        ("Jose Cuervo Tequila", "A popular tequila with a smooth and fiery taste.", 9.0, 60.0),
        ("Patron Silver Tequila", "A premium tequila with a smooth and clean finish.", 12.0, 85.0)
    ]
    
    for spirit_name, description, price_shot, price_bottle in spirits:
        add_drink(spirit_name, "BWS", "Spirits", description, price_shot, price_bottle)

if __name__ == "__main__":
    seed_bws_drinks()
    print("Seeding completed.")
    session.close()
