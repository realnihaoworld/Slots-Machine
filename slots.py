import random as rnd

# emoji list
symbols = ['🍎', '🍍', '🎰', '🐍', '⚜', '🎉', '💎', '🏆', '♥', '💰']

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

    # print(playSlots())

# assigns values to arraycan
def playSlots():
    slotIcons = [0] * 5
    for icons in range(len(slotIcons)):
        slotIcons[icons] = rnd.randint(1, 20)

    return slotIcons

if __name__ == "__main__":
    main()