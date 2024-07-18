from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Drink, Food, ShishaHead, ShishaFlavor, RestaurantTable

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

def add_food(name, main_category, sub_category=None, description=None, price=None):
    existing_food = session.query(Food).filter_by(name=name).first()
    if existing_food is None:
        food = Food(
            name=name, 
            main_category=main_category, 
            sub_category=sub_category, 
            description=description, 
            price=price
        )
        session.add(food)
        session.commit()
    else:
        print(f"Food {name} already exists. Skipping.")

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

def seed_special_drinks():
    # Mocktails
    add_drink("Mango Mojito", "Special Drinks", "Mocktails", "A delicious layered drink of mango juice with lime and fresh mint.", 14.0)
    add_drink("Egyptian Lemon Mint", "Special Drinks", "Mocktails", "Egyptian blend of fresh mint and lemon mint tea.", 14.0)
    add_drink("Nectarine’s Dream", "Special Drinks", "Mocktails", "A delicious blend of nectarine, pineapple juice, aloe vera juice, and tropical flavors.", 15.0)
    
    # Cocktails
    add_drink("Toblerone", "Special Drinks", "Cocktails", "Creamy cocktail containing Baileys, Frangelico, Kahlua and fresh cream.", 22.0)
    add_drink("Fruit Tingle", "Special Drinks", "Cocktails", "Sweet & exotic, this cocktail contains vodka, blue curacao, raspberry & lemonade.", 19.0)
    add_drink("Pina Colada", "Special Drinks", "Cocktails", "A delicious pina colada mix with coconut cream, pineapple juice & Malibu.", 19.0)
    add_drink("Cosmopolitan", "Special Drinks", "Cocktails", "Classy cocktail containing vodka, Cointreau, lime juice, and cranberry juice.", 19.0)
    add_drink("Espresso Martini", "Special Drinks", "Cocktails", "For the coffee hit, this must-try contains vodka, Kahlua, and espresso.", 19.0)
    add_drink("Vodka Red Bull or Jager Red Bull", "Special Drinks", "Cocktails", "Vodka or Jager mixed with Red Bull for a tasty boost.", 18.0)
    add_drink("Vodka Sunrise or Tequila Sunrise", "Special Drinks", "Cocktails", "Vodka or tequila mixed with orange juice, slightly grenadine.", 18.0)
    add_drink("Nectarine’s Dream with Tequila or Vodka", "Special Drinks", "Cocktails", "Nectarine’s Dream with a dash of tequila or vodka for a summer twist.", 18.0)
    
    # Specialty Cocktails
    add_drink("Summer in Cairo", "Special Drinks", "Specialty Cocktails", "A refreshing cocktail with rum, coconut milk, pineapple juice, and strawberries.", 24.0)
    add_drink("Cleopatra’s Kiss", "Special Drinks", "Specialty Cocktails", "A delightful blend of champagne, strawberry liqueur, and strawberries.", 24.0)
    add_drink("Pharaoh's Poison", "Special Drinks", "Specialty Cocktails", "A unique cocktail with banana liqueur, passion fruit liqueur, and tropical fruit.", 24.0)
    add_drink("Tahitian Dream", "Special Drinks", "Specialty Cocktails", "A tropical mix with coconut rum, pineapple juice, and passion fruit liqueur.", 24.0)
    add_drink("Blue Lagoon", "Special Drinks", "Specialty Cocktails", "A vibrant blue cocktail with vodka, blue curacao, and lemonade.", 24.0)

