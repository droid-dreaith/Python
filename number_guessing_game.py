#generate a random number
#ask the user to make a guess
#if not a valid number
    #print an error message
#if number < guess
        #print too low
#if number > guess
        #print too high
#else
    #print you guessed it
    
#--------will use a while loop to keep the game running----------------

import random


numnber_to_guess = random.randint(1, 100)

while True: #this is a infinite loop / when using while

    #loop
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        
        if guess < numnber_to_guess:
            print('Too low!')
        elif guess > numnber_to_guess:
            print('Too high!')
        else:
            print('You guessed it!')
            
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        

        


