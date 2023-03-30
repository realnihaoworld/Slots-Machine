import blackjack
import slots
def main():
    game = "n"
    while game != "B" and "S":
        game = input("Do you want to play blackjack [B] or slots [S]? ")

    if game == "B":
        blackjack.blackjack()
    elif game == "S":
        exec('slots')

if __name__ == "__main__":
    import blackjack
    main()


