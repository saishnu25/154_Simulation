import time
import random

def calculateHandValues(cards):
    haveAces = 1 in cards
    handValues = []

    if haveAces:
        numAces = cards.count(1)
        possibleAces = [(x,y) for x in [0, 1, 2, 3, 4] for y in [0, 1, 2, 3, 4] if x + y == numAces]
        temp = sum(cards) - numAces                                                           
        possibleHands = [temp + (x * 1) + (y * 11) for (x,y) in possibleAces] 
        for i in possibleHands:
            if i <= 21:
                handValues.append(                                                                                                                                                                                                                                                   i)
    else:
        temp = sum(cards)
        if temp <= 21:
            handValues.append(temp)
    return handValues

def softHand(handVal, dealerCard):
    if handVal > 18:
        return "STAND"
    elif handVal == 18:
        if dealerCard in [9, 10, 1]:
            return "HIT"
        else:
            return "STAND"
    else:
        return "HIT"

def hardHand(handVal, dealerCard):
    if handVal >= 17:
        return "STAND"
    elif handVal > 12:
        if dealerCard in [6, 7, 8, 9, 10, 1]:
            return "HIT"
        else:
            return "STAND"
    elif handVal == 12:
        if dealerCard in [4, 5, 6]:
            return "STAND"
        else:
            return "HIT"
    else:
        return "HIT"

def hitOrStand(playerCards, dealerCards, policy):
    handValues = calculateHandValues(playerCards)
    
    #Stick >= 17
    if policy == 0:
        for i in handValues:
            # Stand >= 17
            if i >= 17:
                return "STAND"
        return "HIT"
    
    #Stick >= Hard 17
    elif policy == 1:
        if handValues[len(handValues) - 1] >= 17:
            return "STAND"
        else:
            return "HIT"
    
    #Always stick
    elif policy == 2:
        return "STAND"

    #Stick >= 17, if dealer < 7 and player > 11, stick. Else hit.
    elif policy == 3:
        if (max(handValues) >= 17):
            return "STAND"
        if (dealerCards[1] < 7 and dealerCards[1] > 1 and max(handValues) > 11):
            return "STAND"
        return "HIT"

    #Stick >= 17, if dealer < 7 and player > 14, stick. Else hit.
    elif policy == 4:
        if (max(handValues) >= 17):
            return "STAND"
        if (dealerCards[1] < 7 and dealerCards[1] > 1 and max(handValues) > 14):
            return "STAND"
        return "HIT"


def pickCardsSingle(deck, cardAmt, firstCard):
    deckLength = 52 - firstCard
    for i in range(cardAmt):
        card = int(random.random() * deckLength) + firstCard
        deck[firstCard], deck[card] = deck[card], deck[firstCard]
        firstCard += 1
        deckLength = 52 - firstCard
    return deck, firstCard

def singleDeck(policy):
    
    deckStart = 0
    # Initial deck of cards
    deck = [1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10,
            10, 10, 10, 10]
    
    deck, deckStart = pickCardsSingle(deck, 2, deckStart)
    
    playerCards = [deck[0], deck[1]]

    
    deck, deckStart = pickCardsSingle(deck, 2, deckStart)
    
    dealerCards = [deck[2], deck[3]]

    playerDecision = ""

    while playerDecision != "STAND":
        
        handValues = calculateHandValues(playerCards)
        
        if handValues == []:
            return False
       
        if handValues[0] == 21:
            return True
        
        playerDecision = hitOrStand(playerCards, dealerCards, policy)
       
        if playerDecision == "HIT":
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            playerCards.append(deck[deckStart - 1])

    dealerDecision = ""
    
    while dealerDecision != "STAND":
        handValues = calculateHandValues(dealerCards)
        
        if handValues == []:
            return True
        
        if handValues[0] == 21:
            return False
        
        if handValues[0] == 17 and len(handValues) == 2:
            dealerDecision = "HIT"  
        elif handValues[0] >= 17:  
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT" 
        if dealerDecision == "HIT":  
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            dealerCards.append(deck[deckStart - 1])

    #Showdown
    playerCardValue = calculateHandValues(playerCards)[0]
    dealerCardValue = calculateHandValues(dealerCards)[0]

    # Win = 1; Loss = 0; Tie = 2
    if playerCardValue > dealerCardValue:
        return 1  
    elif playerCardValue < dealerCardValue:
        return 0  
    else:
        return 2 

def pickCardsInfinite():
    infinite = [1, 1, 1, 1,
                2, 2, 2, 2,
                3, 3, 3, 3,
                4, 4, 4, 4,
                5, 5, 5, 5,
                6, 6, 6, 6,
                7, 7, 7, 7,
                8, 8, 8, 8,
                9, 9, 9, 9,
                10, 10, 10, 10,
                10, 10, 10, 10,
                10, 10, 10, 10,
                10, 10, 10, 10]
    card = int(random.random() * 52)
    return infinite[card]

# INFINITE DECK
def infiniteDeck(policy):
    playerCards = [pickCardsInfinite(), pickCardsInfinite()]

    dealerCards = [pickCardsInfinite(), pickCardsInfinite()]

    playerDecision = ""
    while playerDecision != "STAND":
        handValues = calculateHandValues(playerCards)
        if handValues == []:
            return False
        if handValues[0] == 21:
            return True
        playerDecision = hitOrStand(playerCards, dealerCards, policy)
        if playerDecision == "HIT":
            playerCards.append(pickCardsInfinite())

    dealerDecision = ""
    while dealerDecision != "STAND":
        handValues = calculateHandValues(dealerCards)
        if handValues == []:
            return True 
        if handValues[0] == 21:
            return False 
        if handValues[0] == 17 and len(handValues) == 2:
            dealerDecision = "HIT"
        elif handValues[0] >= 17:
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT"
        if dealerDecision == "HIT":
            dealerCards.append(pickCardsInfinite())

    #SHOWDOWN
    playerCardValue = calculateHandValues(playerCards)[0]
    dealerCardValue = calculateHandValues(dealerCards)[0]

    # Win = 1; Loss = 0; Tie = 2
    if playerCardValue > dealerCardValue:
        return 1  
    elif playerCardValue < dealerCardValue:
        return 0  
    else:
        return 2 

# Function for counting the number of wins, losses, and ties
def blackjackGame(playerPolicy, deckType, n):
    random.seed(time.time())
    wins = 0
    losses = 0
    ties = 0

    for i in range(n):
        if deckType:
            wonGame = singleDeck(playerPolicy)
        else:
            wonGame = infiniteDeck(playerPolicy)
        if wonGame == 1:
            wins += 1
        elif wonGame == 0:
            losses += 1
        else:
            ties += 1

    if n - ties == 0:
        return wins, losses, ties, 0
    avg = wins / (n - ties) * 100
    return wins, losses, ties, avg