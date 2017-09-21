import Hangman

def playHangman(game):
    game.reset()
    
    while game.lives > 0:
        game.print()
        guessLttr = game.guess()
        
        if not game.evalLetter(guessLttr):
            print("{0} does not appear in the word.".format(guessLttr))
            game.loseLife()
            continue
        else:
            print("The word has at least one {0}. Nice one.".format(guessLttr))
        
        if game.checkVictory():
            return True
    return False

def playAgain():
    choice = ""
    while(choice != "y" and choice != "n"):
        choice = input("Play again? (y/n): ")
    
    if choice == "y":
        return True
    else:
        return False

def main():
    print("===HANGMAN===")
    print("By Weiye Yang")
    game = Hangman.Hangman()
    while True:
        victory = playHangman(game)
        
        if victory:
            print("You won!")
        else:
            print("You lost.")
        print("The answer was {0}.".format(game.answer))
        
        choice = playAgain()
        if not choice:
            break

if __name__ == "__main__":
    main()