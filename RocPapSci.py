# This program lets a user play Rock, Paper, Scissors against the computer.
import random

def main():
    # Generate a random number.
    keep_going = 'y'

    print()
    while keep_going == 'y':
        choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        num = user_input()
        print()
        print('You picked:', choice[num])

        # Get a random number and compare it to the number entered.
        comp = random.randint(1, 3)

        print('The computer picked:', choice[comp])

        decider(num, comp)

        keep_going = (input("Do you want to play again?: Enter, 'y', for " + \
        "yes, anything else for no: "))

def decider (num, comp):
    if num == comp:
        print("It's a draw! ")

    # If the two numbers are different, then figure out who wins.
    elif num == 1 and comp == 2:
        print('The computer wins. Rock loses to paper.\n')
    elif num == 1 and comp == 3:
         print('You win! Scissors loses to rock.\n')
    elif num == 2 and comp == 3:
         print('The computer wins. Paper loses to scissors.\n')
    elif num == 2 and comp ==1:
        print('You win! Rock loses to paper.\n')
    elif num == 3 and comp ==1:
        print('The computer wins. Scissors loses to rock.\n')
    elif num == 3 and comp == 2:
        print('You win! Paper loses to scissors.\n')

    else:
        print('Good game!!')

# Get player's input.
def user_input():
    # Enter a number.
    number = int(input('Make a selection: 1 = Rock, 2 = Paper and 3 = Scissors: '))
    while number < 1 or number > 3:
        print('*** ValueError ***')
        print('Please enter a valid number')
        number = int(input('Make a selection: 1 = Rock, 2 = Paper and 3 = Scissors: '))
    print()
    return number

# Call the main function.
main()
