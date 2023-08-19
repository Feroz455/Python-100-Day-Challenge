import os
import random


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


Hangman = '''

 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
                                                                                
    
'''

print(Hangman)

hangman_stages = [

    '''
    +---+
        |
        |
        |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
        |
        |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
    |   |
        |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
   /|   |
        |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
   /|\  |
        |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
   /|\  |
   /    |
        |
        |
    ===========
    ''',
    '''
    +---+
    O   |
   /|\  |
   / \  |
        |
        |
    ===========
    '''
]


words = ["Bangladesh", "Nepal", "India"]
# Convert the chosen word to lowercase
chosen_word = random.choice(words).lower()
display = list(chosen_word)
choise = ["_"] * len(display)
tryArt = 0
attempts = len(hangman_stages)  # Number of attempts
correct_guesses = 0

# Loop for handling guesses
while attempts > 0 and correct_guesses < len(display):
    clear_screen()

    print(Hangman)
    print(hangman_stages[tryArt])
    print(" ".join(choise))

    letter = input("Enter a letter: ").lower()  # Convert input to lowercase
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabetical letter.")
        continue

    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter and choise[i] == "_":
                choise[i] = letter
                correct_guesses += 1
    else:
        attempts -= 1
        tryArt += 1

if correct_guesses == len(display):
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Sorry, you couldn't guess the word. The word was:", chosen_word)
