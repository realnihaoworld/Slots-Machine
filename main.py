def main():
    game = "n"
    while game != "B" and game!= "S":
        game = input("Do you want to play blackjack [B] or slots [S]? ")

    if game == "B":
        bj.blackjack()
    elif game == "S":
        s.slots()

if __name__ == "__main__":
    import blackjack as bj
    import slots as s
    main()


