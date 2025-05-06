import random
#### 04/28/2025 ####
#I am starting a new project called Jankenpo, which is a rock-paper-scissors game. This is from the Python Course I am taking. I hope to learn more about Python and Informationo Technology/Computer Science along the way. #


#libraries
#import random

##how to use a dictionary in Python
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.  
#dict = {'name': 'beau', 'color': choices}

##Lists
#food = ['pizza', 'sushi', 'tacos']
#dinner = random.choice(food)


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")

    Options= ['rock',  'paper', 'scissors']#list of options for computer_choice to select from

    computer_choice = random.choice(Options)

    choices = { 'player': player_choice, 'computer': computer_choice }  #choices dictionary

    return choices

def greeting():
    return"Hi! Welcome to Jankenpo or Rock, Paper, Scissors!"

def check_win(player,computer):
   ## print("You chose " + player + ", computer chose: " + computer + '.')
   print(f"You chose:{player}, computer chose:{computer}.") 
   if player == computer:
      print("It's a tie!")
      return "It's a tie!" 
   elif player == 'rock':
    if computer == "scissors":
         print("Rock smashes scissors! You win!")
         return "Rock smashes scissors! You win!"
   elif player == "paper":
    if computer == "rock":
         print("Paper covers rock! You win!")
         return "Paper covers rock! You win!"
   elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
        return "Scissors cuts paper! You win!"
    else:
       return "Rock smashes scissors! You lose!"
    


#variables
response = greeting()
choices = get_choices()
result = check_win( choices['player'], choices['computer'])







