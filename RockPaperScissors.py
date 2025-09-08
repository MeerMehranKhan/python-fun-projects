import random

def determine_winner(user, computer, user_score, computer_score):
    if user == computer:
        print("Draw")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win!")
        user_score += 1
        print(f"Your Score: {user_score}")
        if user == "Scissors":
            print(f"{user} beat {computer}")
        else:
            print(f"{user} beats {computer}")
    else:
        print("Computer won")
        computer_score += 1
        print(f"Computer Score: {computer_score}")
        if computer == "Scissors":
            print(f"{computer} beat {user}")
        else:
            print(f"{computer} beats {user}")
    
    return user_score, computer_score   # 🔑 return updated scores


def main():
    choices = ["Rock", "Paper", "Scissors"]
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("Enter your choice: ").lower().capitalize()
        if user_choice not in choices:
            print("Invalid choice, enter again: ")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")

        user_score, comp_score = determine_winner(user_choice, comp_choice, user_score, comp_score)

        play_again = input("Wanna play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print(f"\nFinal Score -> You: {user_score} | Computer: {comp_score}")
            break


if __name__ == "__main__":
    main()