import random  # Better to use this or a random index from word bank list?
from hangmanwords import word_bank

""" 
Hangman Game Project for PP3
"""

def get_random_word(word_bank):
    """ 
    A function to get a random word from the word bank
    """
#     global random_word
    random_word = random.choice(word_bank).upper()
    # print('CAPITAL RANDOM WORD:', random_word)
    print(' ')
    return random_word


def dashes_for_words(word):
    """ 
    A function to print dashes for the number of letters 
    in the randomly chosen word
    """
    print('_ ' * len(word))
    for letter in random_word:
        if letter in letters_to_reveal:
            print(letter.upper() + ' ', end= ' ')

        else:
            print('_ ', end='')

def check_guess(word):
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

        break


    print('LIST of guessed letters:', guessed_letters)
    guessed_letter = guessed_letters[-1]
    print('guessed letter:', guessed_letter)

    if guessed_letter in current_word:
        print('You guessed a correct letter! Well done!')

        # Reveal the word, with dashes and correctly guessed letters
        print('')

        # Get the users input again 
    else:
        print('Keep Trying!')

        # Add the hangman drawing here
        print('Add the hangman drawing here')    

def main():
    """
    A function to run all game functions
    """

    # Welcome the user to Hangman

    user_name = input('To Begin please enter your name: \n').upper().strip()
    print(f"Welcome to Hangman {user_name}! \nHere is your first word:")

#     global guessed_letters
#     guessed_letters = []
    
#     global current_word
    current_word = get_random_word(word_bank)
    # print('CURRENT_WORD:', current_word)

#     letters_to_reveal = 'c,a,t'
    dashes_for_words(current_word)

    keep_playing = True
    while keep_playing:

        while True:
            """ User inputs their guess and this input is validated """

            user_guess = input('Type your guess here: \n').strip().upper()
            # print(user_guess)
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

        # guessed_letters.append(user_guess)
        return True
    
        guessed_letters.append(user_guess)

    guess_is_correct = check_guess(current_word) # Must use the letter and word now
#     # keep_playing = False
main()
