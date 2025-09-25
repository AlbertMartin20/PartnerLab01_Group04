# Lab 1
# Group 4
# Author: Thant Zin Aung
# Date: 09/25/2025
import random

def play_guessing_game():
    """Play the Guessing Game.
    
    The computer generates a random number between 1 and 100.
    The player has 5 tries to guess the number. After each guess,
    the program provides hints:
        - "Too high/Too low" if the guess is far off (difference > 10).
        - "High/Low" if the guess is close (difference ≤ 10).
    
    Special Features:
        - If the player guesses correctly on the first try, a jackpot
          message is shown.
        - If the player guesses correctly on later tries, a congratulatory
          message is displayed.
        - If the player runs out of tries, the secret number is revealed.
    
    After each round, the player is asked if they want to play again.
    """
    play_again = "Y" # sentinel to control replay of full rounds
    while play_again.upper() == "Y":
        secret_number = random.randint(1, 100) # hidden number the user must guess
        tries = 5
        print("\nI'm thinking of a number between 1 and 100.")
        print(f"Guess what it is. You have {tries} tries:", end=" ")

        attempt = 0  # track number of guesses
        while tries > 0:
            # Read a guess; re-prompt if input is not an integer
            try:
                guess = int(input())
            except ValueError:
                print("Please enter a valid number:", end=" ")
                continue

            attempt += 1
            # Correct guess path 
            if guess == secret_number:
                if attempt == 1:
                    print("Incredible!!! You guessed it on the FIRST try! Jackpot Winner!")
                else:
                    print("Congratulations! You guessed the number correctly. Well done!")
                break
            # Wrong guess path: compute hint & decrement tries 
            else:
                tries -= 1
                difference = abs(secret_number - guess)
                # Directional + proximity hint: "Too high/Too low" (far), "High/Low" (close)
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

                # If there are tries left, prompt again; otherwise reveal the number
                if tries > 0:
                    print(f"Nope! {hint} Try again ({tries} tries left):", end=" ")
                else:
                    print(f"Nope! You lost. The number was {secret_number}")
        
        play_again = input("Do you want to play again? (Y/N): ")
