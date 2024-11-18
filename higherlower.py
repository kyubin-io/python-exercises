from game_data import data
import random


def compare(a, b, answer):
    result = 0
    if a["follower_count"] > b["follower_count"]:
        result = "A"
    else:
        result = "B"
    
    return result == answer

score = 0

# create two slots and put random data into them
A = random.choice(data)
B = random.choice(data)

def game(score, A, B):

    print(f"Compare A: {A["name"]}, {A["description"]}, from {A["country"]}.")
    print("VS")
    print(f"Against B: {B["name"]}, {B["description"]}, from {B["country"]}.")

    # let user choose which one has more followers
    winner = input("Who has more followers? Type 'A' or 'B': ")

    # if the user was wrong, print the result and let user know their final score
    result = compare(A, B, winner)
    if result == False:
        return print(f"Sorry, that's wrong. Final score: {score}")



    # if the user wins, print the next question
    else:
        if winner == "B":
            A = B
        B = random.choice(data)
        game(score + 1, A, B)

game(score, A, B)