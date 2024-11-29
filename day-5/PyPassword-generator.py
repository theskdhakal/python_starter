import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   

numbers=["1","2","3","4","5","6","7","8","9","0"]

symbols=["!","@","#","$","%","^","&","*"]


print("Welcom to pypassword generator")

nr_letters=int(input("How many letters would you like in your password? \n"))
nr_symbols=int(input("How many symbols would you like in your password? \n"))
nr_numbers=int(input("How many numbers would you like in your password? \n"))

# //choosing the multiple items from array  depending upon number of required items
random_letters=random.sample(letters,nr_letters) #// choose random sample of length nr_letters from letters array
random_symbols=random.sample(symbols,nr_numbers)
random_numbers=random.sample(numbers,nr_symbols)

random_password_list=random_letters + random_symbols + random_numbers

print(random_password_list)




# shuffle the items in array
random.shuffle(random_password_list)


random_password=''.join(random_password_list)
print(random_password)



# ______________________________________________________________________________________
#                         second way
# _______________________________________________________________________________________

# password_list=[]
# for char in range(1,nr_letters +1):
#     password_list.append(random.choice(letters))


# for char in range(1,nr_numbers+1):
#     password_list+=random.choice(numbers)

# for char in range(1,nr_symbols+1):
#     password_list += random.choice(symbols)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)


# password=""
# for item in password_list:
#     password +=item

# print(password)