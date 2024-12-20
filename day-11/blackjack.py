from art import logo
import random

print(logo)




print("WELCOME TO BLACKJACK")
 





def deal_card():
     """ Returns a random card from deck"""
     cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

     card=random.choice(cards)
     return card


user_cards=[]
computer_cards=[]

for _ in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())

# computer_card=random.sample(cards,2)
# print(computer_card)


# human_card=random.sample(cards,2)
# print(human_card)


# def add_score():
#     human_score=sum(human_card)
#     computer_score=sum(computer_card)

   
    
#     if (human_score==21):
#          print("Blackjack:You won the game")
#          return 0
#     elif (computer_score==21):
#          print("Blackjack:Computer won the game")
#          return 0
#     elif human_score >21:
#          if 11 in human_card:
#               human_card.remove(11)
#               human_card.append(1)

#               if human_score >21:
#                    print("You lose")
              
#          else:
#               print("You lose")
     

# def calculate_score():

#          add_score()

#          another=input("Do you want to draw another card ? Y or N : ").lower()
#          print(another)

#          if another == "y":
#                human_another=random.choice(cards)
#                human_card.append(human_another)

#                add_score()
#          else:
#                if computer_score < 17:
#                      computer_another=random.choice(cards)

#                      computer_card.append(computer_another)
#                      add_score()

#                      if computer_score == 21 or computer_score > human_score:
#                            print("computer won")
#                      else:
#                            print("You won")
               
# calculate_score()



def calculate_score(cards):
     cards=[1,5,3,4]
     # sum use take a iterable list as argument and perform additon from left to right

     if sum(cards)==21 and len(cards) ==2:
          return 0


     if 11 in cards and sum(cards) >21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)  

