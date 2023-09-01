# Importing random library
import random

# def = defines our function 'roll'
def roll():
  # Minimum and Maximum numbers sets the perimeter
  min_value = 1
  max_value  = 6
  # Generates a random integer 'roll', using the min and max value
  roll  = random.randint(min_value, max_value)

  return roll

while True:
# Allows the player to input ammount of addition players 
  players = input("Enter the number of players (2 - 4): \n")
  # forces player to enter an integer, if statement and else statements forces set interaction
  if players.isdigit():
      players = int(players)
      # 2 must be greater than or equal to, players, and less than or equal to 4
      if 2 <= players <= 4:
         break
      else:
          print("Must be between 2 - 4 players.")
      # Spits out error message 
  else:
         print("Invalid, try again.")

max_score = 50
# _ denotes that we dont care what variable is instead of using i to find specific variable
# finding the range with 'players' variables
player_scores = [0 for _ in range(players)]
# Setting boundarie for max variable to be less than the 'max_score'
while max(player_scores) < max_score:  
    # for loop
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started")
        print("Your total score is:", player_scores[player_idx], "\n")
        # keeps track of players score
        current_score = 0
    
        while True:
        # Setting up input for a question
          should_roll = input("Would you like to roll (y)? \n")
          # if player does a capital Y, the command still works
          if should_roll.lower() != "y":
              break
          
          # Tells the player if they rolled a 1 or can continue
          value = roll()
          if value == 1:
              print("You rolled a 1! Turn done!")
              current_score = 0
              break
          else:
              # adds current score with new value
              current_score += value
              print("You rolled a", value)

          print("Your score is:", current_score)

        # players score plus players index points plus and equals to current score 
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Leaderboard
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)