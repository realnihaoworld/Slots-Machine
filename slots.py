import random as rnd

iconDict = {
    1: '🍎', 2: '🍎', 3: '🍎', 4: '🍎', 5: '🍎', 6: '🍎', 7: '🍎', 8: '🍎',
    9: '🍍', 10: '🍍', 11: '🍍', 12: '🍍',
    13: '🎰',
    14: '🎉',  15: '🎉', 16: '🎉', 17: '🎉', 18: '🎉',
    19: '💎', 20: '💎'
}

def main():

    # checks if bet amount is valid
    balance = int(input("How much do you want to add to your balance? "))

    # print statement describing game and different bets
    print("Welcome to my slot machine! Here, each roll is $0.50! Are you ready?")
    print("---------------------------------------------------------------------------------------------")

    # ask player to put money into slot machine
    amount = int(input("How much do you want to put into the slot machine? "))

    while amount > balance:
        amount = int(input(f"You can not exceed ${balance}. Enter different amount: "))

    # array for rng and icons
    numbersList = playSlots()
    symbols = []

    for num in numbersList:
        emoji = iconDict.get(num)
        symbols.append(emoji)

    for x in symbols:
        print(x)

# assigns values to a list to determine which icon

def playSlots():
    slotIcons = [0] * 3
    for icons in range(len(slotIcons)):
        slotIcons[icons] = rnd.randint(1, 20)

    return slotIcons


if __name__ == "__main__":
    main()