print("Welcome to python pizza ")
size=input("Enter Size of Pizza S,M & L: ")
paperoni=input("Enter for Paperoni y: ")
extra=input("Enter y for extra chees: ")
bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20

elif size=="L":
    bill+=25
else:
    print("You enter wrong size")

if paperoni=="y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra=="y":
    bill+=1

print(f"You Have to pay final amount {bill}")    
        

