import random
#### 04/28/2025 ####
#I am starting a new project called Jankenpo, which is a rock-paper-scissors game. This is from the Python Course I am taking. I hope to learn more about Python and Information Technology/Computer Science along the way. #


#libraries
#import random

##how to use a dictionary in Python
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.  
#dict = {'name': 'beau', 'color': choices}

##Lists
#food = ['pizza', 'sushi', 'tacos']
#dinner = random.choice(food)
def greeting():
    return"Hi! Welcome to Jankenpo or Rock, Paper, Scissors!"

def get_choices():

    print (greeting()) #call the greeting function

    player_choice =  input( "Enter a choice (rock, paper, scissors):")

    Options= ['rock',  'paper', 'scissors']#list of options for computer_choice to select from

    computer_choice = random.choice(Options)

    choices = { 'player': player_choice, 'computer': computer_choice }  #choices dictionary

    return choices

def check_win(player,computer):
   ## print("You chose " + player + ", computer chose: " + computer + '.')
   print(f"You chose:{player}, computer chose:{computer}.") 

   if player == computer:
      return "It's a tie!"
   elif player == 'rock' and computer == "scissors":
       print("Rock smashes scissors! You win!")
       return 
   elif player == 'rock' and computer == 'paper':
       print("Paper covers rock! You lose!")
       return 
   elif player == 'paper' and computer == 'rock':
       print("Paper covers rock! You win!")
       return 
   elif player == 'paper' and computer == 'scissors':
       print("Scissors cuts paper! You lose!")
       return 
   elif player == 'Scissors' and computer == 'rock':
        print("Rock smashes scissors! You lose!")
        return 
   elif player == 'Scissors' and computer == 'paper':
       print("Scissors cuts paper! You win!")
       return 
   else:
       return 'ERROR: Try again...'
   




#variables
response = greeting()
choices = get_choices()
result = check_win( choices['player'], choices['computer'])





