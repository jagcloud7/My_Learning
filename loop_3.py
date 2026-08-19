# Number guessing program - Number hard coded

import random
guess_the_number = 7

for guesses_taken in range(1,7):
    print('take a guess from 0 - 7.')
    guess_the_number = int(input('>'))
    
    if guess_the_number < 5:
        print('Your guess is too low')
    elif guess_the_number < 7:
        print('Not yet!!! You are almost there, Try again')
    else:
        break
    
if guess_the_number == 7:
    print("correct! you got it!!!")
    