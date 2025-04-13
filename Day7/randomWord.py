import random
word_list=["ranjit","abhishek","vaibhav","laxman"]
word=random.choice(word_list)
print(word)


  
guess=input("Guess a letter").lower()
print(guess)



for letter in word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")