import random

choices = ("rock", "paper", "scissors")
run = True

while run:

    user = None
    computer = random.choice(choices)

    while user not in choices:
        user = input("Enter a choice (rock, paper, scissors): ")

    print(f"user: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (yes/no): ").lower() == "yes":
        run = False

print("Thanks for playing!")
