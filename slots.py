import random as rnd

# emoji list
symbols = ['🍎', '🍍', '🎰', '🎉', '💎']
iconDict = {
    (1, 2, 3, 4, 5, 6, 7, 8): '🍎',
    (9, 10, 11, 12): '🍍',
    (13): '🎰',
    (14, 15, 16, 17, 18): '🎉',
    (19, 20): '💎'
}
def main():

    # checks if bet amount is valid
    total = int(input("How much do you want to add to your balance? "))

    # print statement describing game and different bets
    print("Welcome to my slot machine! Here you can make normal rolls ($0.50) or jackpot rolls (all in!)")
    print("---------------------------------------------------------------------------------------------")

    # ask player to put money into slot machine
    amount = int(input("How much do you want to put into the slot machine? "))

    while amount > total:
        amount = int(input(f"You can not exceed ${total}. Enter different amount: "))

    betType = input("Do you want a normal (n) or jackpot roll? (j) ")


# assigns values to a list to determine which icon
def playSlots():
    slotIcons = [0] * 3
    for icons in range(len(slotIcons)):
        slotIcons[icons] = rnd.randint(1, 50)

    return slotIcons

if __name__ == "__main__":
    main()