# emoji list
icons = ['🍎', '🍍', '🎰', '🐍', '⚜', '🎉', '💎', '🏆', '♥', '💰']

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
