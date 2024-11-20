print("Welcome to the tip calculator.")
bill=float(input("What was the total bill ? "))
print(bill)

tip=int(input("What percentage tip would you like to give ? "))
# print(str(tip) + "%")
print(f"{tip} % ")



people=int(input("How many people to split the bill ? "))
print(people)

total_amount= bill + ((tip/100)*bill)
your_share=round(total_amount/people,2)

print(f"Each person should pay: {your_share}")