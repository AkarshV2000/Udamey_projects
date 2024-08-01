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

def is_resource_suuficient(order_ingredient):
    """ReturnsTrue when order can be made else return False if Ingredients are
        insufficient"""
    for item in order_ingredient:
        if order_ingredient[item]>= resources[item]:
            print(f"Sorry! not enough {item}")
            return False
    return True

def process_coin():
    """Returns the total sum of coins inserted"""

    print("Please! insert coins")
    total = int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1 
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transaction_succesfull(money_recieved, cost_of_the_drink):
    """Returns True if payment is successfull else returnFalse if payment is insufficient"""

    if money_recieved>= cost_of_the_drink:
        change = round(money_recieved - cost_of_the_drink, 2)
        print(f"Here is ${change} in change")
        global profit
        profit+= cost_of_the_drink
        return True
    else:
        print("Sorry!not enough money. Money is refunded!")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink: {drink_name} ")


profit = 0
is_on = True
while is_on:
    choice= input(" what you'd like to take: espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"water: {resources['water']}ml")
       print(f"milk:  {resources['milk']}ml")
       print(f"coffee:{resources['coffee']}g")
       print(f"money: ${profit}")
    else:
        drink = MENU[choice] 
        if is_resource_suuficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])