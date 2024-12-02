programming_dictionary={

    "Bug":"An error in program that prevent it from running as expected" ,
    "Function":"A piece of code that you can easily call over and over again"

}

# retrieving item from dictionary
print(programming_dictionary["Bug"])


# adding new itms to dictionary
programming_dictionary["Loop"]="The action of doing something over and over again"


#creat an empty_dictionary
empty_dictionary={}

#wipe an exisitng dictionary
# programming_dictionary={}


#edit an dictionary
programming_dictionary ["Bug"]="kira"

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])