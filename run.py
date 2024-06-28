import random 
from hangmanwords import word_bank

""" 
Hangman Game Project for PP3
"""

def get_random_word(word_bank):
    """ 
    A function to get a random word from the word bank
    """
    random_word = random.choice(word_bank).upper()
    print(' ')
    return random_word


def dashes_for_words(word):
    """ 
    A function to print dashes for the number of letters 
    in the randomly chosen word
    """
    print('_ ' * len(word))

def check_guess():
    """
    User inputs their guess and this input is validated
    Check if users guessed letter is in the word and give feedback 
    """
    guessed_letters = []
    user_guess = input('Type your guess here: \n').strip().upper()

    print(f'You guessed {user_guess}')
    print('')
    print('Checking answer...')
    
    while True:
        
        if not user_guess.isalpha():
            print('Please enter a letter')
            continue

        if len(user_guess) > 1:
            print('Please enter just one letter')
            continue

        if user_guess in guessed_letters:
            print('You have already guessed that letter, try again!')
            continue

        break

    guessed_letters.append(user_guess)
    guessed_letter = guessed_letters[-1]

    return guessed_letter

def show_letters(guess, word):
    #Use the returned guessed letter to start displaying right letters in the word
    if guess in word:
            print('You guessed a correct letter! Well done!')
    else:
            print('Keep Trying!')

def main():
    """
    Run all game functions
    """

    user_name = input('To Begin please enter your name: \n').upper().strip()
    print(f"Welcome to Hangman {user_name}! \nHere is your first word:")

    current_word = get_random_word(word_bank)
    dashes_for_words(current_word)
    guessed_letter = check_guess()
    show_letters(guessed_letter, current_word)

main()
