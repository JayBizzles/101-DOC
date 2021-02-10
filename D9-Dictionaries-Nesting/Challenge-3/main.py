import os
import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(logo.logo)



collection = {}
biddingFinished = False

def findLargestbidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highestBid}')

while not biddingFinished:

    name = input('input your name\n')

    price = int(input('input your bidding price\n'))

    collection[name] = price

    answer = input('are there other users who want to bid?\n')

    if answer == 'no':
        biddingFinished = True
        findLargestbidder(collection)
    elif answer == 'yes':
        cls()



    
