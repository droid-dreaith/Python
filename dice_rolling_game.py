
#roll a dice?
#if the user enters y
# generate a random number two numbers
#print them
# if users enters n 
# print thank you message 
# terminate 
    # else 
    # print invalid choice  
import random

while True:
    print('=========== Welcome to the Dice Rolling Game! ===========')
    print('==========================================================')
    choice = input('========= Shall We Begin? ======== (y/n): ').strip().lower()
    print(f'You entered: {choice}')
    
    if choice == 'y':
        print('Loading...')
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled: ({die1}, {die2})')
        print('Thank you for playing!')
        
    elif choice == 'n':
        print('Exiting........')
        print('Goodbye!')
        break
        
    else:
        print('Invalid choice! Please enter "y" or "n".')
       
   