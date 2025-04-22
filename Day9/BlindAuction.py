import art
print(art.logo)

def find_highest_buiding(buiding_dictionary):
    winner=""
    highest_bid=0
    for bidder in buiding_dictionary:
        bid_amount=buiding_dictionary[bidder]  
        if bid_amount> highest_bid:
            highest_bid=bid_amount 
            winner=bidder  
    print(f"The winner is {winner} with a bid of ${highest_bid}.")            
bids={}
continue_buiding=True

while continue_buiding:
    name=input("Enter your name: ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue=="no":
        continue_buiding=False
        find_highest_buiding(bids)
    else:
        print("\n"*20)

