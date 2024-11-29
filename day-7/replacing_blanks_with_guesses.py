import random

word_list=["glass","table","donkey","laptop"]

chosen_word=random.choice(word_list)
print(chosen_word)
chosen_word_letters=list(chosen_word)

chosen_word_length=len(chosen_word)

display=[]

for number in range(chosen_word_length):
    display.append("_")

print(display)





for gap in display:
    guess=input("Guess a letter: ").lower()
    i=0
    while i<chosen_word_length:
        if chosen_word_letters[i]==guess:
            display[i]=guess
        i+=1
    print(display) 
        
    
        
 




