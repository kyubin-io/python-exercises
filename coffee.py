
from coffee_menu import MENU, resources


money = 0

def report():
    print(f"{resources["water"]}ml")
    print(f"{resources["milk"]}ml")
    print(f"{resources["coffee"]}g")
    print(f"${money}")


while True :
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    print(coffee)

    if coffee == "report":
        report()

    else:
        print("Please insert coins.")

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        sum = quarters + dimes + nickles + pennies

        
        if sum < MENU[coffee]["cost"] :
            print("not enough money")
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print(f"Sorry there is not enough milk.")
        if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
        else :
            money = sum - MENU[coffee]["cost"]

            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

            print(f"Here is ${money} in change.")
            print(f"Here is your {coffee} Enjoy!")



