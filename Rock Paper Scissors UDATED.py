# code for ROCK, PAPER, SCISSORS Game

import random

print("You are playing___ ROCK(👊), PAPER(🤚) AND SCISSORS(✌️)___🌺.")
print()
print("The rules of this game are:")
print("A . Rock beats scissors.")
print("B . Scissors beats paper.")
print("C . Paper beats rock.")
print()
print("Let's Start The Game")
print("😃😎😁")
print("")


def game():
    '''
    Objective:To write a program to display
    the game:Stone Paper Scissors.
    Input parameters: user choice and computer choice - numeric value
    Output value:
    '''
    Score1 = 0  # Player's score
    Score2 = 0  # Computer's score
    move = ["Rock⛰️", "Paper📃", "Scissors✂️"]

    # keep playing until user wants to exit.

    while True:
        print("Enter 1 for Rock⛰️.")
        print("Enter 2 for Paper📃.")
        print("Enter 3 for Scissors ✂️.")
        print("Enter 0 to exit.")
        user = eval(input("Enter your choice:"))

        # user choice
        if user == 0:
            print("You Exit")
            break

        # validation of user choice
        if user < 0 or user > 3:
            print("Enter a valid choice")
            print()
            continue

        # computer chooses random move
        computer = random.randint(1, 3)

        # initial Score

        # display the move of each player
        print("You chose : ", (user))
        print("Computer played: ", (computer))

        # condition to win
        # rock vs paper => paper wins
        # rock vs scissor => rock wins
        # paper vs scissor => scissor wins

        # playing - computer vs user
        if computer == user:
            Score1 += 1  # user's score
            Score2 += 1  # computer's score
            print("[It is a tie!]")
            print("*You Scored:", (Score1))
            print("*Computer Scored:", (Score2))
            print()

        elif computer == 1 and user == 3:
            Score2 += 1
            Score1 += 0
            print("[Computer wins!]")
            print('*Computer Scored:', (Score2))
            print('*You Scored:', (Score1))

        elif computer == 2 and user == 1:
            Score2 += 1
            Score1 += 0
            print("[Computer wins!]")
            print('*Computer Scored:', (Score2))
            print('*You Scored:', (Score1))
            print()

        elif computer == 3 and user == 2:
            Score2 += 1
            Score1 += 0
            print("[Computer wins!]")
            print('*Computer Scored:', (Score2))
            print('*You Scored:', (Score1))
            print()
        else:
            Score1 += 1
            Score2 += 0
            print("[You win!]")
            print('*You scored:', (Score1))
            print('*Computer Scored:', (Score2))
            print()

        if Score1 == 5 or Score2 == 5:
            return Score1, Score2


def main():
    Score1 = 0
    Score2 = 0
    game()
    if Score1 == 5 and Score2 != 5:
        print("U WoN 🎉🥳")
    else:
        print("U lost😔.Better luck next time!!")


if __name__ == '__main__':
    main()
