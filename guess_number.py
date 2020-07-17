import random

def guess_game():
    guesses = 0
    number_guess = random.randint(1, 100)
    print(number_guess)
    guess = input("Guess a number from 1 to 100: ")
    while True:
        try:
            if int(guess) == number_guess:
                guesses += 1
                print(f"You guessed the number in {guesses} tries!")
                break
            elif int(guess) > number_guess:
                guesses += 1
                guess = input(f"The number is lower than {guess}. Try again! ")
            else:
                guesses += 1
                guess = input(f"The number is higher than {guess}. Try again! ")
        except ValueError:
            print("Please enter a valid number!")

    play_again = input("Would you like to play again? [Y/N] ")
    if play_again.lower() == "y":
        guess_game()

if __name__ == '__main__':
    guess_game()