import random as rnd
def earnings(money, bet, winner):
    if winner == "You":
        money += int(bet)
    elif winner == "The dealer":
        money -= int(bet)
    return money

def draw(deck):
    i = rnd.randint(0,12)
    if deck[i]["number"] == 0:
        draw(deck)
    else:
        card = deck[i]["card"]
        deck[i]["number"] -= 1
    return card

def dealerAdd(dealerHand):
    card = draw(deck)
    dealerHand += card
    return dealerHand

def playerAdd(playerHand):
    card = draw(deck)
    playerHand += card
    return playerHand

def checkWinner(player, dealer):
    if player == 21 or dealer > 21:
        winner = "You"
        return winner
    elif dealer == 21 or player > 21:
        winner = "The dealer"
        return winner

def play(playerHand, dealerHand):
    choice = "n"
    while playerHand < 21 and dealerHand < 21:
        if dealerHand > playerHand:
            print("Your hand is less than the dealers, Hit!")
            playerHand = playerAdd(playerHand)

            print("Dealer Hand:" + str(dealerHand))
            print("Player Hand:" + str(playerHand))
        else:
            while choice !=  "h" and choice != "s":
                choice = input("Hit [h] or Stand [s]: ")
            if choice == "h":
                print("Hit!")
                playerHand = playerAdd(playerHand)
                choice = "n"

                print("Dealer Hand:" + str(dealerHand))
                print("Player Hand:" + str(playerHand))
            elif choice == "s":
                print("Stand!")
                dealerHand = dealerAdd(dealerHand)
                choice = "n"


                print("Dealer Hand:" + str(dealerHand))
                print("Player Hand:" + str(playerHand))

    winner = checkWinner(playerHand, dealerHand)
    return winner

def main():
    money = 50

    # BLACKJACK game
    print("Rules:")
    print(
        "The objective is to get a total of 21 without going over and busting. There is one deck, and all cards are equal to their point value; face cards are all worth 10. Aces are worth 1. You and the dealer are each dealt 2 cards, then you have the choice to either hit, drawing another card, or stand, skip and allow the dealer to draw. If you have less than the dealer, you have to draw. This continue until someone reaches 21 or busts.")

    while money > 0 and money < 1000:
        deck = [{"card": 1, "number": 4}, {"card": 2, "number": 4}, {"card": 3, "number": 4}, {"card": 4, "number": 4},
                {"card": 5, "number": 4}, {"card": 6, "number": 4}, {"card": 7, "number": 4}, {"card": 8, "number": 4},
                {"card": 9, "number": 4}, {"card": 10, "number": 4}, {"card": 10, "number": 4},
                {"card": 10, "number": 4}, {"card": 10, "number": 4}]
        dealerHand = 0
        playerHand = 0
        bet = 1001

        print("---------------------------------------------------------------------")
        while bet > money or bet < 0:
            bet = int(input("How much do you want to bet? "))

        dealerHand = dealerAdd(dealerHand)
        playerHand = playerAdd(playerHand)
        dealerHand = dealerAdd(dealerHand)
        playerHand = playerAdd(playerHand)

        print("Dealer Hand:" + str(dealerHand))
        print("Player Hand:" + str(playerHand))

        winner = play(playerHand, dealerHand)

        money = earnings(money, bet, winner)
        print(winner + " won. You have a total of $" + str(money) + ".")

    if money > 1000:
        print("You have won! Congratulations!")
    else:
        print("You have run out of money...")