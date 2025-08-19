import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for computer"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("\n--- Welcome to Rock-Paper-Scissors Game ---")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    
    while True:
        # Get user choice
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print(" Invalid choice. Please try again.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f" You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")

        
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print(" It's a tie!")
        elif result == "user":
            print(" You win this round!")
            user_score += 1
        else:
            print(" Computer wins this round!")
            computer_score += 1

        
        print(f" Scores => You: {user_score} | Computer: {computer_score}")

        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n--- Final Score ---")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print(" Congratulations, You are the overall winner!")
            elif user_score < computer_score:
                print(" Computer wins overall! Better luck next time.")
            else:
                print(" It's an overall tie!")
            print("Thanks for playing! ")
            break

play_game()