"""An exercise in remainders and boolean logic."""

__author__ = "730321464"


number: int = int(input('Pick a number: '))

if number % 2 == 0 and number % 7 == 0:
    print('TAR HEELS')
else:
     if number % 2 == 0:
         print('TAR')
     else:
        if number % 7 == 0:
            print('HEELS')
        else: 
            print("CAROLINA")