def seed_entrees():
    # From the Egypt
    add_food("Kebda Iskandarani", "Entree", "From the Egypt", "Veal liver marinated and pan tossed with chilli, garlic & Chef Thawat’s special spices, served with a side of Tahini & our bread.", 24.0)
    add_food("Egyptian Waraq Enab", "Entree", "From the Egypt", "Vines leaves stuffed with rice, herbs & mince meat.", 24.0)
    add_food("Hawawshi", "Entree", "From the Egypt", "Spiced minced meat cooked in the oven in flat baladi bread with onions, capsicum & chilli.", 19.0)
    add_food("Mombar", "Entree", "From the Egypt", "3 pieces sausage skin stuffed with special spicy rice, tomato, onions & herbs.", 19.0)
    add_food("Dukkah Lamb Brain", "Entree", "From the Egypt", "Lamb brain coated with dukkah cooked in breadcrumbs.", 19.0)
    
    # From the Sea
    add_food("Calamari", "Entree", "From the Sea", "Fried calamari with aioli.", 24.0)
    
    # From the Middle-East
    add_food("Chicken Wings", "Entree", "From the Middle-East", "Marinated & grilled chicken wings served with a gel dip.", 18.0)
    add_food("Kobeba", "Entree", "From the Middle-East", "3 pieces of ground meat with bulgur wheat, stuffed with spices, pine nuts & onions.", 18.0)
    add_food("Lamb Sambousek", "Entree", "From the Middle-East", "Pastry stuffed with lamb mince, onions & spices.", 15.0)
    add_food("Cheese Sambousek", "Entree", "From the Middle-East", "Pastry stuffed with fetta cheese & herbs.", 15.0)
    add_food("Molokhia Soup", "Entree", "From the Middle-East", "Egyptian stew served with our bread.", 14.0)
    add_food("Lentil Soup", "Entree", "From the Middle-East", "Served with our bread.", 14.0)

    # Dips
    add_food("Feta Cheese Dip", "Entree", "Dips", "Mixed cheese with olives & spices.", 12.0)
    add_food("Garlic Dip", "Entree", "Dips", "Crushed garlic puree with oil & lemon.", 12.0)
    add_food("Tzatziki", "Entree", "Dips", "Yoghurt with cucumber & mint.", 12.0)
    add_food("Pet Pet", "Entree", "Dips", "Chilli dip.", 12.0)
    add_food("Baba Ghanoush", "Entree", "Dips", "Grilled eggplant, tahini & garlic.", 12.0)
    add_food("Tourshi", "Entree", "Dips", "Homemade mixed pickles.", 11.0)
    add_food("Bread Basket", "Entree", "Dips", "3 pieces of our homemade bread.", 6.0)
    
    # Salads
    add_food("Lamb Tenderloin Salad", "Entree", "Salads", "Grilled lamb tenderloins on a bed of salad leaves & Egyptian dukkah.", 28.0)
    add_food("Prawn Salad", "Entree", "Salads", "Lemon & olive oil dressing.", 26.0)
    add_food("Chicken Salad", "Entree", "Salads", "Marinated grilled chicken on a bed of salad leaves with special Egyptian style dressing.", 18.0)
    add_food("Greek Salad", "Entree", "Salads", "Lettuce, feta cheese, olives, tomato & capsicum.", 18.0)
    add_food("Salata Baladi", "Entree", "Salads", "Tomato, cucumber, onion, lettuce with lemon & olive oil dressing.", 11.0)

def seed_main_claypots():
    # Egyptian Style Claypots
    add_food("Tagen Super Sayadia", "Main", "Egyptian Style Claypots", "Barramundi fish fillet, calamari, prawn, tomato puree & capsicum baked in an Egyptian style claypot served on a bed of Sayadia rice.", 38.0)
    add_food("Tagen Sayadia", "Main", "Egyptian Style Claypots", "Barramundi fish fillet baked with spicy tomato & capsicum sauce baked in an Egyptian style claypot served on a bed of Sayadia rice.", 32.0)
    add_food("Tagen Lamb Roz Moammar", "Main", "Egyptian Style Claypots", "Rice cooked in an Egyptian style claypot with lamb fillet pieces, onions & cream.", 29.0)
    add_food("Tagen Prawn Roz Moammar", "Main", "Egyptian Style Claypots", "Rice cooked in an Egyptian style claypot with prawn, garlic, onions & cream.", 29.0)
    add_food("Tagen Calamari Iskandarani", "Main", "Egyptian Style Claypots", "Spicy Calamari baked in tomato puree in an Egyptian style claypot, served with bread, The Alexandrian way!", 28.0)
    add_food("Tagen Bamia", "Main", "Egyptian Style Claypots", "Egyptian Bamia (Okra) is a stew with lamb, cooked in an Egyptian style claypot.", 28.0)
    add_food("Tagen Macarona Bechamel", "Main", "Egyptian Style Claypots", "Penne pasta with mince beef covered with bechamel sauce cooked in an Egyptian style claypot.", 26.0)
    add_food("Tagen Moussaka", "Main", "Egyptian Style Claypots", "Eggplant with beef mince and tomato puree topped with bechamel sauce, cooked in an Egyptian style claypot.", 26.0)
    add_food("Tagen Moussaka Falahi", "Main", "Egyptian Style Claypots", "Eggplant baked in tomato puree with capsicum slices & chilli served with our homemade bread.", 24.0)

