import random 
from hangmanwords import word_bank
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" 
Hangman Game Project for PP3
"""

# # A word bank from which the words will be chosen randomly
# # for the user to guess
# word_bank = ['apple', 'ball', 'cat', 'duck', 'eggshell', 'football', 'garden',
# 'harp', 'icecream', 'jam', 'king', 'library', 'museum', 'nutella', 'ocean',
# 'playground', 'queen', 'race', 'snake', 'tea', 'under', 'vulture',
# 'waterfall', 'xylophone', 'yoyo', 'zoologist', 'always', 'before', 'chapel',
# 'dragon', 'electricity', 'fudge', 'game', 'heart', 'ice', 'jersey', 'kitten',
# 'lightbulb', 'monsoon', 'nut', 'octagon', 'pretend', 'quick', 'ready',
# 'smooth', 'train', 'unbelievable', 'van', 'wheel', 'xray', 'yard', 'zip',
# 'abacus', 'blackboard', 'chalk', 'dusty', 'emoji', 'flamingo', 'goblin',
# 'halloween', 'island', 'joker', 'ketchup', 'lookalike', 'magic', 'newspaper',
# 'office', 'priest', 'qualify', 'rabbit', 'shop', 'turtle', 'uncle', 'video',
# 'wagon', 'xbox', 'yoghurt', 'zero']


def get_random_word(word_bank):
    """ 
    A function to get a random word from the word bank
    """
    random_word = random.choice(word_bank)
    # print(random_word)
    return random_word

def dashes_for_words(random_word):
    """ 
    A function to print dashes for the number of letters 
    in the randomly chosen word
    """
    
    print('_' * len(random_word))

# A function to allow a user to guess a letter
# def get_user_guess():
#     """
#     A function to ask user to guess a letter
#     """
#     return user_guess


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
        print('You guessed a correct letter!')
    else:
        print('Try again')
    


""" 
Welcome the user to Hangman
"""
user_name = input('To Begin please enter your name: \n')
print(f"Welcome to Hangman {user_name}! \nHere is your first word:")


# print(word_bank[2])
# print(word_bank[-34])
# print(word_bank[-32])
# print(word_bank[42])
# print(word_bank[12])

# dashes_for_words()
# get_random_word(word_bank)
# get_user_guess()
# check_guess()

def main():
    """
    A function to run all game functions
    """
    global guessed_letters
    guessed_letters = []
    
    global current_word
    current_word = get_random_word(word_bank)
    # print(current_word)
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


    # global guessed_letters
    # guessed_letters = []
    guessed_letters.append(user_guess)
    # print('LINE 119', guessed_letters)


    # guessed_letter = guessed_letters.pop()
    # print(guessed_letter)
    check_guess()

main()
