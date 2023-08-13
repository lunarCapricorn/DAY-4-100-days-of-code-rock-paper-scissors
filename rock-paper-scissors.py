import asciiArt
import os
import random
os.system('clear')
typeSpeed = .04

def compResult():
    result = random.randint(0, 2)
    return result

def choice():
    choices = input()
    choiceLower = choices.lower()
    switches = {
        'rock':0,
        'paper':1,
        'scissors':2,
    }
    for index, value in switches.items():
        if (choiceLower == index):
            return value
    asciiArt.typingEffect('Wrong input . . . Would you like to play again? ', typeSpeed, 0)
    replay(input())
            
def replay():
    playerInput = input()
    if (playerInput == 'n'):
        asciiArt.typingEffect('Have a nice day! :)', typeSpeed, 3)
        exit()
    elif (playerInput == 'y'):
        os.system('clear')
        asciiArt.typingEffect('Yayy! :)\n', typeSpeed, 3)
        main()
    asciiArt.typingEffect('Only y = yes; n = no', typeSpeed, 3)
    replay()

def main():
    asciiArt.typingEffect('Choose: \033[1;32mRock\033[0m, \033[1;34mPaper\033[0m, or \033[1;35mScissors\033[0m ', typeSpeed, 0)
    playerResult = choice()
    compChoice = compResult()
    print(playerResult)
    asciiArt.result(compChoice)

    if (playerResult == compChoice):
        asciiArt.typingEffect('Draw!\n', typeSpeed, 2)
    elif ((playerResult == 0 and compChoice == 2) or (playerResult == 2 and compChoice == 1) or (playerResult == 1 and compChoice == 0)):
        asciiArt.typingEffect('Player won!', typeSpeed, 1)
    elif ((compChoice == 0 and playerResult == 2) or (compChoice == 2 and playerResult == 1) or (compChoice == 1 and playerResult == 0)):
        asciiArt.typingEffect('Computer won!', typeSpeed, 1)

    asciiArt.typingEffect('Would you like to play again? ', typeSpeed, 0)
    replay()

asciiArt.typingEffect('\033[0mWelcome to \033[1;32mRock\033[0m, \033[1;34mPaper\033[0m, \033[1;35mScissors\033[0m!\n', typeSpeed, 1)
asciiArt.typingEffect('Would you like to play? [y/n] ', typeSpeed, .5)
replay()