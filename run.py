import random 
from hangmanwords import word_bank

""" 
Hangman Game Project for PP3
"""

def get_random_word(word_bank):
    """ 
    A function to get a random word from the word bank
    """
    global random_word
    random_word = random.choice(word_bank).upper()
    print('CAPITAL RANDOM WORD:', random_word)
    return random_word

def dashes_for_words(random_word):
    """ 
    A function to print dashes for the number of letters 
    in the randomly chosen word
    """
    
    print('_' * len(random_word))

def check_guess():
    """
    Find out if users guessed letter is in the word and give feedback
    """
    # current_word = get_random_word(word_bank)
    # guessed_letter = get_user_guess()

    print('LIST of guessed letters:', guessed_letters)
    guessed_letter = guessed_letters.pop()
    print('guessed letter:', guessed_letter)

    if guessed_letter in current_word:
        print('You guessed a correct letter! Keep going!')

    if guessed_letter not in current_word:
        print('incorrect letter...')
        print('hangman drawing here')       

def main():
    """
    A function to run all game functions
    """

    # Welcome the user to Hangman

    user_name = input('To Begin please enter your name: \n').upper()
    print(f"Welcome to Hangman {user_name}! \nHere is your first word:")

    global guessed_letters
    guessed_letters = []
    
    global current_word
    current_word = get_random_word(word_bank)
    print('CURRENT_WORD:', current_word)
    dashes_for_words(current_word)

    while True:

        user_guess = input('Type your guess here: \n').strip().upper()
        # print(user_guess)
        print(f'You guessed {user_guess}')
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

    guessed_letters.append(user_guess)

    check_guess()

main()
