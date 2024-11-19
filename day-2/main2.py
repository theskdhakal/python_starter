# Data types 

# String

"Hello"

print("124"+"432")

#integer

print(123 + 456)

#float -- floating point number ( the one with decimal)

1.43476

#boolean
True
False




# ****************************challenge DAY 2 ********************************

three_digit_number=input("Enter a three digit number: ")
print(three_digit_number)


print(int(three_digit_number[1]) + int(three_digit_number[2]) + int(three_digit_number[0]))


# Mathematical operation
# ** ----- gives exponention value
# 2 ***3 it means 2 power 3 i.e 2*2*2 

print (3+3*3/3-3)


# ************************ BMI CALCULATOR ***********************************************
height=float(input('enter your height in m: '))
weight=float(input('enter your weight in kg: '))


BMI= (weight)/(height * height)

print(int(BMI))



# rounding off the number 
# print (round(9/2,4))  -- 4 denote the decimal places to be round off 
# print(8//3)-flow division, just gives the whole number 

# maniputing the value using previous value
# score = 0

# score += 1 // increase score by 1
# score -=1 // decrease score by 1


#  ------------------- f-String ------------------------------
score = 0
height=1.8
isWinning =True

#f-string

print(f"your score is {score}, your height is {height}")
# using f string convert type itself ,thus eliminating the need of converting type conversion and concatenation using + sign


