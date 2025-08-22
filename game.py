import random
import logo

print(logo.game_logo)

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 5 lives to guess the number!")

    # Generate random number
    number_to_guess = random.randint(1, 50)
    attempts = 0
    lives = 5  # maximum attempts allowed

    while attempts < lives:
        try:
            guess = int(input(f"Enter your guess (Attempt {attempts+1}/5): "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                return
        except ValueError:
            print("Please enter a valid number!")

    # If all lives are used
    print(f"💀 Game Over! The correct number was {number_to_guess}.")

# Run the game
number_guessing_game()
