import random

def guessing_game():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("🎯 Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


guessing_game()
