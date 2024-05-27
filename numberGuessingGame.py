import random

#define range and maximum attempt
def take_number():
    lower_range = int(input('Enter lower range:\n'))
    upper_range = int(input('Enter upper range:\n'))
    max_attempt = 10
    
    number = secret_number(lower_range, upper_range)
    return lower_range, upper_range, max_attempt, number

#generate random secret number
def secret_number(lower_ranage, upper_range):
    return random.randint(lower_ranage, upper_range)

#Get the user's guess
def take_guess(lower_range, upper_range):
    while True:
        guess = int(input('Enter your guess:\n'))
        if guess < lower_range or guess > upper_range:
            print('Invalid guess, please try again')
        else:
            return guess

#validation of guess
def check_guess(guess, number, lower_range, upper_range):
    if guess == number:
        return "Correct"
    elif guess < number:
        return "Too low"
    else:
        return "Too high"
    #push to git hub
#track number of attempts, detect if game is over
def play_game(lower_range, upper_range, max_attempt, number):
    attempts = 0
    won = False

    while attempts < max_attempt:
        attempts += 1
        guess = take_guess(lower_range, upper_range)
        result = check_guess(guess, number, lower_range, upper_range)

        if result == "Correct":
            print(f"Congratulations! You guessed the number {number} in {attempts} attempt.")
            won = True
            break
        else:
            print(f"{result}. Try again")
    
    if not won:
        print(f"Sorry, you ran out of attempts. The number was {number}")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    lower_range, upper_range, max_attempt, number = take_number()
    play_game(lower_range, upper_range, max_attempt, number)

