# list karet
# fc a royd8va9 karet
# fnc ktera  to spocita

import random

cards = ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10,
         'A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]


def deal_card(list_of_cards):
    random_card = random.choice(list_of_cards)
    list_of_cards.remove(random_card)
    return random_card


def decide_bet(player_cards, computer_cards):
    diff_p = 21 - count_score(player_cards)
    diff_c = 21 - count_score(computer_cards)
    if diff_c > diff_p or count_score(computer_cards) > 21:
        return 1
    elif diff_c == diff_p:
        return 2
    else:
        return 0


def count_score(list_of_cards):
    score = 0
    score_aone = 0
    for card in list_of_cards:

        if 'A' in list_of_cards:
            if card == 'A':
                score_aone += 1
                score += 11
            elif type(card) == str:
                score += 10
                score_aone += 10
            else:
                score += card
                score_aone += card
        elif type(card) == str:
            score += 10
        else:
            score += card
    if score > 21 and "A" in list_of_cards:
        return score_aone
    else:
        return score


def who_won(computer_cards, player_cards):
    diff_p = 21 - count_score(player_cards)
    diff_c = 21 - count_score(computer_cards)
    if diff_c > diff_p or count_score(computer_cards) > 21:
        return "You WIN"
    elif diff_c == diff_p:
        return "Its a draw"
    else:
        return "You lost"


def one_round():
    play = 1
    while play != 0:
        if count_score(player_cards) == 21 and count_score(computer_cards) != 21:
            print("you WIN blackjack")
            play = 0
            return who_won(computer_cards, player_cards)

        while count_score(computer_cards) < 17:
            computer_cards.append(deal_card(cards))

        if count_score(computer_cards) == 21:
            print("blackjack you loose")
            return who_won(computer_cards, player_cards)

        new_card = input("add card?")
        if new_card == "y":
            player_cards.append(deal_card(cards))
            print(player_cards)
            print(count_score(player_cards))
            if count_score(player_cards) > 21:
                print("looser")
                return who_won(computer_cards, player_cards)

            elif count_score(player_cards) == 21:
                print("BLACKJACK")
                print("you Won")
                return who_won(computer_cards, player_cards)

        else:

            print(f"Player cards are {player_cards}")
            print(f"Computer cards are {computer_cards}")
            return who_won(computer_cards, player_cards)


player_bank = 500
while input("wanna play: ") == "y":
    player_cards = []

    computer_cards = []

    print("your cards")
    player_cards.append(deal_card(cards))
    player_cards.append(deal_card(cards))
    print(player_cards)
    print(count_score(player_cards))

    computer_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))
    print(f" 1rst computer card is {[computer_cards[1]]}")

    bet = int(input("place your bet:"))

    one_round()
    dec = {1: bet, 2: 0, 3: -bet}

    player_bank += dec[decide_bet(player_cards, computer_cards)]

    print(player_bank)

print(f"Your bank is {player_bank}")
