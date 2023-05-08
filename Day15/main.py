MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,        #no milk here
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

finish = True

def order():
    order = input(" What would you like? (espresso/latte/cappuccino): ")
    return order

        #use this shit
#fix checker

def intro():
    global orderMemory
    global finish
    orderMemory= order()
    if ingredientsNeededForDrink() == False:
        finish = False
        return
    changes = coins_entered()
    if changes < MENU[orderMemory]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        changes = changes-(MENU[orderMemory]["cost"])
        print("Here is $",changes," in change.")
#returns if something is missing, else just none
#make list of keys, then iterate
# def resource_checker():
#     if (MENU[orderMemory]["water"]>resources["water"]):
#         return f"Sorry there is not enough water." 
#     elif(MENU[orderMemory]):
#         return 


# if MENU[order]["cost"] > coins_entered():
#         return "Sorry that's not enough money. Money refunded."
#     else:
#         return "Here is $"+coins_entered()-(MENU[order]["cost"])+" in change."


def ingredientsNeededForDrink():
    #if cappy then get ing of cappy and returns all the ing and go to checker if theres enough 
    materials = MENU.get(orderMemory)
    for j in materials['ingredients']:
        if ((MENU[orderMemory]['ingredients'][j]) > resources.get(j)):
            print( f"Sorry there's not enough {j}.")
            return False
        else:   #update value of resources
            resources[j] = resources.get(j) -MENU[orderMemory]['ingredients'][j]
            # resources.update(j,resources.get(j) -MENU[orderMemory]['ingredients'][j])
            print(f"Here is your {orderMemory}. Enjoy!")
            return True



def coins_entered():
    print("please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return  (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)

while (finish):
    intro()
print("machine off")
# price = coins_entered()
