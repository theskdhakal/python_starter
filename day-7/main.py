import random

word_list=["glass","table","wallpaper", "chicken"]

chosen_word=random.choice(word_list)

print(chosen_word)

letter_list=list(chosen_word)
array_length=len(letter_list)





guess_list=[]
for letter in letter_list:
    guess=input("enter a letter: ")
    print(guess)

    guess_list.append(guess)


    i=0
    while i < array_length:
        if guess in letter_list[i]:
            print("right")
            
        else:
            print("wrong")
        
        i +=1


guessed_word=''.join(guess_list)

print(guessed_word)
    


        
        

