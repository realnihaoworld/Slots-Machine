import random as rnd
import time

iconDict = {
    1: '🍎', 2: '🍎', 3: '🍎', 4: '🍎', 5: '🍎', 6: '🍎', 7: '🍎', 8: '🍎',
    9: '🍍', 10: '🍍', 11: '🍍', 12: '🍍',
    13: '🎰',
    14: '🎉',  15: '🎉', 16: '🎉', 17: '🎉', 18: '🎉',
    19: '💎', 20: '💎'
}

def slots():

    # checks if bet amount is valid
    #balance = int(input("How much do you want to add to your balance? "))
    balance = 50

    # print statement describing game and different bets
    print("Welcome to my slot machine! Here, each roll is $0.50! Are you ready?")
    print("---------------------------------------------------------------------------------------------")

    # ask player to put money into slot machine
    amount = int(input("How much do you want to put into the slot machine? "))

    while amount > balance:
        amount = int(input(f"You can not exceed ${balance}. Enter different amount: "))

    # array for rng and icons
    numbersList = fillSlots()
    symbols = []

    for num in numbersList:
        emoji = iconDict.get(num)
        symbols.append(emoji)

    for x in symbols:
        print("[" + x + "]", end=" ")
        time.sleep(1)



# assigns values to a list to determine which icon

def fillSlots():
    slotIcons = [0] * 3
    for icons in range(len(slotIcons)):
        slotIcons[icons] = rnd.randint(1, 20)

    return slotIcons

def checkWin(symbols):
    win = False
    for x in range(len(symbols) - 1):
        if symbols[x] == symbols[x + 1]:
            win = True
            continue
        else:
            win = False
            break

    winIcon = ''
    if win:
        print('\n')
        print("You win!")
        winIcon = symbols[0]
    else:
        print('\n')
        print("You lose :(")

    print(winIcon)

if __name__ == "__main__":
    slots()