def seed_authentic_egyptian_plates():
    # Authentic Egyptian Plates
    add_food("Lamb Shank Fattah", "Main", "Authentic Egyptian Plates", "Lamb shank served on a bed of rice cooked with angel hair pasta, topped with fried bread pieces & special garlic vinegar sauce.", 39.0)
    add_food("Samakmak", "Main", "Authentic Egyptian Plates", "Chef Tharwat’s Special Fish Dish. Singari Style baked barramundi fillet with onions, capsicum & special spices.", 36.0)
    add_food("Molokhia with Chicken", "Main", "Authentic Egyptian Plates", "Egyptian jute stew served in a bowl with a side of grilled half chicken & vermicelli rice.", 29.0)
    add_food("Kawarrah", "Main", "Authentic Egyptian Plates", "Buffalo trotters slow cooked and served on a bed of vermicelli rice, topped with fried bread pieces, garlic sauce & soup.", 29.0)
    add_food("Koshari", "Main", "Authentic Egyptian Plates", "Egypt’s popular street food. Layers of black lentils, medium grain rice, macaroni pasta, chickpeas, fried onions, salsa & a special dukkah dressing.", 24.0)

def seed_grill_items():
    # From the Grill
    add_food("Cairo King Grill", "Main", "From the Grill", "Selection of three dips to share, 2 Lamb Kebabs, 2 Kofta Skewers, 2 Chicken Kebabs, 2 Chicken Wings, 1 Quail (cut in half), served with a side of our Cairo rice & Salata Baladi. Suitable for 2 people.", 99.0)
    add_food("Mix Grill", "Main", "From the Grill", "1 lamb kofta, 1 lamb kebab, 1 chicken kebab served with a garlic & hummus dip, served with a side of our Cairo rice & Salata Baladi.", 38.0)
    add_food("BBQ Quails", "Main", "From the Grill", "2 large quail marinated and grilled served with a side of our Cairo rice, Salata Baladi & garlic dip.", 34.0)
    add_food("Lamb Shish Kebab", "Main", "From the Grill", "2 marinated lamb tenderloin served with a side of Cairo rice, hummus dip & Salata Baladi.", 34.0)
    add_food("Lamb Kofta", "Main", "From the Grill", "2 low fat lamb mince skewers served with a side of our Cairo rice, hummus dip & Salata Baladi.", 32.0)
    add_food("Chicken Shish Kebab", "Main", "From the Grill", "2 large skewers of thigh fillets served with a side of Cairo rice, garlic dip & Salata Baladi.", 32.0)

def seed_kids_menu():
    # Kids Menu
    add_food("Lamb Kofta & Chips", "Main", "Kids Menu", "1 skewer of lamb kofta served with a side of chips & tomato sauce.", 19.0)
    add_food("Chicken & Chips", "Main", "Kids Menu", "1 skewer of thigh fillet served with a side of hot chips & tomato sauce.", 19.0)
    add_food("Fish & Chips", "Main", "Kids Menu", "Fried fish fillet served with side of hot chips & tomato sauce.", 19.0)
    add_food("Kids Pasta", "Main", "Kids Menu", "Pasta served with your choice of tomato sauce or bolognese.", 19.0)
    add_food("Bowl of Chips", "Main", "Kids Menu", "A bowl of hot chips with tomato sauce.", 14.0)

def seed_desserts():
    # Desserts
    add_food("Om Ali (Mother of Ali) - Small", "Desserts", None, "A traditional Egyptian croissant pudding, small size.", 14.0)
    add_food("Om Ali (Mother of Ali) - Medium", "Desserts", None, "A traditional Egyptian croissant pudding, medium size.", 18.0)
    add_food("Om Ali (Mother of Ali) - Large", "Desserts", None, "A traditional Egyptian croissant pudding, large size.", 26.0)
    add_food("Om Ali (Mother of Ali) - Family", "Desserts", None, "A traditional Egyptian croissant pudding, family size.", 36.0)
    add_food("Konafa with Mango", "Desserts", None, "Angel hair pastry served with mango pieces, cream & ice cream.", 14.0)
    add_food("Roz bel Laban With Mango", "Desserts", None, "Traditional style sweet rice pudding with mango.", 14.0)
    add_food("Roz bel Laban", "Desserts", None, "Traditional style sweet rice pudding topped with pistachio, cinnamon powder & sultanas.", 12.0)
    add_food("Baklava - 1 Piece", "Desserts", None, "Middle Eastern sweets.", 4.0)
    add_food("Baklava - 3 Pieces", "Desserts", None, "Middle Eastern sweets.", 11.0)
    add_food("Ice-Cream", "Desserts", None, "x2 scoops with either - strawberry, chocolate or caramel sauce.", 5.0)

def delete_food_by_id_and_name(food_id, name):
    food_item = session.query(Food).filter_by(id=food_id, name=name).first()
    if food_item:
        session.delete(food_item)
        session.commit()
        print(f"Food item with ID {food_id} and name '{name}' has been deleted.")
    else:
        print(f"No food item found with ID {food_id} and name '{name}'.")

