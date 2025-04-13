print("Welcome to the bill tip calculator")
bill=float(input("Enter you Bill?"))
tip=int(input("How much percent tip you would like to give 10 , 12 or 15?"))
split=int(input("How many people split the bill?"))
tip_per=tip/100
amount_tip=tip_per*bill
total_amount=bill+amount_tip
each_person=total_amount/split

print(f"Each should pay {each_person}$")