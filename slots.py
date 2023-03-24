# checks if bet amount is valid
total = input("How much do you want to add to your balance? ")

# print statement describing game and different bets
print("")

# ask player to put money into slot machine
amount = input("How much do you want to put into the slot machine? ")
while amount > total:
    amount = input("You can not exceed $" + total + ". Enter different amount: ")
