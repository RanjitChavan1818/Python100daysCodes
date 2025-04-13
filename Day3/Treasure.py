print("Welcome on Treasure Game")
choice1=input('enter your choice as "right" or left: ').lower()

if(choice1=="left"):
  print("You in the game")
  choice2=input('You want to "swim" or "wait": ').lower()
  if choice2=="wait":
    choice3=input('Choice the door "Yellow", "Blue","Red": ').lower()
    if choice3=="yellow":
      print("Sorry rum full and you lose the game")
    elif choice3=="red":
      print("You Choose wrong door, Sorry you lose")
    elif choice3=="blue":
      print("You Win. You Find treasure ")
    else:
      print("No door available ")
  else:
    print("Game Over")
else:
  print("game Over")