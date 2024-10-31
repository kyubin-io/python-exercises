import random

def attempts(type):
    if type == "hard":
        return 5
    else:
        return 10

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is 100")
type = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randrange(1,101)
count = attempts(type)



while (count):
    print(f"You have {count} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high.")
    elif guess < random_number:
        print("Too low.")
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}")
        break

    print("Guess Again.")
    count -= 1

print("You've run out of guesses, you lose.")

