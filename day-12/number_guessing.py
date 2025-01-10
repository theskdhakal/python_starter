import random


EASY_LEVEL_TURNS=10         
HARD_LEVEL_TURNS=5     

# functions to check user's guess aginst the actual answer
def check_answer(guess,game_number,turns):
    ''' check whether user guess matches with the game number'''

    if guess>game_number:
        print("Too high")
        return turns - 1
    elif guess < game_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {game_number}")


# Make function to set difficulty
def set_difficulty():
    level=input("Chosse a difficulty.Type 'easy' or 'hard': ").lower()
    
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print(" Welcome to Number guessing game !")
    print(" I am thinking a number between 1 and 100")
    print("........")
    print(".....")
    print("...")
    game_number=random.randint(1,101)

    turns=set_difficulty()

    guess=0

    while guess !=game_number:
        print(f"you have {turns } attempt left to guess the number.")

        # let user guess a number
        guess=int(input("Make a guess : "))

        turns=check_answer(guess,game_number,turns)

        if turns==0:
            print("You have run out of guesses, you lose")
            print(game_number)
            return
        elif guess !=game_number:
            print("Guess again")

game()






# ______________________________________________________ALTERNATIVE METHOD_____________________________________________________________________________

# game_over=False


# def game_outcome():
#     user_guess=int(input("guess the number : "))
#     if game_number==user_guess:
#         print(f"You have made right guess. the answer is {game_number}")
#         return True
#     elif user_guess > game_number:
#         print("You have gone too high")
#     elif user_guess < game_number:
#         print("You have gone too low")
#     return False




# while not game_over:
    # if game_mode=='easy':
    #     print("you have got 10 chances")
    #     for _ in range(10):
    #         if game_outcome():
    #             game_over=True
    #             break
            
    #     if not game_over:
    #             print("You used all your guesses")
    #             game_over=True





    # elif game_mode=='difficult':
    #     print("you have got 5 chances")
    #     for _ in range(5):
    #         if game_outcome():
    #             game_over=True
    #             break
    #     if not game_over:
    #             print("You used all your guesses")
    #             game_over=True
    # else:
    #    print("select valid game mode")
    #    game_over=True
        


