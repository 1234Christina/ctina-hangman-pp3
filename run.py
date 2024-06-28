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

        guessed_letters.append(user_guess)

        if user_guess in guessed_letters:
            print('You have already guessed that letter, try again!')
            continue

        continue

    print('LIST of guessed letters:', guessed_letters)
    guessed_letter = guessed_letters[-1]
    print('guessed letter:', guessed_letter)

    if guessed_letter in current_word:
        print('You guessed a correct letter! Well done!')
    else:
        print('Keep Trying!')

def main():
    """
    Run all game functions
    """

    user_name = input('To Begin please enter your name: \n').upper().strip()
    print(f"Welcome to Hangman {user_name}! \nHere is your first word:")

    guessed_letters = []
    current_word = get_random_word(word_bank)
    dashes_for_words(current_word)

    keep_playing = True
    while keep_playing:

        while True:
            """ User inputs their guess and this input is validated """

            user_guess = input('Type your guess here: \n').strip().upper()
            print(f'You guessed {user_guess}')
            print('')
            print('Checking answer...')

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
        check_guess()

        guessed_letters.append(user_guess)

main()
