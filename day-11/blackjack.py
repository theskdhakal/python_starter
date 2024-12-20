from art import logo
import random
import os

print(logo)




print("WELCOME TO BLACKJACK")
 





def deal_card():
     """ Returns a random card from deck"""
     cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

     card=random.choice(cards)
     return card



def calculate_score(cards):
     """ Take a list of card and return the sum of the card"""
     
     # sum use take a iterable list as argument and perform additon from left to right

     if sum(cards)==21 and len(cards) ==2:
          return 0


     if 11 in cards and sum(cards) >21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)  


def compare_score(user_score, computer_score) :
     if user_score == computer_score:
          return "Draw "
     elif computer_score == 0:
          return "Lose, opponent has Blackjack"
     elif user_score ==0:
          return "Win with a blackjack"
     elif user_score >21:
          return "You went over.you lose"
     elif computer_score >21:
          return "Opponent went over. You win"
     elif user_score > computer_score:
          return "You win"
     else:
          return "You lose"


def play_game():
     user_cards=[]
     computer_cards=[]
     is_game_over=False

     for _ in range(2):
          user_cards.append(deal_card())
          computer_cards.append(deal_card())





     while not is_game_over:
          user_score=calculate_score(user_cards)
          computer_score=calculate_score(computer_cards)

          print(f"Your cards: {user_cards}, current score:{user_score}")
          print(f"computer's first card: {computer_cards[0]}")


          if user_score==0 or computer_score==0 or user_score > 21:
               is_game_over=True
          else:
               ask_user=input("Do you want to draw another card ? Y or N : ").lower()

               if ask_user == "y":
                    user_cards.append(deal_card())
               else:
                    is_game_over=True

     while computer_score !=0 and computer_score <17:
          computer_cards.append(deal_card())
          computer_score=calculate_score(computer_cards)


     print(f"Your cards: {user_cards}, current score:{user_score}")
     print(f"computer's cards: {computer_cards}, computer score:{computer_score}")

     print(compare_score(user_score,computer_score))



while input("Do you want to play the game ? Y or N: ").lower() == "y":
     os.system('cls')
     play_game()
