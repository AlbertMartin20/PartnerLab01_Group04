import random

def rock_paper_scissors():
    play = input("Do you want to play? (yes/no): ").strip().lower()

    # Loop runs only while the user keeps saying "yes"
    while play == "yes":
        # Ask for user choice
        user_choice = int(input("Enter your choice: 1. paper, 2. scissors, 3. rock: "))

        # Computer's choice
        computer_choice = random.randint(1, 3)

        # Map numbers to names
        choices = {1: "paper", 2: "scissors", 3: "rock"}

        print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}.")

        # Determine the winner
        if user_choice == computer_choice:
            print("It is a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("Computer wins!")
        print()

        # Ask again at the end of each round
        play = input("Do you want to play again? (yes/no): ").strip().lower()

    print("Okay, thanks for playing!")

# Call the function to start the game
rock_paper_scissors()
