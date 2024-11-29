import random

word_list= [
    "compass",
    "fortune",
    "journey",
    "lantern",
    "mystery",
    "thunder",
    "whistle",
    "courage",
    "harvest",
    "mirror"
]

hints = [
    "A tool used to find directions.",
    "Luck, often related to wealth or success.",
    "An act of traveling from one place to another.",
    "A portable light source often used outdoors.",
    "Something that is difficult to explain or understand.",
    "The loud sound during a storm.",
    "A sound made by forcing air through lips or a device.",
    "The ability to face danger without fear.",
    "The act of gathering crops.",
    "A reflective surface you look into."
]


stages = [
    '''
        ____________________                     
       |                    |
       O                    |
                            |
                            |
                            |
                            |
                            |
  =============================
    ''',
    '''
       _____________________                     
       |                    |
       O                    |
      /                     |
                            |
                            |
                            |
                            |
  =============================
    ''',
    '''
       _____________________                     
       |                    |
       O                    |
      / \\                  |
                            |
                            |
                            |
                            |
  =============================
    ''',
    '''
       _____________________                     
       |                    |
       O                    |
      /|\\                  |
       |                    |
                            |
                            |
                            |
  =============================
    ''',
    '''
       _____________________                     
       |                    |
       O                    |
      /|\\                  |
       |                    |
      /                     |
                            |
                            |
  =============================
    ''',
    '''
       _____________________                     
       |                    |
       O                    |
      /|\\                   |
       |                    |
      / \\                   |
                            |
                            |
  =============================
    '''
]
   
  

stages.reverse()

index=random.randint(0,len(word_list)-1)
chosen_word=word_list[index]
hint=hints[index]

print("________________________________WELCOME TO HANGMAN GAME______________________________________")


print(f"Your hint is : {hint}")

chosen_word_length=len(chosen_word)

display=[]

for number in range(chosen_word_length):
    display.append("_")

print(display)



life=len(stages)-1


game_over=False

while game_over is False:
    guess=input("guess a letter: ").lower()

    if guess in display:
        print("You have already guessed this letter")
     

    elif guess in chosen_word:
         for position in range(0,chosen_word_length):
            letter=chosen_word[position]
            if letter==guess:
                display[position]=letter
        
         print(display)
         
         if "_" not in display:
                  game_over=True
                  print("****** You won the game *********")

  
       
    else:
        if life > 0:
            print(stages[life])
            life -=1
        else:
            print(stages[life])
            print("You ran out of life. You lost the game")
            game_over=True
    
   
   





# for gap in display:
#     guess=input("Guess a letter: ").lower()
#     i=0
#     while i<chosen_word_length:
#         if chosen_word_letters[i]==guess:
#             display[i]=guess
#         i+=1
#     print(display) 
        
    
        
 




