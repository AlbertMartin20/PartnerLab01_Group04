import guessing_game
#from dice_game import roll_dice

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Play Guessing Game")
        print("2. Rock Paper Scissors")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            guessing_game.play_guessing_game()
        elif choice == "2":
            pass
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
