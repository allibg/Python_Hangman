from HangMan import Hangman
from colorama import Fore

hangman = Hangman(input('please enter your name: '))
while True:
    hangman.guess(input(Fore.BLUE+'\nplease enter your guess: '))
    if hangman.failed == 0:
        print(Fore.GREEN+'\nyou won')
        break
