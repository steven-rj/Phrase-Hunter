import random

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []


    def start(self):

        self.welcome()

        # creates game loop

        # calls get_guess()

        # adds player's guess to the guesses list

        # increments missed if guess incorrect

        # calls game_over()


    def get_random_phrase(self):

        return random.choice(self.phrases)


    def welcome(self):

        print("Welcome to P-H-R-A-S-E--H-U-N-T-E-R!!")

    
    def get_guess(self):

        # get guess from user; adds it to self.guesses
        pass


    def game_over(self):

        # print win or lose message
        pass
