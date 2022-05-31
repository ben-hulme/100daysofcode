import os
import random

card_deck = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

keep_playing = True
player_over = False

while keep_playing:

    dealer_cards = []
    player_cards = []
    player_add_card = True

    def deal_cards(player_deal, dealer_deal, number_of_cards):
        for _ in range(number_of_cards):
            if player_deal and not dealer_deal:
                player_cards.append(random.choice(list(card_deck)))
            if dealer_deal and not player_deal:
                dealer_cards.append(random.choice(list(card_deck)))
            if dealer_deal and player_deal:
                player_cards.append(random.choice(list(card_deck)))
                dealer_cards.append(random.choice(list(card_deck)))

    def calculate_score(cards, dealer_player):
        global dealer_score, player_score
        score = 0
        no_aces = 0

        for card in cards:
            score += card_deck[card]
            if card == "A":
                no_aces += 1
        for no in range(no_aces):
            if score > 21 and no_aces > 0:
                score -= 10
        if dealer_player:
            dealer_score = 0
            dealer_score = score
        if not dealer_player:
            player_score = 0
            player_score = score

    def display_first_results():
        if len(player_cards) == 2 and player_score == 21:
            print(f"You have Blackjack: {player_cards}, Score: {player_score}")
            play_again_func()
        elif len(dealer_cards) == 2 and dealer_score == 21:
            print(f"The Dealer has Blackjack: {dealer_cards}, Score: {dealer_score}")
            play_again_func()
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer first card: {dealer_cards[0]}.")

    def final_results():
        while dealer_score < 17 and not player_over:
            deal_cards(False, True, 1)
            calculate_score(dealer_cards, True)
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computers final hand: {dealer_cards}, final score: {dealer_score}")
        if player_score > dealer_score and player_score <= 21:
            print("You Win!")
        elif player_score > 21:
            print("You went over. You Loose!")
        elif dealer_score > 21 and player_score <= 21:
            print("Computer went over. You Win!")
        elif player_score == dealer_score:
            print("Draw!")
        elif dealer_score > player_score:
            print("You Loose!")

    deal_cards(True, True, 2)
    calculate_score(player_cards, False)
    calculate_score(dealer_cards, True)
    display_first_results()

    def play_again_func():
        global keep_playing
        play_again = input("Do you want to play again? 'y' or 'n'? ")
        if play_again == 'n':
            keep_playing = False

    while player_add_card:
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card == "y":
            deal_cards(True, False, 1)
            calculate_score(player_cards, False)
            display_first_results()
            if player_score > 21:
                player_add_card = False
                player_over = True
                calculate_score(dealer_cards, True)
                final_results()
        else:
            player_add_card = False
            final_results()
    
    play_again_func()
    
    os.system('cls')