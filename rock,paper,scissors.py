import os
import random
import time

#Declare variables
user_wins = 0
computer_wins= 0

while True:
    os.system("clear")

    #Show the instructions
    print("""************************************************************
    Welcome to Rock Paper Scissors...
    The rules are simple:
    The computer and user choose from Rock, Paper, or Scissors.
    Rock crushes scissors.
    Paper covers rock.
    and
    Scissors cut paper.
    You will play the computer...the first to reach 3 wins wins the match.
    Good luck!
    ************************************************************
    """)
    print("""
Wins: {}
Computer Wins: {}""".format(user_wins, computer_wins))

    user_choice = input("Please choose (R) Rock, (P) Paper, or (S) Scissors: ").upper()

    #Let the computer make a choice
    #1 = rock
    #2 = paper
    #3 = scissors
    random_number = random.randint(1,3)

    #Convert random number to R, P, or S for Rock, Paper, Scissors
    if random_number == 1:
        computer_choice = "R"

    elif random_number == 2:
        computer_choice = "P"

    elif random_number == 3:
        computer_choice = "S"

    #Print ASCII Art for the computer's choice
    if computer_choice == "R":
        print("""
    _______
---'   ____)
     (_____)
     (_____)
      (____)
---.__(___)
    The CPU chose rock.""")

    elif computer_choice == "P":
        print("""
    _______
---'   ____)____
          ______)
         _______)
         _______)
---.__________)
    The CPU chose paper.""")

    elif computer_choice == "S":
        print("""
   _______
---'  ____)____
         ______)
     __________)
        (____)
---.__(___)
    The CPU chose scissors.""")

    print("")

    #User wins
    #Computer: R    User: P
    #Computer: P    User: S
    #Computer: S    User: R

    if (computer_choice == "R" and user_choice == "P") or \
        (computer_choice == "P" and user_choice == "S") or \
        computer_choice == "S" and user_choice == "R":
        print("Player wins!")
        user_wins += 1

    #Computer wins
    #Computer: R    User: S
    #Computer: P    User: R
    #Computer: S    User: P

    elif (computer_choice == "R" and user_choice == "S") or \
        (computer_choice == "P" and user_choice == "R") or \
        (computer_choice == "S" and user_choice == "P"):
        print("Player loses!")
        computer_wins += 1

    #Tie
    #Computer: R    User: R
    #Computer: P    User: P
    #Computer: S    User: S

    elif computer_choice == user_choice:
        print("Tie!")

    elif   input != user_choice:
        print("INPUT NOT AMONG THE OPTION. TYPE CORRECT INPUT!!!")

    if user_wins == 3:
        print("PLAYER WINS!!!!")
        Play_again = input("Would you like to play again? (y/n) > ")
        if Play_again == "Y":
            user_wins = 0
            computer_wins= 0
            continue
        else:
            exit()
    

    if computer_wins == 3:
        print("CPU WINS!!!")
        Play_again = input("Would you like to play again? (y/n) > ")
        if Play_again == "Y":
            user_wins = 0
            computer_wins= 0
            continue
        else:
            exit()
    


    time.sleep(1.5)
    