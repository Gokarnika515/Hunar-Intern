import random

def produce_secret_number():
    # Produces a 4-digit secret number
    return str(random.randint(1000, 9999))

def get_cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0
    secret_count = {}
    guess_count = {}

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    for digit in guess_count:
        if digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

    return cows, bulls

def play_game():
    secret_number = produce_secret_number()
    attempts = 0
    print("Welcome to the Cows and Bulls Game!")
    print("I have generated a 4-digit secret number... Try to guess it!")

    while True:
        guess = input("Enter your guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid guess!... Please enter a 4-digit number")
            continue

        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        print(f"Cows: {cows}, Bulls: {bulls}")

        if bulls == 4:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()

    
