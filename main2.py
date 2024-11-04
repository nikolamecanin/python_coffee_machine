MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]


def print_report():
    """Prints the current resources of the coffee machine."""
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}")


def check_resources(drink):
    """Checks if there are enough resources for the requested drink."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Processes the coins inserted by the user and returns the total amount."""
    print("Insert coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total_amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    print(f"You inserted {total_amount:.2f} $")
    return total_amount


def make_coffee(drink):
    """Deducts the required ingredients from resources and adds money."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine."""
    while True:

        desire = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if desire not in valid_choices:
            print("Wrong Input. Try again.")
            continue
        if desire == "off":
            break
        if desire == "report":
            print_report()
            continue


        if check_resources(desire):
            total_amount = process_coins()
            if total_amount < MENU[desire]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total_amount - MENU[desire]["cost"]
                if change > 0:
                    print(f"Here is {change:.2f} dollars in change.")
                make_coffee(desire)


coffee_machine()