# Lab 1
# Group 4
# Author: Joey Zhen & Thant Zin Aung
# Date: 09/25/2025
# Description: This program lets the user play multiple games (Guessing Game and
# Rock-Paper-Scissors). The user selects from a menu, plays until
# they choose to quit, and can replay each game as desired.

import guessing_game
import rock_paper_scissors_game()

def main():
    """Main entry point of the program.
    Displays a welcome message and a menu of games. 
    Lets the user choose between:
        1. Guessing Game
        2. Rock-Paper-Scissors
        3. Dice Roll
        4. Quit
    Runs the selected game and keeps looping until the user chooses to quit.
    """
    while True:
        print("\n=== Main Menu ===")
        print("1. Play Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            guessing_game.play_guessing_game()
        elif choice == "2":
            rock_paper_scissors_game.rock_paper_scissors()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
