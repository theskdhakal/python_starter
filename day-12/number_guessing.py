import random

print(" Welcome to Number guessing game !")
print(" I am thinking a number between 1 and 100")
print("........")
print(".....")
print("...")
game_mode=input(" Choose a difficulty . Type 'easy' or 'difficult' : ").lower()

game_number=random.randint(1,101)

print(game_number)
game_over=False


def game_outcome():
    user_guess=int(input("guess the number : "))
    if game_number==user_guess:
        print("You have made right guess")
        return True
    elif user_guess > game_number:
        print("You have gone too high")
    elif user_guess < game_number:
        print("You have gone too low")





while not game_over:
    if game_mode=='easy':
        print("you have got 10 chances")
        for _ in range(10):
            game_outcome()
        game_over=True
        print("You used all your guesses")
    elif game_mode=='difficult':
        print("you have got 5 chances")
        for _ in range(5):
            game_outcome()
        game_over=True
        print("You used all your guesses")
    else:
       print("select valid game mode")
       game_over=True
        


            


