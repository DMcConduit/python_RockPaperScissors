import random

#use while loop to keep repeating game
while True:
  
  print("Welcome to Rock, Paper, Scissors. Let's play!")
  
  #player input
  player_choice = input("Player, choose one: rock, paper, or scissors?  ")
  
  #computer input
  choices = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(choices)

  #validate player input
  if player_choice not in (choices):
    print("Your choice was invalid. Please try again.")
    player_choice = input("Player, choose one: rock, paper, or scissors?  ")
        
  print(f"You chose {player_choice}. Computer chose {computer_choice}.")
  
  #check winner
  if player_choice == computer_choice:
    print("It's a tie!")
  
  elif player_choice == "rock":
    if computer_choice == "scissors":
      print("Rock smashes scissors. You win.")
    else:
      print("Paper covers rock. You lose.")
  
  elif player_choice == "paper":
    if computer_choice == "rock":
      print("Paper covers rock. You win!")
    else:
      print("Scissors cut paper. You lose.")
  
  elif player_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors cut paper. You win!")
    else:
      print("Rock smashes scissors. You lose.")
  
  play_again = input("Would you like to play again? Enter y or n.  ")
  if play_again != 'y':
    break
    #use break to the break the loop and end the game

