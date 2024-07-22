import click

from db.models import Base, Reservation, RestaurantTable, session
import os



def print_menu():
    click.echo("Welcome to the Cario Nights Restaurant Management System")
    click.echo("Cario Nights offers a delightful dining experience with a variety of dishes, drinks, and a cozy ambiance.")
    click.echo("We are committed to providing excellent service to our customers and a great working environment for our staff.")
    click.echo("\nPlease choose an option:")
    click.echo("1. Management")
    click.echo("2. Employees")
    click.echo("3. Customers")
    click.echo("4. Quit the application")

def management():
    click.echo("Management options are under development. Please check back later.")

def employees():
    click.echo("Employees options are under development. Please check back later.")

def customers():
    click.echo("\nCustomer options:")
    click.echo("1. I have a reservation")
    click.echo("2. I am here for a walk-in")
    click.echo("3. I have a table and am walking back in")
    click.echo("4. Make a reservation")
    click.echo("5. Go back to the main menu")
    customer_choice = input("Enter your choice: ")

    if customer_choice == '1':
        reservation()
    elif customer_choice == '2':
        walk_in()
    elif customer_choice == '3':
        walking_back()
    elif customer_choice == '4':
        make_reservation()
    elif customer_choice == '5':
        return
    else:
        click.echo("\nInvalid choice, please select a valid option (1, 2, 3, 4, or 5).")
        customers()

def reservation():
    click.echo("\nYou have a reservation. Please proceed to your table.")
    # Implement reservation logic here

def walk_in():
    click.echo("\nYou are here for a walk-in. Please wait to be seated.")
    # Implement walk-in logic here

def walking_back():
    click.echo("\nWelcome back! Please proceed to your table.")
    # Implement walking back logic here

def make_reservation():
    click.echo("\nMaking a reservation.")
    customer_name = input("Please enter your name: ")
    num_people = int(input("Number of people for the reservation: "))
    reservation_time = input("Reservation time (e.g., 7:00 PM): ")

    # Check if a table is available
    available_table = session.query(RestaurantTable).filter_by(is_available=True).filter(RestaurantTable.capacity >= num_people).first()

    if available_table:
        # Mark the table as reserved
        available_table.is_available = False
        session.add(available_table)

        # Add the reservation to the database
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

def quit_app():
    click.echo("Thank you for using the Cario Nights Restaurant Management System. Goodbye!")
    exit()

def handle_user_choice(choice):
    if choice == '1':
        management()
    elif choice == '2':
        employees()
    elif choice == '3':
        customers()
    elif choice == '4':
        quit_app()
    else:
        click.echo("\nInvalid choice, please select a valid option (1, 2, 3, or 4).")

@click.command()
def cli():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        handle_user_choice(choice)

if __name__ == '__main__':
    cli()
