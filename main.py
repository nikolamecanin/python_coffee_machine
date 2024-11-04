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
}

# TODO 1. Print report of all coffee machine resources
# Checking resources, turn off machine and print report


valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]
condition = True

while condition:
    desire = input("What would you like? (espresso/latte/cappuccino): ")
    if desire not in valid_choices:
        print("Wrong Input. Try again.")
        continue
    if desire == "off":
        condition = False
        exit()
    if desire == "report":
        print(resources)
        continue

    if desire == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
    if desire == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            continue
    if desire == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            continue
    # Coins insert and check transaction succesful


    print("Insert coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes : "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total_amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    print(f"You inserted {total_amount} $")
    resources["Money :"] = 0
    change = 0
    if MENU[desire]["cost"] > total_amount:
        print("Sorry that's not enough money. Money refunded")
    else:
        resources["water"] -= MENU[desire]["ingredients"]["water"]
        resources["coffee"] -= MENU[desire]["ingredients"]["coffee"]
        if "milk" in MENU[desire]["ingredients"]:
            resources["milk"] -= MENU[desire]["ingredients"]["milk"]

        resources["Money :"] +=total_amount
        change = total_amount - MENU[desire]["cost"]
        if change > 0:
            print(f"Here is {change:.2f} dollars in change")
            resources["Money :"] -=change









