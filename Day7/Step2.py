import random
word_list=["ranjit","abhishek","vaibhav","laxman"]
word=random.choice(word_list)
print(word)
length=len(word)
for i in range(length):
    print("_",end=" ")
print()    
guess=input("Guess a letter").lower()
print(guess)



for letter in word:
    if letter == guess:
        print(letter,end=" ")
    else:
        print("_",end=" ")