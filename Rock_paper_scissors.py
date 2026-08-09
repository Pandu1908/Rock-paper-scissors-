import random

def play_game():
    # Valid choices for the game
    choices = ["rock", "paper", "scissors"]
    
    # Initialize scores
    player_score = 0
    computer_score = 0
    
    print("=== Welcome to Rock, Paper, Scissors! ===")
    print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock")
    print("Type 'quit' at any time to exit the game.\n")
    
    while True:
        # Get and clean user input
        user_input = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        
        # Check if player wants to exit
        if user_input == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
            break
            
        # Validate input
        if user_input not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue
            
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Game logic to determine the winner
        if user_input == computer_choice:
            print("It's a tie!")
        elif (user_input == "rock" and computer_choice == "scissors") or \
             (user_input == "paper" and computer_choice == "rock") or \
             (user_input == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display current standings
        print(f"Scoreboard -> You: {player_score} | Computer: {computer_score}\n")

# Run the game
if __name__ == "__main__":
    play_game()
