from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "quarters": 0.25,
    "dimes" : 0.10,
    "nickels" : 0.05,
    "pennies" : 0.01
}

EMPTY = False

def coffeeMachine():
    usrval = input("What would you like? (espresso/latte/cappuccino): ")
    if usrval in MENU.keys():
        coins = COINS.copy()
        print("Please insert coins: ")
        for k,v in COINS.items():
            val = int(input(f"How many {k}: "))
            COINS[k] = val*COINS[k]
        if sum(COINS.values()) >= MENU[usrval]["cost"]:
            x = sum(COINS.values()) - MENU[usrval]["cost"]
            change = round(x, 2)
            print(f"Here is your ${change} in change.")
            print(f"Here is you {usrval} Enjoy!")
            resourceSub(usrval)
            resourceCheck()
            if not EMPTY:
                for k in COINS and coins:
                    COINS[k] = coins[k]
                coffeeMachine()
        else:
            print("Please insert the right amount of money")
            coffeeMachine()
    elif usrval == "report":
        for k,v in resources.items():
            print(k,v)
        coffeeMachine() 
    else:
        print("Invalid input!")

def resourceSub(i):
    used = MENU[i]["ingredients"]

    for k, v in used.items():
        if k in resources:
            resources[k] = resources[k] - v
        
def resourceCheck():
    global EMPTY
    for k,v in resources.items():
        if v <= 0:
            EMPTY = True
            print(f"need a refill of {k}")

coffeeMachine()