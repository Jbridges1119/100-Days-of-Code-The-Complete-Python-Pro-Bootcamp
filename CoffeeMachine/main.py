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

# Totals up customer payment
def calculate_change(drink_cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    return_value = float(total) - float(drink_cost)
    if drink_cost < total:
      return "{:.2f}".format(round(return_value, 2))
      
    return False
    
    
    
# Handles initial drink question with secret choices
def drink_question():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if (choice == 'off'):
      return False
    
    while choice != 'espresso' and choice != 'latte' and choice != 'cappuccino' and choice != 'report':
      choice = input("Invalid input. What would you like? (espresso/latte/cappuccino): ").lower()
      
    return choice

# Verifies enough resources are present to make coffee
def verify_resources(drink_ingredients, resources):
    for item, value in drink_ingredients.items():
      if (value > resources[item]):
        print(f"Sorry there was not enough {item}.")
        return False
    
    return True

# Handles removing resources when coffee is made
def remove_resources(drink_ingredients, resources):
    for item, value in drink_ingredients.items():
        resources[item] -= drink_ingredients[item]

# Handles reporting remaining resources
def report_resources(resources):
    for item, value in resources.items():
      match item:
        case 'coffee':
          formatted_value = str(value) + 'g'
        case 'money':
          formatted_value = '$' + str(value)
        case _:
          formatted_value = str(value) + 'ml'
      
      print(f"{item.capitalize()}: {formatted_value}")

# Handles adding money to resources and formatting return value
def process_transaction(drink_cost):
    if 'money' in resources:
      resources['money'] += "{:.2f}".format(round(drink_cost, 2))
    else:
      resources['money'] = "{:.2f}".format(round(drink_cost, 2))
  
  
def coffee_machine(MENU, resources):
  choice = True

  while choice:
    choice = drink_question() 
    
    if choice == False:
      return
    elif choice == 'report':
      report_resources(resources)
    else:
      drink_ingredients = MENU[choice]['ingredients']
      drink_cost = int(MENU[choice]['cost'])
      
      if verify_resources(drink_ingredients,resources):
        return_value = calculate_change(drink_cost)
        
        if return_value:
          process_transaction(drink_cost)
          remove_resources(drink_ingredients, resources)

          print(f"Here is ${return_value} in change.")
          print(f"Here is your {choice} ☕️. Enjoy!")
        else: 
          print("Sorry that's not enough money. Money refunded.")
    
coffee_machine(MENU, resources)