"""An example of conditional (if-else) statements"""

SECRET : int = 3

print("im thinking of a number between 1-5, what is it? ")
guess : int = int(input("what is your guess? "))

if guess == SECRET:
    print('you guessed correctly!!!')
else: 
    print('Sorry, you guessed incorrectly :(')
    if guess > SECRET:
        print("You guessed to high!")
    else: 
        print('Your guessed too low!')

print('game over.') 
