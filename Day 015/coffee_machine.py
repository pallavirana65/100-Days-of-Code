# Day 15 Project - The Coffee Machine
# This project allows the user to choose a drink (espresso, latte, or cappuccino).
# The code checks if there are enough ingredients for the drink. If there are enough ingredients, the user enters money.
# Finally, the code calculates and gives the user back change and their drink.
# Secret inputs: If the user enters "report" instead of a drink name, it will print the amount of each ingredient left
# in the coffee machine. If the user enters "off", then the coffee machine will turn off.

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


profit = 0


def check_resources(order_ingredients):
    """Returns True when order can be made, or False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins. ')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickels?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry, that is not enough money. Money refunded.')
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕. Enjoy!')


is_on = True


while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


