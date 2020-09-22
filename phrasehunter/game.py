import random
import sys

from .phrase import Phrase

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = [
        {"Disney Songs [Hard]": [Phrase("A Girl Worth Fighting For"), Phrase("Out There"), Phrase("I Just Cant Wait To Be King"), Phrase("Friend in Me")]},
        {"Disney Movies [Medium]": [Phrase("The Hunchback of Notre Dame"), Phrase("Mulan"), Phrase("Aladdin"), Phrase("Moana"), Phrase("The Princess and the Frog"), Phrase("The Lion King")]},
        {"Colors [Easy]": [Phrase("blue"), Phrase("green"), Phrase("black")]} ]
        self.active_phrase = None
        self.guesses = []
        self.category = ""


    def start(self):

        self.welcome()
        self.active_phrase = self.get_random_phrase()
        # creates game loop
        while True:       
            print(f"\n\nCategory: {self.category}\n")
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

        category = -1
        while category not in range(1, len(self.phrases)+1):
            try:
                print("\nCategories:")
                for index, subset in enumerate(self.phrases, start=1):
                    for cat in subset.keys():
                        print(index, cat) 
                    
                category = int(input("\nChoose a phrase category number >> "))
            except ValueError:
                print("Enter a category NUMBER!")

        self.category = list(self.phrases[category - 1].keys())[0]

        phrases = list(self.phrases[category - 1].values())[0]
        return random.choice(phrases)


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
        elif message == "win":
            print("\nYOU WON!!")
        
        print(f"The phrase was: '{self.active_phrase}''")

        # ask for replay
        replay = ""
        while replay != "y" and replay != "n":
            replay = input("\nPlay again? [y/n] >> ").lower()
        
        if replay == "y":
            game = Game()
            game.start()
        elif replay == "n":
            sys.exit()
