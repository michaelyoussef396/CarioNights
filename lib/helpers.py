from db.models import Order, Reservation, RestaurantEmployee, RestaurantTable, ShishaFlavor, session, ShishaHead, Drink, Food, WaitingList, Feedback
import click

def print_message(message):
    print(message)

def get_current_table_number():
    return int(input("Enter your table number: "))

def view_shisha_heads():
    print("\nShisha Heads Menu:")
    shisha_heads = session.query(ShishaHead).all()
    for head in shisha_heads:
        print(f"{head.id}. {head.head_type} - ${head.price}")
    input("\nPress Enter to go back.")

def view_drinks():
    print("\nDrinks Menu:")
    drinks = session.query(Drink).all()
    for drink in drinks:
        print(f"{drink.id}. {drink.name} - ${drink.price_glass if drink.price_glass else drink.price_bottle}")
    input("\nPress Enter to go back.")

def view_food():
    print("\nFood Menu:")
    foods = session.query(Food).all()
    for food in foods:
        print(f"{food.id}. {food.name} - ${food.price}")
    input("\nPress Enter to go back.")

def order_shisha_head():
    table_id = get_current_table_number()
    if table_id is None:
        return
    
    name = input("\nEnter the name of the Shisha Head you want to order: ")
    shisha_head = session.query(ShishaHead).filter(ShishaHead.head_type.ilike(f"%{name}%")).first()
    if not shisha_head:
        print("\nInvalid Shisha Head name. Please try again.")
        return
    
    flavor_name = input("\nEnter the name of the Shisha Flavor you want: ")
    flavor = session.query(ShishaFlavor).filter(ShishaFlavor.name.ilike(f"%{flavor_name}%")).first()
    if not flavor:
        print("\nInvalid Shisha Flavor name. Please try again.")
        return
    
    quantity = int(input("Enter quantity: "))
    
    head_order = Order(table_number=table_id, item_type='ShishaHead', item_id=shisha_head.id, quantity=quantity)
    flavor_order = Order(table_number=table_id, item_type='ShishaFlavor', item_id=flavor.id, quantity=quantity)
    session.add_all([head_order, flavor_order])
    session.commit()
    
    print(f"\nYou have ordered: {quantity} x {shisha_head.head_type} with {flavor.name} flavor. It will be served shortly.")
    input("\nPress Enter to go back.")

def order_drink():
    table_number = get_current_table_number()
    name = input("\nEnter the name of the Drink you want to order: ")
    drink = session.query(Drink).filter(Drink.name.ilike(f"%{name}%")).first()
    if drink:
        quantity = int(input("Enter quantity: "))
        order = Order(table_number=table_number, item_type='Drink', item_id=drink.id, quantity=quantity)
        session.add(order)
        session.commit()
        print(f"\nYou have ordered: {quantity} x {drink.name}. It will be served shortly.")
    else:
        print("\nInvalid Drink name. Please try again.")
    input("\nPress Enter to go back.")

def order_food():
    table_number = get_current_table_number()
    name = input("\nEnter the name of the Food you want to order: ")
    food = session.query(Food).filter(Food.name.ilike(f"%{name}%")).first()
    if food:
        quantity = int(input("Enter quantity: "))
        order = Order(table_number=table_number, item_type='Food', item_id=food.id, quantity=quantity)
        session.add(order)
        session.commit()
        print(f"\nYou have ordered: {quantity} x {food.name}. It will be served shortly.")
    else:
        print("\nInvalid Food name. Please try again.")
    input("\nPress Enter to go back.")

def check_order_status():
    print("\nChecking order status...")
    order_item_name = input("Enter the name of the ordered item to check its status: ")
    print(f"\nApologies for the delay. Your order '{order_item_name}' will be served within 5 minutes.")
    input("\nPress Enter to go back.")

def give_feedback():
    customer_name = input("\nPlease enter your name: ")
    feedback_text = input("Please provide your feedback: ")
    
    new_feedback = Feedback(customer_name=customer_name, feedback=feedback_text)
    session.add(new_feedback)
    session.commit()
    
    print("\nThank you for your feedback! We appreciate your input and will strive to improve our services.")
    input("\nPress Enter to go back.")

