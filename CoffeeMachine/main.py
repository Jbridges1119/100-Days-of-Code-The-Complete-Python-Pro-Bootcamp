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

def total_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)

    return total
    
    
def drink_question():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
      choice = input("Invalid input. What would you like? (espresso/latte/cappuccino): ").lower()
      
    return choice


def verify_resources(drink_ingredients, resources):
    for item, value in drink_ingredients.items():
      if (value > resources[item]):
        print(f"Sorry there was not enough {item}.")
        return False
    
    return True

  
def remove_resources(drink_ingredients, resources):
    for item, value in drink_ingredients.items():
        resources[item] -= drink_ingredients[item]
      

def coffee_machine(MENU, resources):
  serving = True

  while serving:
    choice = drink_question()
    drink_ingredients = MENU[choice]['ingredients']

    if verify_resources(drink_ingredients,resources):
      payment = total_payment()
      drink_cost = int(MENU[choice]['cost'])

      if (drink_cost < payment):
        return_value = float(payment) - float(drink_cost)
        
        remove_resources(drink_ingredients, resources)
        
        rounded_return_value = "{:.2f}".format(round(return_value, 2))
        print(f"Here is ${rounded_return_value} in change.")
        print(f"Here is your {choice} ☕️. Enjoy!")
      else: 
        print("Sorry that's not enough money. Money refunded.")
    
coffee_machine(MENU, resources)