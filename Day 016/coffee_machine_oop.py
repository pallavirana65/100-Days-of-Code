# Day 16 Project - Coffee Machine with OOP (Object Oriented Programming)
# We recreated the Coffee Machine project from Day 15 using the concepts of Classes and Objects with Attributes
# and Methods. The goal was to simplify the code by creating Objects and then calling the methods and attributes
# already defined in the instructor-provided Classes.


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)