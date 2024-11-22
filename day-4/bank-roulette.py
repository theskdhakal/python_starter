import random
name=input("Give me name of everyone, seperated by comma: ")

name_list=name.split(",")
last_index=len(name_list)-1

random_number=random.randint(0,last_index)

unlucky_guy=name_list[random_number]

print(f"{unlucky_guy} will pay for food today")

