import random

print("Welcome to Rock, Paper, Scissors Game!")

def get_choices(): 
       
        player_choice = str(input("Enter a choice (rock, paper, scissors): "))
        options = ["rock","paper","scissors"]
        computer_choice = random.choice(options) 

        choices = {"player": player_choice , "computer": computer_choice}
        return choices  
        

def check_win(player, computer): 
    print(f"You choose {player} and computer choose {computer}")
    if player == computer: 
        return "It's a tie."
    elif player == "rock": 
        if computer == "scissors": 
            return "Rock smashes scissors. You win!"
        else: 
            return "Paper covers rock. You lose."
    elif player == "scissors": 
        if computer == "paper": 
            return "Scissors cuts paper. You win!"
        else: 
            return "Rock smashes scissors. You lose."
    elif player == "paper": 
        if computer == "rock": 
            return "Paper covers rock. You win!"
        else: 
            return "Scissors cuts paper. You lose."
    else: 
        return "Write your choice as mentioned!"


while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)