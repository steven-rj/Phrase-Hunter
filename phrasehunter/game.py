import random
from .phrase import Phrase

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = [Phrase("cat in the hat"), Phrase("boy who cried wolf"), Phrase("the fox and the hound"), Phrase("the sword in the stone"), Phrase("robin hood")]
        self.active_phrase = None
        self.guesses = []


    def start(self):

        self.welcome()

        # creates game loop
        self.active_phrase = self.get_random_phrase()
        # calls get_guess()
        guess = self.get_guess()
        # adds player's guess to the guesses list
        self.guesses.append(guess)
        # increments missed if guess incorrect
        if guess not in self.active_phrase:
            self.missed += 1
            print(f"{guess} isn't in the phrase!")
            print(f"You have {5 - self.missed} lives left!")
        # calls game_over()
        if self.missed > 5:
            game_over()


    def get_random_phrase(self):

        return random.choice(self.phrases)


    def welcome(self):

        print("Welcome to P-H-R-A-S-E--H-U-N-T-E-R!!")

    
    def get_guess(self):

        # get guess from user, verifies it's a letter and hasn't been guessed yet
        guess = ""
        while not guess.isalpha():
            guess = input("Enter a letter to guess >> ").lower()

            if guess in self.guesses:
                print("You've alread guessed that letter!")
                print(self.guesses)
                guess = ""

        return guess

    def game_over(self):

        # print win or lose message
        print("Game Over!")
