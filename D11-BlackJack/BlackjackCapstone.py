#Creating Blackjack in python

#Joker,King,Queen  = 10
#Ace = 1,11 depending on what the user wants

#Create A dictionary that will hold the card and the value associated with it.

#Have a random hand generator that picks the player's hand and the dealer's hand

#Have a conditional that asks the player if they want to make an ace a 1 or an 11.

#Have another condition that check to see if their hand is over 21

#Have another conditional that ask them if they want to pick another card again

import random

clubs = {
    'cace': 11,
    'cking' : 10,
    'cqueen': 10,
    'cjack': 10,
    "c10": 10,
    "c9": 9,
    "c8": 8,
    "c7": 7,
    "c6": 6,
    "c5": 5,
    "c4": 4,
    "c3": 3,
    "c2": 2,
    "c1": 1
}

diamonds = {
    'dace': 11,
    'dking' : 10,
    'dqueen': 10,
    'djack': 10,
    "d10": 10,
    "d9": 9,
    "d8": 8,
    "d7": 7,
    "d6": 6,
    "d5": 5,
    "d4": 4,
    "d3": 3,
    "d2": 2,
    "d1": 1
}

hearts = {
    'hace': 11,
    'hking' : 10,
    'hqueen': 10,
    'hjack': 10,
    "h10": 10,
    "h9": 9,
    "h8": 8,
    "h7": 7,
    "h6": 6,
    "h5": 5,
    "h4": 4,
    "h3": 3,
    "h2": 2,
    "h1": 1
}

spades = {
    'sace': 11,
    'sking' : 10,
    'squeen': 10,
    'sjack': 10,
    "s10": 10,
    "s9": 9,
    "s8": 8,
    "s7": 7,
    "s6": 6,
    "s5": 5,
    "s4": 4,
    "s3": 3,
    "s2": 2,
    "s1": 1
}


cards = [
        clubs,
        spades,
        hearts,
        diamonds
]

prompt = "> "

#doesn't clear the history of the past cards if rematch is chosen
#doesn't correctly determine the winner of the game
#the switch from 11 to 1 doesn't work correctly

def blackjack():
    rematch = True
    while rematch is True:
        player_hand =[]
        dealer_hand =[]



        player_hand, dealer_hand = playerAction(player_hand, dealer_hand)
        player_score, dealer_score =calc(player_hand,dealer_hand)
        while (player_score < 21) and (dealer_score < 21): 
            deal = input(f"{prompt}Would you like to deal again? (Y or N)")
            if deal.upper() == "Y":
                player_hand, dealer_hand = playerAction(player_hand,dealer_hand)
                player_score, dealer_score = calc(player_hand, dealer_hand)
            else:
                break
        if player_score == 21 or ((player_score < 21) and (player_score > dealer_score)):
            print("Player wins")
            ans = input(f"{prompt}Would you like to have a rematch \? (Y or N)")
            if ans.upper() == "Y":
                player_hand.clear()
                dealer_hand.clear()
        else:
            print("Dealer wins")
            ans = input(f"{prompt}Would you like to have a rematch \? (Y or N)")
            if ans.upper() == "Y":
                player_hand.clear()
                dealer_hand.clear()
            else:
                rematch = False
def showHand(player_hand,dealer_hand):
    print(f"Your hand is {player_hand}\n\nThe dealer's hand is {dealer_hand}")

def playerAction(player_hand, dealer_hand):
    for key,value in player_hand:
        if len(key) == 4:
            answer = input(f"{prompt}Would you like to change the 11 into a 1? (Y or N)") 
            if answer == "Y":
                value = 1
    for key,value in dealer_hand:
        if len(key) == 4:
            answer = random.choice(["Y","N"]) 
            if answer == "Y":
                value = 1
    for suits in cards:
        suit1 = random.choice(cards)
        for card in suit1:
            c1 = random.choice(list(suit1.items()))
            if c1 in player_hand:
                continue
    player_hand.append(c1)

    for suits in cards:
        suit2 = random.choice(cards)
        for card in suit1:
            c2 = random.choice(list(suit2.items()))
            if c2 in dealer_hand:
                continue
    dealer_hand.append(c2)
    showHand(player_hand,dealer_hand)
    return player_hand, dealer_hand

def calc(player_hand, dealer_hand):
    ph = dict(player_hand)
    player_score = sum(ph.values())

    dh = dict(dealer_hand)
    dealer_score = sum(dh.values())
    print(10*"=")
    print(player_score, dealer_score)
    print(10*"=")
    return player_score, dealer_score
blackjack()



