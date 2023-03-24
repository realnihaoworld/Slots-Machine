import random as rnd

def earnings(money, bet, winner):
    #Add the amount to what the player has earned so it can display the current money they have.
    if winner == "You":
        money += int(bet)
    elif winner == "The dealer":
        money -= int(bet)
    return money

def draw(deck):
    #draw a card from the deck and remove it from the deck
    i = rnd.randint(0,12)
    if deck[i]["number"] == 0:
        draw(deck)
    else:
        card = deck[i]["card"]
        deck[i]["number"] -= 1
    return card

def add(hand):
    #Add a card to the hand specificed
    card = draw(deck)
    hand += card
    return hand

def checkWinner(player, dealer):
    # see which of the players won the game.
    if player == 21 or dealer > 21:
        winner = "You"
        return winner
    elif dealer == 21 or player > 21:
        winner = "The dealer"
        return winner

def play(playerHand, dealerHand):
    #actually play each hand
    choice = "n"
    while playerHand < 21 and dealerHand < 21:
        #while one of the players hasn't won
        if dealerHand > playerHand:
            #if the players hand is less than the dealer, they have to play.
            print("Your hand is less than the dealers, Hit!")
            playerHand = add(playerHand)
            #print the totals
            print("Dealer Hand:" + str(dealerHand))
            print("Player Hand:" + str(playerHand))
        else:
            # give the player the choice to hit or stand
            while choice != "h" and choice != "s":
                #make sure that they have chosen one of the options
                choice = input("Hit [h] or Stand [s]: ")
            #if they choose to hit, add the card to the players hand and reset the choice.
            if choice == "h":
                print("Hit!")
                playerHand = add(playerHand)
                choice = "n"
                #display totals
                print("Dealer Hand:" + str(dealerHand))
                print("Player Hand:" + str(playerHand))
            #if they choose to stand, add a card to the dealers hand and reset choice
            elif choice == "s":
                print("Stand!")
                dealerHand = add(dealerHand)
                choice = "n"
                #display totals
                print("Dealer Hand:" + str(dealerHand))
                print("Player Hand:" + str(playerHand))
    #determine the winner and return who they are
    winner = checkWinner(playerHand, dealerHand)
    return winner

def main():
    #set baseline money
    money = 50
    print("You have a total of $" + str(money) + ".")
    #continue to play while the player has between 0 and 1000 dollars
    while money > 0 and money < 1000:
        #the card deck resets each hand, as do the totals and the bet
        deck = [{"card":1,"number":4},{"card":2,"number":4},{"card":3,"number":4},{"card":4,"number":4},{"card":5,"number":4},{"card":6,"number":4},{"card":7,"number":4},{"card":8,"number":4},{"card":9,"number":4},{"card":10,"number":4},{"card":10,"number":4},{"card":10,"number":4},{"card":10,"number":4}]
        dealerHand = 0
        playerHand = 0
        bet = 1001
        #barrier between each hand (makes it easier to seperate the hands)
        print("---------------------------------------------------------------------")
        #take bet that is viable
        while bet > money or bet < 0:
            bet = int(input("How much do you want to bet? "))
        #deal the first two cards
        dealerHand = add(dealerHand)
        playerHand = add(playerHand)
        dealerHand = add(dealerHand)
        playerHand = add(playerHand)
        #display starting totals
        print("Dealer Hand:" + str(dealerHand))
        print("Player Hand:" + str(playerHand))
        #play the game and determine a winner
        winner = play(playerHand, dealerHand)
        #determine the amount of money the player has and display winner.
        money = earnings(money, bet, winner)
        print(winner + " won. You have a total of $" + str(money) + ".")
        
    #winning/losing conditions
    if money > 1000:
        print("You have won! Congratulations!")
    else:
        print("You have run out of money...")