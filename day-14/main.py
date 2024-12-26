from game_data import data
from art import logo
from art import vs
import random

data_length=len(data)
data_index=random.randint(0,data_length)

first_set=data[data_index]
second_set=data[data_index]


print(logo)

print(f"Compare A: {first_set['name']}, a {first_set['description']}, from {first_set["country"]} .")

print(vs)

print(f"Compare B: {second_set['name']}, a {second_set['description']}, from {second_set["country"]} .")

user_guess=input("Who has more followers? Type 'A' or 'B':  ").lower()
print(user_guess)