def seed_shisha():
    # Shisha Heads
    add_shisha_head("Clay Head", 45.0)
    add_shisha_head("Premium Head", 50.0)
    add_shisha_head("French Apple Head", 50.0)
    
    # Shisha Flavors
    add_shisha_flavor("Lady Killer", None, 5.0)
    add_shisha_flavor("Punkman", None, 5.0)
    add_shisha_flavor("Godfather", None, 5.0)
    add_shisha_flavor("Joker 777", None, 5.0)
    add_shisha_flavor("Shiek Money", None, 5.0)
    add_shisha_flavor("Love 66", None, 5.0)
    add_shisha_flavor("Magic Love", None, 5.0)
    add_shisha_flavor("Homer Simpson", None, 5.0)

    add_shisha_flavor("Lady in Blue", "Contains Lady Killer, Love 66 and Blueberry", 5.0)
    add_shisha_flavor("Blue Heaven", "Contains Blueberry with Gum Mint", 5.0)
    add_shisha_flavor("Tropical Island", "Contains Kiwi with Gum Mint", 5.0)
    add_shisha_flavor("Citrus King", "Contains Orange with Lemon and Mint", 5.0)
    add_shisha_flavor("Fruit Fever", "Contains Apple, Kiwi, Gum Mint", 5.0)

    add_shisha_flavor("Double Apple", None, 5.0)
    add_shisha_flavor("Apple Mint", None, 5.0)
    add_shisha_flavor("Grape with or without Mint", None, 5.0)
    add_shisha_flavor("Blueberry with or without Mint", None, 5.0)
    add_shisha_flavor("Kiwi with or without Mint", None, 5.0)
    add_shisha_flavor("Watermelon with or without Mint", None, 5.0)
    add_shisha_flavor("Peach with or without Mint", None, 5.0)
    add_shisha_flavor("Lemon Mint", None, 5.0)
    add_shisha_flavor("Orange with or without Mint", None, 5.0)
    add_shisha_flavor("Gum Mint", None, 5.0)

def add_shisha_head(head_type, price):
    existing_shisha_head = session.query(ShishaHead).filter_by(head_type=head_type).first()
    if existing_shisha_head is None:
        shisha_head = ShishaHead(head_type=head_type, price=price)
        session.add(shisha_head)
        session.commit()
    else:
        print(f"Shisha head type {head_type} already exists. Skipping.")

def add_shisha_flavor(name, description, extra_price):
    existing_shisha_flavor = session.query(ShishaFlavor).filter_by(name=name).first()
    if existing_shisha_flavor is None:
        shisha_flavor = ShishaFlavor(name=name, description=description, extra_price=extra_price)
        session.add(shisha_flavor)
        session.commit()
    else:
        print(f"Flavor {name} already exists. Skipping.")
def add_table(location, table_number, capacity, is_available=True):
    existing_table = session.query(RestaurantTable).filter_by(location=location, table_number=table_number).first()
    if existing_table is None:
        table = RestaurantTable(
            location=location,
            table_number=table_number,
            capacity=capacity,
            is_available=is_available
        )
        session.add(table)
        session.commit()
    else:
        print(f"Table {location} {table_number} already exists. Skipping.")

def seed_tables():
    # Indoor Tables
    indoor_tables = [
        (1, 6), (2, 4), (3, 6), (4, 2), (5, 8), (6, 2), (7, 4), 
        (8, 0), (9, 0), (10, 4), (11, 4), (12, 4), (13, 2)
    ]
    
    for table_number, capacity in indoor_tables:
        add_table("Indoor", table_number, capacity, is_available=(capacity != 0))

    # Terrace Tables
    terrace_tables = [
        (1, 0), (2, 2), (3, 2), (4, 3), (5, 5), (6, 2), (7, 2),
        (8, 4), (9, 6), (10, 4), (11, 0), (12, 5), (13, 2), (14, 14, False),
        (15, 4), (16, 4), (17, 2), (18, 4), (19, 6), (20, 4), (21, 4), (22, 2)
    ]
    
    for table in terrace_tables:
        if len(table) == 2:
            table_number, capacity = table
            add_table("Terrace", table_number, capacity, is_available=(capacity != 0))
        elif len(table) == 3:
            table_number, capacity, is_available = table
            add_table("Terrace", table_number, capacity, is_available)

    # Street Tables
    for table_number in range(1, 13):
        add_table("Street", table_number, 4)

if __name__ == "__main__":
    seed_tables()
    print("Table seeding completed.")
    session.close()