import random
import sys

from .phrase import Phrase

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = [Phrase("cat in the hat"), Phrase("boy who cried wolf"), Phrase("the fox and the hound"), Phrase("the sword in the stone"), Phrase("robin hood")]
        self.active_phrase = None
        self.guesses = []


    def start(self):

        self.welcome()
        self.active_phrase = self.get_random_phrase()
        # creates game loop
        while True:       
            print(f"\n\nCategory: {self.active_phrase}\n")
            self.active_phrase.display(self.guesses)
            
            # calls get_guess()
            guess = self.get_guess()
            # adds player's guess to the guesses list
            self.guesses.append(guess)
            # print(self.guesses)
            self.active_phrase.check_letter(guess)
            # increments missed if guess incorrect
            if not self.active_phrase.check_letter(guess):
                self.missed += 1
                print(f"\n** '{guess}' isn't in the phrase!")
                print(f"** {5 - self.missed} chances left!")
            # calls game_over()
            if self.missed > 4:
                self.game_over("lose")
            elif self.active_phrase.check_complete(self.guesses):
                self.game_over("win")


    def get_random_phrase(self):

        return random.choice(self.phrases)


    def welcome(self):

        print("\n\nP-H-R-A-S-E--H-U-N-T-E-R!!\n")

    
    def get_guess(self):

        # get guess from user, verifies it's a letter and hasn't been guessed yet
        guess = ""
        while not guess.isalpha():
            guess = input("\nEnter a letter to guess >> ").lower()

            if guess in self.guesses:
                print("\nYou've alread guessed that letter!")
                print(f"Past Guesses: {self.guesses}")
                guess = ""

        return guess

    def game_over(self, message):

        # print win or lose message
        if message == "lose":
            print("\nGAME OVER!!")
            print(f"The phrase was: '{self.active_phrase}''")
        elif message == "win":
            print("\nYOU WON!!")
        
        # ask for replay
        replay = ""
        while replay != "y" and replay != "n":
            replay = input("\nPlay again? [y/n] >> ").lower()
        
        if replay == "y":
            game = Game()
            game.start()
        elif replay == "n":
            sys.exit()
