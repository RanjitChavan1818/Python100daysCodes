print("Welcome to thr Roller Coster")
height=int(input("Enter you height"))

if height>=120:
    print("You can ride")
    age=int(input("Enter your age "))
    if age<=12:
        print("Please Pay 5$")
    elif age<=18:
        print("Please Pay 7$")
    else:
        print("Please Pay 12$")
else:
    print("Sorry you need to grow")
