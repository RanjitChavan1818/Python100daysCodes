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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
   # returns True when order can be made, false if ingredients are insufficient
   for item in order_ingredients:
     if order_ingredients[item]>= resources[item]:
       print(f"Sorry there is not enough {item}.")
       return False
   return True

def process_coins():
  # returns total calculated amount from the inserted coins🪙
  print("please insert coins.")
  total=int(input("how many quarters?: "))*0.25   
  total+=int(input("how many dines?: "))*0.1 
  total+=int(input("how many nickels?: "))*0.05   
  total+=int(input("how many pennies?: "))*0.01 
  return total  

def is_transaction_successful(money_received, drink_costs):
  # return True when the payment is accepted , or false if money is insufficient
  if money_received>= drink_costs:
    change=round(money_received-drink_costs,2)
    print(f"Here is $ {change} is change.")
    global profit
    profit+= drink_costs
    return True
  else:
    print("Sorry that's do not have enough money. Money refunds")
    return False
  
def make_cofee(drink_name,order_ingredients):
  #deduct the required ingredients in the resources 
  for item in order_ingredients:
    resources[item]-=order_ingredients[item]
  print(f"Here is your {drink_name} ☕")  

is_on=True
while is_on:
  choice=input('“What would you like? (espresso/latte/cappuccino):”')
  if choice =='off':
   is_on=False
  elif choice=="report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit}")
  else:
    drink=MENU[choice]
    if is_resources_sufficient(drink["ingredients"]):
      payment=process_coins()
      if is_transaction_successful(payment,drink["cost"]):
       make_cofee(choice,drink["ingredients"])