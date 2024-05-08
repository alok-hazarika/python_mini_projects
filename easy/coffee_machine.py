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
    "Water" : 200,
    "Milk"  : 200,
    "Coffee": 100,
    "Money" : 1.5
}


is_active = True
available_bal = 0

###################################
# make coffee function
###################################

def make_coffee(choice):
    global revenue, available_bal
    if choice == "espresso":
        if MENU[choice]["cost"] <= available_bal:
            resources["Water"] -= MENU[choice]["ingredients"]["water"]
            resources["Coffee"] -= MENU[choice]["ingredients"]["coffee"]   
            resources["Money"] += MENU[choice]["cost"]
            available_bal -= MENU[choice]["cost"]
            print("Here is your", choice, "and your change", round(available_bal,2))
        else:
            print("Still insufficient money! Refunded")
    else:
        if MENU[choice]["cost"] <= available_bal:
            resources["Water"] -= MENU[choice]["ingredients"]["water"]
            resources["Milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["Coffee"] -= MENU[choice]["ingredients"]["coffee"]     
            resources["Money"] += MENU[choice]["cost"]
            available_bal -= MENU[choice]["cost"]
            print("Here is your", choice, "and your change", round(available_bal,2))
        else:
            print("Still insufficient money! Refunded")

###################################
# load money to wallet
###################################

def load_money(choice):
    global available_bal
    available_bal = round((int(input("How many quarters?: "))) * 0.25, 2)
    available_bal += round((int(input("How many dimes?: "))) * 0.10, 2)
    available_bal += round((int(input("How many nickels?: "))) * 0.05, 2)
    available_bal += round((int(input("How many pennies?: "))) * 0.01, 2)
    print("Money addded", available_bal)
    make_coffee(choice)


###################################
# check for sufficient money
###################################

def is_sufficient_money(choice):
    if MENU[choice]["cost"] <= available_bal:
        print("Sufficient Money for", choice)
        make_coffee()
    else:
        print("Insufficient Money for", choice,"! Please add some coins")
        load_money(choice)
        

# ###################################
# # check for sufficient ingredient
# ###################################

def is_sufficient_ingredients(choice):
    if MENU[choice]["ingredients"]["water"] <= resources["Water"]:
        print("Sufficient Water")
        is_sufficient_money(choice)
    else:
        print("Insufficient water")

# ###################################
# # Loop while machine is on
# ###################################


while is_active:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "off":
        quit()
    elif prompt == "report":
        print(
            f"Water: {resources['Water']}ml\nMilk: {resources['Milk']}ml\nCoffee: {resources['Coffee']}\nMoney: ${resources['Money']}"
            )
    elif prompt == "espresso":
        is_sufficient_ingredients(prompt)       
    elif prompt == "latte":
        is_sufficient_ingredients(prompt)
    elif prompt == "cappucino":
        is_sufficient_ingredients(prompt)
