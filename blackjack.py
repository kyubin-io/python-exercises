import random

cards = [1,2,3,4,5,6,7,8,9,10,10,10]

# function으로 감싸기
playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ", )

while(playGame == "y"):
    cardsArray = [random.choice(cards), random.choice(cards)]
    currentScore = sum(cardsArray)
    computersArray = [random.choice(cards), random.choice(cards)]
    computerScore = sum(computersArray)

    print(f"Your cards: {cardsArray}, Current Score: {currentScore}")
    print(f"Computer's first card: {computersArray[0]}")


    getAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

    while(getAnotherCard =="y" and currentScore <= 21):
        cardsArray.append(random.choice(cards))
        print("cardsArray",cardsArray)
        currentScore = sum(cardsArray)
        print(f"Your cards: {cardsArray}, Current Score: {currentScore}")
        print(f"Computer's first card: {computersArray[0]}")
        getAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ")


    print(f"Your final hand: {cardsArray}, Final Score: {currentScore}")
    print(f"Computer's final hand: {computersArray}, Final Score: {computerScore}")

    if currentScore > 21 or (21-currentScore) > (21-computerScore):
        print("You lost")
    elif currentScore == computerScore:
        print("Draw")
    else:
        print("You win.")

    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ", )

