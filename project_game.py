# Game Stone Papper Scissor
import random

def game(computer,player1):
    if computer==1:
        comp = "S"
    elif computer==2:
        comp = "P"
    else:
        comp = "C"
    print("Computer : ",comp)
    if comp==player1:
        print("Game Tied!")
    elif comp=="S":
        if player1=="P":
            print("You Win!")
        else:
            print("You Lose!")
    elif comp=="P":
        if player1=="C":
            print("You Win!")
        else:
            print("You Lose!")
    elif comp=="C":
        if player1=="S":
            print("You Win!")
        else:
            print("You Lose!")
    
computer = random.randint(1,3)
player1 = input("Enter Stone(S) or Papper(P) or Scissor(C)")

print("Player :",player1)
game(computer,player1)