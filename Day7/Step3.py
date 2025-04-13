import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["ranjit","abhishek","vaibhav","laxman"]
word=random.choice(word_list)
print(word)
length=len(word)
placeholder=""
for i in range(length):
    placeholder+="_"
print(placeholder)
Game_Over=False
check_Letters=[]
lives=6
while not Game_Over:  

    guess=input("Guess a letter").lower()
    print(guess)


    display=""


    for letter in word:
        if letter == guess:
            display+=letter
            check_Letters.append(letter)
        elif letter in check_Letters:
            display+=letter

        else:
            display+="_"
 
    if guess not in word:
        lives-=1
        if lives==0:
            Game_Over=True
            print("You Loose")        
   
    if "_" not in display:
        Game_Over=True
        print("You Win")

    print(stages[lives])    


  
    print(display)        