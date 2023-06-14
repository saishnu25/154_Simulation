import blackjack
import time
import random

if __name__ == "__main__":
    random.seed(time.time())

    print("Blackjack")
    print("---------------------------")


    # Player chooses policy
    while True:
        print("Policy: ")
        print("\t0 - Stick >= 17")
        print("\t1 - Stick >= Hard 17")
        print("\t2 - Always Stick")
        print("\t3 - Stick >= 17, if dealer < 7 and player > 11, stick. Else hit.")
        print("\t4 - Stick >= 17, if dealer < 7 and player > 14, stick. Else hit.")
        inputPolicy = int(input("Press 0,1,2,3, or 4: "))
        if inputPolicy == 0:
            break
        if inputPolicy == 1:
            break
        if inputPolicy == 2:
            break
        if inputPolicy == 3:
            break
        if inputPolicy == 4:
            break
        print("Invalid Input!\n")

    # Player chooses deck type
    while True:
        print("\nDeck Type:")
        print("\t0 - Infinite Deck")
        print("\t1 - Single Deck")
        inputDeck = int(input("Enter deck type (0 or 1): "))
        if inputDeck == 0:
            break
        if inputDeck == 1:
            break
        print("Invalid Input!\n")

    inputIterations = int(input("\nNumber of games?: "))

    # Calculate time and number of wins, losses, ties
    start = time.time()
    win, loss, ties, avg = blackjack.blackjackGame(inputPolicy, inputDeck, inputIterations)
    t = time.time() - start

    print("---------------------")
    print("Policy:", inputPolicy,", Deck: ", inputDeck, ", Games: ", inputIterations)
    print("wins:", win)
    print("Loss:", loss)
    print("Ties:", ties)
    print("Avg. Win:", avg,"%")
    print("Time:", t)