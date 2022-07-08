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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True


def process_coin():
    print("Please Insert the coins.")
    total = int(input("How many quarters ?"))*0.25
    total += int(input("How many dimes ?"))*0.1
    total += int(input("How many nickels ?"))*0.05
    total += int(input("How many pennies ?"))*0.01
    return total


def is_transaction_successful(money_received, order_cost):
    if money_received >= order_cost:
        change = round(money_received - order_cost, 2)
        print(f"Here is a ${change} in change.")
        global profit
        profit += order_cost
        return True
    else:
        print(f"You have an insufficient amount.")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your drink {drink_name}")


is_on = True
while is_on:
    choice = input("Which drink do you want espresso/latte/cappuccino ?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"milk: {resources['milk']}ml")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



