from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


is_on = True
profit = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffeeMaker.report())
        print(f"Money : ${profit}")
    else:
        drink = menu(choice)
        if coffeeMaker.is_resource_sufficient(drink["ingredients"]):
            payment = moneyMachine.process_coins()
            if coffeeMaker.is_transaction_successful(payment, drink["cost"]):
                coffeeMaker.make_coffee(choice, drink["ingredients"])

