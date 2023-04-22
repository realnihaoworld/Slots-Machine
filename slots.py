import random as rnd
import time

iconDict = {
    1: '🍎', 2: '🍎', 3: '🍎', 4: '🍎', 5: '🍎', 6: '🍎', 7: '🍎', 8: '🍎',
    9: '🍍', 10: '🍍', 11: '🍍', 12: '🍍',
    13: '🎰',
    14: '🎉',  15: '🎉', 16: '🎉', 17: '🎉', 18: '🎉',
    19: '🍎', 20: '🍎'
}

moneyDict = {
    '🍎': 10, '🍍': 25, '🎰': 100, '🎉': 50, '': 0
}

def main():
    #TODO make it so that balance has to be greater than 50 cents

    # checks if bet amount is valid
    balance = float(input("How much do you want to add to your balance? "))

    while balance < 1:
        balance = float(input("You must insert at least $1: "))

    # print statement describing game and different bets
    print("Welcome to my slot machine! Here, each roll is $1! Are you ready?")
    print("---------------------------------------------------------------------------------------------")
    time.sleep(2)

    while True:
        # fills numbers list with random numbers between 1-20
        numbersList = fillSlots()

        # gets the symbol corresponding to each number and puts it in its own array
        symbols = fillSymbols(numbersList)

        # prints each icon out to the user
        printIcons(symbols)

        # checks if all symbols are the same
        winIcon = checkWin(symbols)

        # sends earnings back to user
        winnings = earnings(winIcon)

        # print current balance and winnings
        balance -= 1.00
        balance += winnings
        print(f"Your new balance is: ${format(balance, '.2f')}\n")

        if input("Roll again? (Y/N)").strip().upper() != 'Y':
            print("Thanks for playing!")
            print(f"Your final balance is: ${format(balance, '.2f')}")
            break
        elif balance < 1:
            print("You have run out of money, thanks for playing!")
            break

    #TODO check if they have more than 50 cents

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
        winIcon = symbols[0]
        return winIcon
    else:
        print('\n')
        print("You lose :(")
        return winIcon


# matches number with icon, then prints it out
def fillSymbols(numbersList):
    symbols = []
    for num in numbersList:
        emoji = iconDict.get(num)
        symbols.append(emoji)

    return symbols

def printIcons(symbols):
    for x in symbols:
        print("[" + x + "]", end=" ")
        time.sleep(1)

def earnings(winIcon):
    money = 0
    money += moneyDict[winIcon]
    if money > 0:
        print(f"You won ${money}!")
    return money


if __name__ == "__main__":
    main()