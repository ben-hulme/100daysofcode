import os

os.system('cls')

auction_finish  = False
multiple_highs = False
highest_bid = 0
highest_bidder_list = []
bids = {}

while not auction_finish:

    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What is your bid?: $"))

    bids[bidder_name] = bidder_bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if more_bidders == "no":
        os.system('cls')
        auction_finish = True
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bid = bids[bidder]
                highest_bidder = bidder
                highest_bidder_list.clear()
                multiple_highs = False
            elif bids[bidder] == highest_bid:
                highest_bidder_list.append(bidder)
                multiple_highs = True
        if multiple_highs == False:
            print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
        else:
            print(f"There is more than one top bidder. They are {', '.join(highest_bidder_list)}, and {highest_bidder} and the bid was ${highest_bid}.")
    else:
        os.system('cls')