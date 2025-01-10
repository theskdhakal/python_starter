# import random
# import my_module




# # way to generate the random integer in pyhton

# random_integer= random.randint(1,100)
# print(random_integer)

# # Module
# print(my_module.pi)


# # generate random floating points
# random_floating=random.random() 
# # the code above genrate random float number between 0 and 1

# random_floating_between=random.uniform(1.5,7.8)
# print(random_floating_between)

# print(random_floating)


# _______________________________________Understanding the offset and Appending items to Lists________________________________________________
# Lists
states_of_america=["Delaware", "colorado", "Iowa", "....."]


# to alter the list// using the index , any list items can be indexed  and henced updated
states_of_america[1]="colo"

print(states_of_america)


# to add the item in list
states_of_america.append("Shivaland")



# add other list to the list
states_of_america.extend(["abcd","defg"])

print(states_of_america)



# __________________________________________________________________________________________________________________________________
# ________________________________________Index errors and working with Nested Lists_________________________________________________
# ___________________________________________________________________________________________________________________________________


boys=["ram","shyam","shiva"]
girls=["sita","gita","rita"]
# classroom is the nested list
classroom=[boys,girls]


