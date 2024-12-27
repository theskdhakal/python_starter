import os
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
    "water": 250,
    "milk": 200,
    "coffee": 100,
}


is_machineOn=True




def selected_coffee_data(coffee):
    req_water=MENU[coffee]['ingredients']['water']
    req_coffee=MENU[coffee]['ingredients']['coffee']
    req_milk=MENU[coffee]['ingredients'].get('milk',0)
    total_cost=MENU[coffee]['cost']

    return req_water,req_coffee,req_milk,total_cost


def check_sufficient_resources(req_water,req_coffee,req_milk):
    if req_water > resources['water']:
        print("Not enough water in machine")
        return False
    if req_milk >resources['milk']:
        print('Not enough milk in machine')
        return False
    if req_coffee > resources['coffee']:
        print('Not enough coffee in machine')
        return False
    return True


def inset_coins(total_cost):
    quarters_inserted=int(input("How many quarters do you want to insert ?: "))
    dimes_inserted=int(input("How many dimes do you want to insert ?: "))
    nickles_inserted=int(input("How many nickles do you want to insert ?: "))
    pennies_inserted=int(input("How many pennies do you want to insert ?: "))

    total_amount_paid= float((quarters_inserted *0.25)+(dimes_inserted*0.10)+(nickles_inserted*0.05)+(pennies_inserted*0.01))

    if total_amount_paid < total_cost:
        print("Sorry that's not enough money. Money refunded")
    else:
        resources['money'] =resources.get('money',0) + total_cost

        if total_amount_paid > total_cost:
            change_back=total_amount_paid -total_cost
            rounded_change_back=round(change_back,2)

            print(f"Here is ${rounded_change_back} dollar  in change. ")



while  is_machineOn:
    coffee_type=input("What would you like? (espresso/latte/cappuccino): ").lower()

    os.system('cls')

    if coffee_type in MENU:
        water_needed, coffee_needed, milk_needed,final_cost =selected_coffee_data(coffee_type)

        if check_sufficient_resources(water_needed, coffee_needed, milk_needed,):
                 inset_coins(final_cost)

                 print(f'preparing your {coffee_type}')

                 resources['water'] -= water_needed
                 resources['coffee'] -= coffee_needed
                 resources['milk'] -=milk_needed

                 print(f"Here is your {coffee_type}.Enjoy !")

    elif coffee_type == 'report':
            print(resources)
    elif coffee_type == 'off':
            print("Coffee Machine is turned off for maintenance. Please check in later")
            is_machineOn=False
    else:
        print('Invalid choice')












# TODO: 1. print report



# TODO: 2. Check if sufficient resources is avialable


# TODO: 3. Process the coin


# TODO: 3. Check if transaction is successful