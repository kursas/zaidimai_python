#Hint: Take the user choice and then compare it with the computer choice
# which is taken using the random module from a list of choices, 
# and if the user wins then increase the score by 1.
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='E':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    computer = random.choice(choices)
    
    #output
    Rock, Paper or  Scissors?Rock
You win! Rock smashes Scissors
Rock, Paper or  Scissors?Paper
Tie!
Rock, Paper or  Scissors?Scissors
You win! Scissors cut Paper
Rock, Paper or  Scissors?
