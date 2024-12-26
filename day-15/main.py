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


is_machineOn=True





def selected_coffee_data(coffee):

    req_water=MENU[coffee]['ingredients']['water']
    req_coffee=MENU[coffee]['ingredients']['coffee']
    req_milk=MENU[coffee]['ingredients'].get('milk',0)
    total_cost=MENU[coffee]['cost']
    print(req_water,req_coffee,req_milk,total_cost)


coffee_type=input("What would you like? (espresso/latte/cappuccino): ").lower()

if coffee_type == 'espresso':
        selected_coffee_data('espresso')
elif coffee_type == 'latte':
        print('latte')
elif coffee_type == 'cappuccino':
        print('cappuccino')
elif coffee_type == 'report':
        print(resources)
elif coffee_type == 'off':
        is_machineOn=False
else:
    print('Invalid choice')
#









# TODO: 1. print report



# TODO: 2. Check if sufficient resources is avialable


# TODO: 3. Process the coin


# TODO: 3. Check if transaction is successful