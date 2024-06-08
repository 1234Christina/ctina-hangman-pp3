import random 
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

""" 
Hangman Game Project for PP3
"""

# A word bank from which the words will be chosen randomly
# for the user to guess
word_bank = ['apple', 'ball', 'cat', 'duck', 'eggshell', 'football', 'garden',
'harp', 'icecream', 'jam', 'king', 'library', 'museum', 'nutella', 'ocean',
'playground', 'queen', 'race', 'snake', 'tea', 'under', 'vulture',
'waterfall', 'xylophone', 'yoyo', 'zoologist', 'always', 'before', 'chapel',
'dragon', 'electricity', 'fudge', 'game', 'heart', 'ice', 'jersey', 'kitten',
'lightbulb', 'monsoon', 'nut', 'octagon', 'pretend', 'quick', 'ready',
'smooth', 'train', 'unbelievable', 'van', 'wheel', 'xray', 'yard', 'zip',
'abacus', 'blackboard', 'chalk', 'dusty', 'emoji', 'flamingo', 'goblin',
'halloween', 'island', 'joker', 'ketchup', 'lookalike', 'magic', 'newspaper',
'office', 'priest', 'qualify', 'rabbit', 'shop', 'turtle', 'uncle', 'video',
'wagon', 'xbox', 'yoghurt', 'zero']


def get_random_word(word_bank):
    """ 
    A function to get a random word from the word bank
    """
    random_word = random.choice(word_bank)
    #print(random_word)
    return random_word

# def dashes_for_words():
""" 
A function to print dashes for the number of letters 
in the randomly chosen word
"""

# A function to allow a user to guess a letter


""" 
Welcome the user to Hangman
"""
print("Welcome to Hangman")

# print(word_bank[2])
# print(word_bank[-34])

get_random_word(word_bank)