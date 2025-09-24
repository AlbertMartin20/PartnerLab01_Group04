import random

def play_guessing_game():
    """Run the guessing game with detailed hints and positive win messages."""
    play_again = "Y"
    while play_again.upper() == "Y":
        secret_number = random.randint(1, 100)
        tries = 5
        print("\nI'm thinking of a number between 1 and 100.")
        print(f"Guess what it is. You have {tries} tries:", end=" ")

        attempt = 0  # track number of guesses
        while tries > 0:
            try:
                guess = int(input())
            except ValueError:
                print("Please enter a valid number:", end=" ")
                continue

            attempt += 1

            if guess == secret_number:
                if attempt == 1:
                    print("Incredible!!! You guessed it on the FIRST try! Jackpot Winner!")
                else:
                    print("Congratulations! You guessed the number correctly. Well done!")
                break
            else:
                tries -= 1
                difference = abs(secret_number - guess)

                if guess < secret_number:
                    if difference > 10:
                        hint = "Too low!"
                    else:
                        hint = "Low!"
                else:
                    if difference > 10:
                        hint = "Too high!"
                    else:
                        hint = "High!"

                if tries > 0:
                    print(f"Nope! {hint} Try again ({tries} tries left):", end=" ")
                else:
                    print(f"Nope! You lost. The number was {secret_number}")
        
        play_again = input("Do you want to play again? (Y/N): ")
