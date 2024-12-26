from game_data import data
from art import logo
from art import vs
import random
import os





def check_guess(a,b,score):
 
    user_guess=input("Who has more followers? Type 'A' or 'B':  ").lower()
    print(user_guess)

    if (a['follower_count'] > b['follower_count'] and user_guess=='a')or (a['follower_count']<b['follower_count'] and user_guess=='b'):
        
        score +=1
        print(f'You are right. Your score is {score}')
        return True,score 
        
    else:
        print(f'You are wrong. Your score is {score}')
        return False,score



game_continue=True
score=0
b=random.choice(data)


while game_continue:
    os.system('cls')

    print(f"Your score is {score}")

    
    a=b
    b=random.choice(data)
   

    if a==b:
        b=random.choice(data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a["country"]} .")

    print(vs)

    print(f"Compare B: {b['name']}, a {b['description']}, from {b["country"]} .")

    

    game_continue,score=check_guess(a,b,score)

  
    

        




# display art
#generate random account
#format the account data into printab;e format
#ask user for guess
#check if user is correct
#get follower count of each account
#use if statement to check if user is correct
#give feedback on their guess
#score keeping
#make game repeatable .
# make account at position B become the next account at postion A.
#clear the console
