import random

#ask the user to make a choice
#if chocie is not valid
  #print "Invalid choice"
#let the computer make a choice
 #print the computer's choice
#determine the winner
  #if user choice is rock
    #if computer choice is rock
      #print "It's a tie"
    #if computer choice is paper
      #print "Computer wins"
    #if computer choice is scissor
      #print "User wins"
  #if user choice is paper
    #if computer choice is rock
      #print "User wins"
    #if computer choice is paper
      #print "It's a tie"
    #if computer choice is scissor
      #print "Computer wins"
  #if user choice is scissor
    #if computer choice is rock
      #print "Computer wins"
    #if computer choice is paper
      #print "User wins"
    #if computer choice is scissor
      #print "It's a tie"
import random

print('========Welcome to Rock, Paper, Scissors Game========')
print('Instructions:')
print('Enter "r" for Rock')
print('Enter "p" for Paper')
print('Enter "s" for Scissors')
print('Let\'s start the game!')

emojis = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}
choices = ['r', 'p', 's']

while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice not in ['r', 'p', 's']:
                print('Invalid choice!')
                continue
        computer_choice = random.choice(choices)

        print(f'You chose {emojis[user_choice]}')
        print(f'The computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
                print("It's a tie!")
        elif (
                (user_choice == 'r' and computer_choice == 's') or
                (user_choice == 's' and computer_choice == 'p') or
                (user_choice == 'p' and computer_choice == 'r')
        ):
                print("You win!")
        else:
                print('You Lose!')

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
                break