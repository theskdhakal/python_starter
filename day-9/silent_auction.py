from art import logo

print(logo)

print('++++++++++++++++++++++++++WELCOME TO SILENT AUCTION++++++++++++++++++++++++++++++++++++')

bid_list=[]

# def add_bid


def silent_auction(name,bid):
    new_bid={
        "name":name,
        "amount":bid
    }
    
    bid_list.append(new_bid)

    highest_bid=0
    winner=''
    for bid in bid_list:
       if bid["amount"] > highest_bid:
           highest_bid=bid["amount"]
           winner=bid["name"]
    

    print(f"The highest bid is {highest_bid} by {winner}")

    



while True:
    name=input("What's name of bidder? :")
    amount=input("What is the bid amount? :")

    silent_auction(name=name,bid=int(amount))

    more_bid=input("Are the more bidder? Y or N").lower()
    



    if more_bid != 'y':

        print("finished")