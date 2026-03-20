import random

options = ["rock", "paper", "scissors"]

wins = 0
losses = 0
ties = 0

while True:
    user_choice = input("Choose rock, paper or scissors (or type 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    
    if user_choice not in options:
        print("Invalid choice, please try again.")
        continue

    computer_choice = random.choice(options)
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! :D")
        wins += 1
    else:
        print("You lose! D:")
        losses += 1

    print(f"Score - Wins: {wins}, Losses: {losses}, Ties: {ties}")
    print("-" * 20)  # easier to read each round