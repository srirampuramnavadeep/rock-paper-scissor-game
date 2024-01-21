import random
rock = "ROCK"
paper = "PAPER"
scissor = "SCISSOR"
game_image = [rock,paper,scissor]
user_choice=int(input("What do you choose? Type 0 for rock ,1 for paper or 2 for scissors.\n"))
print(game_image[user_choice])
computer_choice=random.randint(0, 2)
print("Computer chose",computer_choice)
print(game_image[computer_choice])
if user_choice ==0 and computer_choice ==0:
    print("TIE GAME")
elif user_choice == 0 and computer_choice==1:
    print("YOU LOSS")
elif user_choice ==0 and computer_choice==2:
    print("YOU WON")
elif user_choice == 1 and computer_choice==0:
    print("YOU WIN")
elif user_choice == 1 and computer_choice==1:
    print("TIE GAME")
elif user_choice == 1 and computer_choice==2:
    print("YOU LOSS")
elif user_choice == 2 and computer_choice==0:
    print("YOU LOSS")
elif user_choice == 2 and computer_choice==1:
    print("YOU WON")
elif user_choice==2 and computer_choice==2:
    print("TIE GAME")
   
else:
    print("You typed an invalid number, you lose!")
