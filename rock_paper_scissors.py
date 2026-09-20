import random
choices = ["rock", "paper", "scissors"]
player = input("Enter rock, paper, or scissors: ").lower()
if player not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
