import random

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < number:
                print("Too Low! Try again.")
            elif guess > number:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for playing!")
            break

if _name_ == "_main_":
    main()
