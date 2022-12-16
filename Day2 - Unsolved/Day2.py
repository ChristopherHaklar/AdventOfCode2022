# Open the file with the opponent's choices and your responses
with open('choices.txt', 'r') as f:
  # Initialize the total score to 0
  total_score = 0
  # Read through the file line by line
  for line in f:
    # Split the line into the opponent's choice and your response
    opponent_choice, your_response = line.split()
    # Determine the outcome of the round based on the choices
    if opponent_choice == your_response:
      # Draw: add 3 points for the draw
      if opponent_choice == 'A':
        # Add 1 point for Rock
        total_score += 4
      elif opponent_choice == 'B':
        # Add 2 points for Paper
        total_score += 5
      else:
        # Add 3 points for Scissors
        total_score += 6
    elif (opponent_choice, your_response) == ('A', 'Y'):
      # You win: add 6 points for the win and 2 points for Paper
      total_score += 8
    elif (opponent_choice, your_response) == ('B', 'Z'):
      # You win: add 6 points for the win and 3 points for Scissors
      total_score += 9
    elif (opponent_choice, your_response) == ('C', 'X'):
      # You win: add 6 points for the win and 1 point for Rock
      total_score += 7
    elif (opponent_choice, your_response) == ('A', 'X'):
      # Draw: add 3 points for the draw and 1 point for Rock
      total_score += 4
    elif (opponent_choice, your_response) == ('B', 'Y'):
      # Draw: add 3 points for the draw and 2 points for Paper
      total_score += 5
    elif (opponent_choice, your_response) == ('C', 'Z'):
      # Draw: add 3 points for the draw and 3 points for Scissors
      total_score += 6
    else:
      # You lose: subtract 3 points for the loss
      total_score -= 3
  # Print the total score at the end
  print(total_score)