def reservation():
    customer_name = input("Please enter your name: ")
    reservation = session.query(Reservation).filter_by(customer_name=customer_name).first()
    if reservation:
        table = session.query(RestaurantTable).filter_by(id=reservation.table_number).first()
        if table:
            if table.is_available or reservation.customer_name == customer_name:
                table.is_available = False
                session.commit()
                click.echo(f"\nReservation found for {customer_name}. Please proceed to table number {table.table_number}.")
            else:
                click.echo(f"\nReservation found, but table number {reservation.table_number} is currently occupied by another reservation.")
        else:
            click.echo(f"\nNo table found with number {reservation.table_number}.")
    else:
        click.echo("\nNo reservation found for your name. Please check with the reception.")

def walk_in():
    click.echo("\nYou are here for a walk-in. Please wait to be seated.")
    customer_name = input("Please enter your name: ")
    num_people = int(input("Number of people: "))
    
    waiting = WaitingList(
        customer_name=customer_name,
        num_people=num_people,
        reason='Walk-in'
    )
    session.add(waiting)
    session.commit()
    click.echo(f"{customer_name}, you have been added to the waiting list for {num_people} people. Please wait to be seated.")
    
    session.close()

def make_reservation():
    click.echo("\nMaking a reservation.")
    customer_name = input("Please enter your name: ")
    num_people = int(input("Number of people for the reservation: "))
    reservation_time = input("Reservation time (e.g., 7:00 PM): ")

    available_table = session.query(RestaurantTable).filter_by(is_available=True).filter(RestaurantTable.capacity >= num_people).first()

    if available_table:
        available_table.is_available = False
        session.add(available_table)

        reservation = Reservation(
            customer_name=customer_name,
            table_number=available_table.id
        )
        session.add(reservation)
        session.commit()
        click.echo(f"Reservation made for {customer_name} for {num_people} people at {reservation_time}. Your table number is {available_table.table_number}.")
    else:
        click.echo("Sorry, no tables are available for the specified number of people.")
    
    session.close()

def view_menu():
    while True:
        click.echo("\nView Menu:")
        click.echo("1. Shisha Heads")
        click.echo("2. Drinks")
        click.echo("3. Food")
        click.echo("4. Go back")
        menu_choice = input("Enter your choice: ")

        if menu_choice == '1':
            view_shisha_heads()
        elif menu_choice == '2':
            view_drinks()
        elif menu_choice == '3':
            view_food()
        elif menu_choice == '4':
            return
        else:
            click.echo("\nInvalid choice, please select a valid option (1, 2, 3, or 4).")

def order_item():
    while True:
        click.echo("\nOrder Item:")
        click.echo("1. Shisha Heads")
        click.echo("2. Drinks")
        click.echo("3. Food")
        click.echo("4. Go back")
        order_choice = input("Enter your choice: ")

        if order_choice == '1':
            order_shisha_head()
        elif order_choice == '2':
            order_drink()
        elif order_choice == '3':
            order_food()
        elif order_choice == '4':
            return
        else:
            click.echo("\nInvalid choice, please select a valid option (1, 2, 3, or 4).")

def print_bill():
    table_id = get_current_table_number()
    if table_id is None:
        return
    
    orders = session.query(Order).filter_by(table_number=table_id).all()
    table = session.query(RestaurantTable).get(table_id)
    
    if not orders:
        print("\nYou haven't ordered anything yet.")
        return

    print(f"\n--- Bill for Table {table.table_number} ---")
    total = 0
    for order in orders:
        if order.item_type == 'ShishaHead':
            item = session.query(ShishaHead).get(order.item_id)
            price = item.price * order.quantity
            print(f"{order.quantity} x {item.head_type} (Shisha Head): ${price:.2f}")
        elif order.item_type == 'ShishaFlavor':
            item = session.query(ShishaFlavor).get(order.item_id)
            price = item.extra_price * order.quantity
            print(f"{order.quantity} x {item.name} (Shisha Flavor): ${price:.2f}")
        elif order.item_type == 'Drink':
            item = session.query(Drink).get(order.item_id)
            price = (item.price_glass or item.price_bottle) * order.quantity
            print(f"{order.quantity} x {item.name} (Drink): ${price:.2f}")
        elif order.item_type == 'Food':
            item = session.query(Food).get(order.item_id)
            price = item.price * order.quantity
            print(f"{order.quantity} x {item.name} (Food): ${price:.2f}")
        
        total += price
    
    print(f"\nTotal: ${total:.2f}")
    
    while True:
        choice = input("\nEnter '1' to go back or '2' to request payment: ")
        if choice == '1':
            return
        elif choice == '2':
            waiting_list = WaitingList(customer_name=f"Table {table.table_number}", num_people=1, reason="Payment")
            session.add(waiting_list)
            session.commit()
            print("\nYou have been added to the waiting list for payment. An employee will assist you shortly.")
            input("\nPress Enter to go back to the main menu.")
            return
        else:
            print("Invalid choice. Please try again.")

