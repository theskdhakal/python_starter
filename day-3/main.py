print("Welcome to the rollercoaster !")
height=int (input("What is your height in cm ? "))



if height == 120:
    print("You can ride the rollercoaster !")
    age=int(input("whats your age? "))
    if age <12:
        print("$5")
    elif 12<age<18:
         print("$10")
    else:
         print("$20")
else:
    print("sorry")



# ______________________________________check the odd or even program_____________________________________________

number=int(input("which whole number you want to check ? "))

remainder=number%2

if remainder ==1 :
    print("odd")
else:
    print("Even")