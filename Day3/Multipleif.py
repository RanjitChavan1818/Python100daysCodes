print("Welcome to thr Roller Coster")
height=int(input("Enter you height"))
bill=0

if height>=120:
    print("You can ride")
    age=int(input("Enter your age "))
    if age<=12:
        bill=5
        print("Please Pay 5$")
    elif age<=18:
        bill=7
        print("Please Pay 7$")
    else:
        bill=12
        print("Please Pay 12$")
    want_photo=input("If you want to photo then say y otherwise n")
    if want_photo=='y':
        bill+=3
    print(f"You have to pay total bill{bill}$")        
else:
    print("Sorry you need to grow")
