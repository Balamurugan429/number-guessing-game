import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