def check_on_tables():
    occupied_tables = session.query(RestaurantTable).filter_by(is_available=False).all()
    if occupied_tables:
        for table in occupied_tables:
            click.echo(f"Table number {table.table_number} is occupied.")
            response = input(f"Do you want to check on table number {table.table_number}? (yes/no): ")
            if response.lower() == 'yes':
                click.echo(f"Checked on table number {table.table_number}. The customers are satisfied.")
    else:
        click.echo("No occupied tables found.")

def deliver_food():
    table_number = input("Enter the table number to deliver food to: ")
    orders = session.query(Order).filter_by(table_number=table_number, item_type='Food').all()
    if orders:
        click.echo(f"Food has been delivered to table number {table_number}.")
        for order in orders:
            food_item = session.query(Food).get(order.item_id)
            click.echo(f"Delivered: {order.quantity} x {food_item.name}")
    else:
        click.echo(f"No food orders found for table number {table_number}.")

def clean_table():
    table_number = input("Enter the table number to clean: ")
    table = session.query(RestaurantTable).filter_by(table_number=table_number).first()
    if table:
        table.is_available = True
        session.commit()
        click.echo(f"Table number {table_number} has been cleaned and is now available.")
    else:
        click.echo(f"No table found with number {table_number}.")

def view_all_reservations():
    click.echo("\nAll Reservations:")
    reservations = session.query(Reservation).all()
    for reservation in reservations:
        click.echo(f"Reservation ID: {reservation.id}, Customer Name: {reservation.customer_name}, Table Number: {reservation.table_number}")
    input("\nPress Enter to go back.")

def view_all_orders():
    click.echo("\nAll Orders:")
    orders = session.query(Order).all()
    for order in orders:
        click.echo(f"Order ID: {order.id}, Table Number: {order.table_number}, Item Type: {order.item_type}, Item ID: {order.item_id}, Quantity: {order.quantity}")
    input("\nPress Enter to go back.")

def add_employee():
    name = input("Enter the name of the new employee: ")
    role = input("Enter the role of the new employee (e.g., Waiter, Chef, Manager): ")
    new_employee = RestaurantEmployee(name=name, role=role)
    session.add(new_employee)
    session.commit()
    click.echo(f"Employee {name} added successfully with role {role}.")

def remove_employee():
    name = input("Enter the name of the employee to remove: ")
    employee = session.query(RestaurantEmployee).filter_by(name=name).first()
    if employee:
        session.delete(employee)
        session.commit()
        click.echo(f"Employee {name} removed successfully.")
    else:
        click.echo(f"No employee found with name {name}.")

def change_employee_role():
    name = input("Enter the name of the employee whose role you want to change: ")
    new_role = input(f"Enter the new role for {name}: ")
    employee = session.query(RestaurantEmployee).filter_by(name=name).first()
    if employee:
        employee.role = new_role
        session.commit()
        click.echo(f"Employee {name}'s role changed to {new_role}.")
    else:
        click.echo(f"No employee found with name {name}.")

def manage_employees():
    while True:
        click.echo("\nManage Employees:")
        click.echo("1. Add an employee")
        click.echo("2. Remove an employee")
        click.echo("3. Change an employee's role")
        click.echo("4. Go back to the management menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            change_employee_role()
        elif choice == '4':
            return
        else:
            click.echo("\nInvalid choice, please select a valid option (1, 2, 3, or 4).")