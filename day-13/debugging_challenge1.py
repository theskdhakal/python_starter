# number=int(input("give a number : "))

# if number % 2==0:
#     print("This is a even number")
# else:
#     print("This is a odd number")


year=int(input("Whic year to check ? "))


if year % 4==0:
    if year%100==0:
        if year %400==0:
            print("Leap year")
        else:
            print("No leap year")
    
    else:
        print("leap year")
else:
    print("no leap year")