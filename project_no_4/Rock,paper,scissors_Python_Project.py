import random

def game():
    attempts = 5
    user_score = 0
    computer_score = 0
    
    for _ in range(attempts):
        user = input("What's your choice! 'r' for rock, 'p' for paper, 's' for scissor:\n ")
        computer = random.choice(['r', 'p', 's'])
        
        print(f"You chose: {user}, Computer chose: {computer}")
        
        if user == computer:
            print("It's a tie!")
        elif win(user, computer):
            print("You won this round!")
            user_score += 1
        else:
            print("You lost this round!")
            computer_score += 1
    
    print("\nGame Over!")
    print(f"Final Score: You {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie overall!")

def win(player, opponent):
    # r > s, s > p, p > r
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

game()
