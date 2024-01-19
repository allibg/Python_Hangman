import random
import time
from colorama import Fore

words_list = ['banana', 'cherry', 'orange', 'pear', 'pineapple', 'apple']


class Hangman:
    def __init__(self, name):
        self.selected_word = random.choice(words_list)
        self.guesses = ''
        self.failed = 0
        print(Fore.LIGHTYELLOW_EX + f'Hello {name} and welcome to my hangman')
        time.sleep(2)
        print(Fore.LIGHTYELLOW_EX + 'in this game, you must guess some letters to fine a word ... the word is from fruits')
        time.sleep(2)
        print(Fore.LIGHTYELLOW_EX + 'lets Dive in....')

    def guess(self, letter):
        self.guesses += letter
        self.failed = 0
        for letters in self.selected_word:
            if letters in self.guesses:
                print(Fore.RED + letters, end=' ')
            else:
                print(Fore.RED + '_', end=' ')
                self.failed += 1
