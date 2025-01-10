print("Welcome to Python Pizza deliveries !")

size=input("What size pizzqa do you want ? S , M , or L ").upper()

print(size)

price=0

if size=="S":
    price=15
    print(f"Price of pizza is ${price}")
if size=="M":
     price=20
     print(f"Price of pizza is ${price}")
if size=="L":
      price=25
      print(f"Price of pizza is ${price}")



pepporini=input("Do you want pepporoni ? Y or N ").upper()
if pepporini=="Y" :
    if size=="S":
         price += 2
    else:
         price +=3

cheese=input("Do you want cheese in your pizza ? Y or N ").upper()
if cheese=="Y":
     price +=1

print(f"Total price of your pizza is {price}")



 