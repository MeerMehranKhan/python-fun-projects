import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ['snake', 'water', 'gun']
    print("Welcome to Snake Water Gun Game!")
    
    user_choice = input("Enter your choice (snake/water/gun): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please choose from snake, water, or gun.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()