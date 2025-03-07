MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 35,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry the {item} is not Sufficient.")
            return False
    return True


def process_coins():
    print("Please Insert Coins!")
    total = int(input("Enter the Number of 1 rs coins: "))
    total += int(input("Enter the Number of 2 rs coins: ")) * 2
    total += int(input("Enter the Number of 5 rs coins: ")) * 5
    total += int(input("Enter the Number of 10 rs coins: ")) * 10
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your Change of Rs. {change}!")
        global profit
        profit += drink_cost
        return True
    else:
        print("The Payment is not Sufficient, Transaction Declined!")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like?(Espresso/Latte/Cappuccino)\n")
    choice = choice.lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk = {resources["milk"]}")
        print(f"Water = {resources["water"]}")
        print(f"Coffee = {resources["coffee"]}")
        print(f"Profit = Rs. {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
