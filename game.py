import random

def play_game():
    print("🎯 Welcome to Number Guessing Game!")
    while True:
        print("Choose difficulty: easy (1-50), medium (1-100), hard (1-500)")
        level = input("Enter difficulty: ").lower()

        if level == "easy":
            max_num = 50
        elif level == "hard":
            max_num = 500
        else:
            max_num = 100

        number = random.randint(1, max_num)
        attempts = 0

        print(f"Guess a number between 1 and {max_num}")

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

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    play_game()
