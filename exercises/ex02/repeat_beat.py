"""Repeating a beat in a loop."""

__author__ = "730321464"


beat = str(input("What beat do you want to repeat? "))
times_repeated = int(input("How many times do you want to repeat it? "))
x = int(times_repeated)
while times_repeated > 0:
    print((beat + " ") * times_repeated)
    times_repeated = times_repeated - times_repeated 
if x <= 0:
    print('No Beat...') 