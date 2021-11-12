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
    "money": 0
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes" : 0.10,
    "quarters": 0.25
}

def check_resources(drink_ingredients):
    available = True
    for ingredient in drink_ingredients:
        if resources[ingredient] - drink_ingredients[ingredient] < 0:
            print("Not enough", ingredient)
            available = False
    return available

def print_report():
    for resource in resources:
        text = ""
        if resource == "money":
            text = "$" + str(round(resources[resource], 2))
        elif resource == "coffee":
            text = str(resources[resource]) + 'g'
        else:
            text = str(resources[resource]) + 'ml'
        print(resource + ' : ' + text)

quit = False
while quit!= True:
    choice = {}
    total = 0.0
    answer = input("What would you like? (cappuccino, latte or espresso):  ")
    if answer == "off":
        print("Shutting down...")
        quit = True
        continue
    elif answer == "report":
        print_report()
    else:
        for drink in MENU:
            if drink == answer:
                if check_resources(MENU[drink]["ingredients"]): 
                    choice = MENU[drink]
        if choice:
            total = choice["cost"]
            print("That will be $", total)
            text = ""
            for coin in coins:
                text = "How many " + coin + "?: "
                total = total - ( eval(input(text)) * coins[coin] ) 
            if total > 0:
                print("Not enough money, please try again")
            else:
                for resource in choice['ingredients']:
                    resources[resource] = resources[resource] - choice["ingredients"][resource]
                resources["money"] += choice["cost"]
                print(f"Thanks! Your change is: {str(round((total * -1.0), 2))}") 
        else:
            print("Sorry,", answer, "is not available, please try again.") 