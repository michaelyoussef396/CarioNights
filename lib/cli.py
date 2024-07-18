import click

def print_menu():
    click.echo("Welcome to the Cario Nights Restaurant And Bar!")
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
    click.echo("Customer options are under development. Please check back later.")

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
