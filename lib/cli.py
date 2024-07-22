import click
from db.models import Reservation, RestaurantTable, WaitingList, PaymentRequest, session
from helpers import (
    order_item, print_bill, view_menu, make_reservation, walk_in, reservation, 
    view_shisha_heads, view_drinks, view_food, order_shisha_head, order_drink, 
    order_food, check_order_status, give_feedback
)

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

def walking_back():
    customer_name = input("Please enter your name: ")
    reservation = session.query(Reservation).filter_by(customer_name=customer_name).first()
    if reservation:
        table = session.query(RestaurantTable).filter_by(id=reservation.table_number, is_available=False).first()
        if table:
            click.echo(f"\nWelcome back, {customer_name}! Please proceed to your table number {table.table_number}.")
            customer_interaction_menu()
        else:
            click.echo("\nNo occupied table found for your reservation. Please check with the reception.")
    else:
        click.echo("\nNo reservation found for your name. Please check with the reception.")

def customer_interaction_menu():
    while True:
        click.echo("\nCustomer Interaction Menu:")
        click.echo("1. View menu")
        click.echo("2. Order item")
        click.echo("3. Check order status")
        click.echo("4. Give feedback")
        click.echo("5. Print bill")
        click.echo("6. Go back")
        interaction_choice = input("Enter your choice: ")

        if interaction_choice == '1':
            view_menu()
        elif interaction_choice == '2':
            order_item()
        elif interaction_choice == '3':
            check_order_status()
        elif interaction_choice == '4':
            give_feedback()
        elif interaction_choice == '5':
            print_bill()
        elif interaction_choice == '6':
            return
        else:
            click.echo("\nInvalid choice, please select a valid option (1, 2, 3, 4, 5, or 6).")

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