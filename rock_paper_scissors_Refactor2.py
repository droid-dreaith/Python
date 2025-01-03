import random #why this is random?because it imports and generate random choices 

#DICTIONARY
#why this is emojis? because it is a dictionary that contains the emojis for rock, paper, and scissors
emojis = { 'r': 'rock', 'p': 'paper', 's': 'scissors' }
choices = ('r','p','s')


#FUNCTIONS
#why this is get_user_choice? because it is a function that gets the user's choice
def get_user_choice(): #why def ? to define the function
    while True: #why while True? because it is a loop that will keep asking the user for their choice until they enter a valid choice
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice. Please try again.')
            
def display_choices(user_choice, computer_choice): #this is a function that displays the user's and computer's choices
     print(f'You chose {emojis[user_choice]}')
     print(f'The computer chose {emojis[computer_choice]}')
     
def determine_winner(user_choice, computer_choice):#this is a function that determines the winner of the game
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win!')
    else:
        print('You lose!')

def play_game():#this is a function that starts the game
        
    while True:
        user_choice = get_user_choice()
            
        computer_choice = random.choice(choices)
            
        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice, computer_choice)
   
#start the game     
play_game() #why this is play_game()? which starts the game loop