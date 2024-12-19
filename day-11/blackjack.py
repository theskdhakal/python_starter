from art import logo
import random

print(logo)




print("WELCOME TO BLACKJACK")
 

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_card=random.sample(cards,2)
computer_score=computer_card[0] + computer_card[1]
print(computer_card)


human_card=random.sample(cards,2)
human_score=human_card[0] + human_card[1]
print(human_card)


def add_score():
    human_score=0
    computer_score=0

    for n in human_card:
          human_score += n
     
    for card in computer_card:
          computer_score += card
    
    if (human_score==21):
         print("Blackjack:You won the game")
         return 0
    elif (computer_score==21):
         print("Blackjack:Computer won the game")
         
         return 0
    elif human_score >21:
         if 11 in human_card:
              human_card.remove(11)
              human_card.append(1)

              if human_score >21:
                   print("You lose")
              
         else:
              print("You lose")
     






def calculate_score():

         add_score()

         another=input("Do you want to draw another card ? Y or N : ").lower()
         print(another)

         if another == "y":
               human_another=random.choice(cards)
               human_card.append(human_another)

               add_score()
         else:
               if computer_score < 17:
                     computer_another=random.choice(cards)

                     computer_card.append(computer_another)
                     add_score()

                     if computer_score == 21 or computer_score > human_score:
                           print("computer won")
                     else:
                           print("You won")
               



calculate_score()






