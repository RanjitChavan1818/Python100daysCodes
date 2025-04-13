#hard Password
import random
print("Welcome to the password generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']


n_letters=int(input("How many letters do you want in password? --> "))
n_symbol=int(input("How many symbols you want in password? -->"))
n_numbers=int(input("How many numbers you want in password? -->"))


password_list=[]
for letter in range(0,n_letters):
    password_list.append(random.choice(letters))

for letter in range(0,n_symbol):
    password_list.append(random.choice(symbols))

for letter in range(0,n_numbers):
    password_list.append(random.choice(numbers))
#I used shuffle to shuffle letters inside a list
random.shuffle(password_list) 

#initialize empty password

password="" 
for i in password_list:
    password+=i
print(password)    