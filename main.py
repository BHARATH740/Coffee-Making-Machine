from art import logo


print(logo)
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


def main_func():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'report':
        print_resources(resources)
        return
    else:
        drinks = MENU[drink]
    enough_resources = check_resources(resources, drinks)
    if not enough_resources:
        return
    print("Please insert coins.")
    quarters =0.01 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles =0.05 * int(input("How many nickles?: "))
    pennies = 0.25 * int(input("How many pennies?: "))
    money = quarters + dimes + nickles + pennies
    if money == drinks["cost"]:
        print(f"Here, Enjoy your {drink}!")
        print("Come back soon!!")
        coffee_making(resources, drinks)
    elif money > drinks["cost"]:
        print(f"Here is {money-drinks['cost']} in change")
        print(f"Here, Enjoy your {drink}!")
        print("Come back soon!!")
        coffee_making(resources, drinks)
    else:
        print("Sorry that's not enough money.Money refunded.")
    # print(drinks)


def coffee_making(resources, drinks):
    # print(drinks["ingredients"]["water"])
    resources["water"] -= drinks["ingredients"]["water"]
    resources["milk"] -= drinks["ingredients"]["milk"]
    resources["coffee"] -= drinks["ingredients"]["coffee"]
    resources["money"] += drinks["cost"]


def print_resources(resources):
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}g")
    print(f" Money: ${resources['money']}")


def check_resources(resources, drinks):
    if resources["water"] < drinks["ingredients"]["water"]:
        print("Sorry! Not enough Water")
        print("Sorry for the trouble.")
        return False
    elif resources["milk"] < drinks["ingredients"]["milk"]:
        print("Sorry! Not enough Milk")
        print("Sorry for the trouble.")
        return False
    elif resources["coffee"] < drinks["ingredients"]["coffee"]:
        print("Sorry! Not enough Coffee powder")
        print("Sorry for the trouble.")
        return False
    else:
        return True


run_loop = True
while run_loop:
    main_func()

