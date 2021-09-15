"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730321464"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print('Your fortune cookie says...')

fortune: int = randint(1, 4)

if fortune == 1:
    print('Now is the time to try something new.')
if fortune == 2: 
    print('A new voyage will fill your life with untold memories.')
if fortune == 3: 
    print('Fortune favors the brave.')
if fortune == 4:
    print('You will conquer obstacles to achieve success.')

print('Now, go spread positive vibes!')