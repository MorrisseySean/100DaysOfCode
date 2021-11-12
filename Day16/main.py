from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
coffeeMenu = Menu()
moneyManager = MoneyMachine()

is_on = True

while is_on:
    options = coffeeMenu.get_items()
    request = input(f"What drink would you like? ({options}): ")
    if request == "off":
        is_on = False
    elif request == "report":
        coffeeMachine.report()
        moneyManager.report()
    else:
        order = coffeeMenu.find_drink(request)
        if order == "None":
            print(f"Sorry, {request} is not available. Please select another option.")
        elif coffeeMachine.is_resource_sufficient(order)!= True:
            print(f"Sorry, {order.name} is sold out. Please try another option.")
        else:
            print(f"A {order.name} will be ${order.cost}: ")
            if moneyManager.make_payment(order.cost):
                coffeeMachine.make_coffee(order)
