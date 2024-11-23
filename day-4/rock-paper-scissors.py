import random


rock = '''
       ,--.--._
------" _, \\___)
        / _/____)
        \\//(____)
------\\     (__)
       `-----"
      '''

paper = '''
              / \\ | | /\\
               \\ \\| |/ /
                \\ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |
    '''

scissor = '''
                .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \\  `(.-')
   > ._>-'
  / \\/
          '''




choices=[rock,paper,scissor]

userInput=int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))
print(userInput)

if userInput==0:
    print(f"You chose: \n {rock}")
elif userInput==1:
    print(f"You chose: \n {paper}")
elif userInput==2:
    print(f"You chose: \n {scissor}")
else:
    print("You chose invalid number")

computer_choice=random.choice(choices)

if userInput not in[0,1,2]:
    print()
else:
     print(f"Computer chose: \n {computer_choice}")


if userInput==0 and computer_choice==rock:
    print("Game is draw")
elif userInput==1 and computer_choice==rock:
    print("you won")
elif userInput==2 and computer_choice==rock:
    print("You lost")
elif userInput==0 and computer_choice==paper:
    print("You lost")
elif userInput==1 and computer_choice==paper:
    print("Game is draw")
elif userInput==2 and computer_choice==paper:
    print("You win")
elif userInput==0 and computer_choice==scissor:
    print("you won")
elif userInput==1 and computer_choice==scissor:
    print("you lost")
elif userInput==2 and computer_choice==scissor:
    print("game is draw")
else:
    print("Please try again")