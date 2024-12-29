from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# TODO 1: print report
my_coffee_maker=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()


is_on=True


#TODO 2: check resources sufficient


#TODO 3: Process coins

# TODO 4: check transaction successful ?

while is_on:
    option=menu.get_items()
    choice=input(f"what would you like ? ({option}) : ")

    if choice=='off':
        is_on=False
    elif choice =='report':
        my_coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)







# TODO 5: Make Coffee