import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_choice=int(input("Enter choice 0 for rock, 1 for Paper, 2 for Scissor: "))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer choose")
print(game_images[computer_choice])   

if user_choice>=3 and user_choice<0:
    print("Invalid choice, type correct choice")

elif user_choice==0 and computer_choice==2: # rock beat scessisor
    print("You Win!")
elif computer_choice==0 and user_choice==2:
    print("You Loose!")
elif computer_choice>user_choice:
    print("you Loose!")
elif user_choice>computer_choice:
    print("You Win!")    

elif computer_choice==user_choice:
    print("Draw")