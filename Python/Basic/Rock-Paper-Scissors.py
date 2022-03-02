import random

scoreUser = 0
scoreComputer = 0


def RockPaperScissors():
    global scoreComputer
    global scoreUser
    again = True
    while(again):
        userChoise = input(
            "What will u chose: \n Rock(r) \n Paper(p) \n Scissors(s) \n")
        computerChoise = random.choice(['r', 'p', 's'])

        if computerChoise == userChoise:
            scoreUser = scoreUser + 1
            scoreComputer = scoreComputer + 1
            print(
                f"It's a tie!!! You both chose {userChoise}. The score is:\n (User - Computer) \n {scoreUser} to {scoreComputer}")
        elif (computerChoise == 'r' and userChoise == 's') \
                or (computerChoise == 'p' and userChoise == 'r') \
                or (computerChoise == 's' and userChoise == 'p'):
            scoreComputer = scoreComputer + 1
            print(
                f"You lost!!! Computer chose {computerChoise}. The score is:\n (User - Computer) \n {scoreUser} to {scoreComputer}")
        else:
            scoreUser = scoreUser + 1
            print(
                f"You Won!!! Computer chose {computerChoise}. The score is:\n (User - Computer) \n {scoreUser} to {scoreComputer}")
        againAnswere = input("Do you want to play again? y/n: \n")
        if(againAnswere != 'y'):
            again = False


RockPaperScissors()
