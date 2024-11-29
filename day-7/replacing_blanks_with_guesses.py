import random

word_list=["glass","table","donkey","laptop"]

chosen_word=random.choice(word_list)
print(chosen_word)
print(chosen_word[2])


chosen_word_length=len(chosen_word)

display=[]

for number in range(chosen_word_length):
    display.append("_")

print(display)


i=0

while i<chosen_word_length:
    
    guess=input("guess a letter: ").lower()

    if guess not in chosen_word:
        print("you guessed wrong letter")
    else:
        for position in range(0,chosen_word_length):
            letter=chosen_word[position]
            if letter==guess:
                display[position]=letter
    
    print(display)
    i+=1

if "_" in display:
    print("You lost the game")
else:
    print("You won the game")



# for gap in display:
#     guess=input("Guess a letter: ").lower()
#     i=0
#     while i<chosen_word_length:
#         if chosen_word_letters[i]==guess:
#             display[i]=guess
#         i+=1
#     print(display) 
        
    
        
 




