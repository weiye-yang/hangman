import random
import string

class Hangman(object):
    def __init__(self):
        self.answer = ""
        self.currentState = []
        self.lives = 6
        self.guessedLetters = set()
    letters = string.ascii_letters
    
    def reset(self): #resets game, and generates new answer. must be called at start of game
        with open("sowpods.txt", "r") as open_file:
            sowpods = open_file.read().split("\n")
            
        self.answer = random.choice(sowpods)
        self.currentState = []
        for i in self.answer:
            self.currentState.append("_")
        self.lives = 6
        self.guessedLetters = set()
            
    def guess(self):#guess a single letter, which hasn't been guessed before. It gets added to guessedLetters
        guessLetter = ""
        while len(guessLetter) != 1 or guessLetter not in self.letters or guessLetter in self.guessedLetters:
            guessLetter = input("You have {0} lives left. Guess a letter: ".format(self.lives))
            guessLetter = guessLetter.upper()
            if guessLetter in self.guessedLetters:
                print("You have already guessed that letter.")
        
        self.guessedLetters.add(guessLetter)
        return guessLetter
    
    def evalLetter(self, letter):#check if a letter is in the answer, if it is, change some underscores to the letter
        #returns a boolean: whether the letter was in the answer
        changed = False
        for i in range(0,len(self.answer)):
            if self.answer[i] == letter:
                self.currentState[i] = letter
                changed = True
        return changed
    
    def loseLife(self):
        self.lives = self.lives - 1
    
    def checkVictory(self): #checks if there are no underscores left
        for char in self.currentState:
            if char == "_":
                return False
        return True
    
    def print(self): #print current state
        print (" ".join(self.currentState))

if __name__ == "__main__":
    game = Hangman()
    game.reset()
    print(game.answer)