class Phrase:

    def __init__(self, phrase):

        self.phrase = phrase.lower()

    def display(self):
        pass

    def check_letter(self, letter):

        return letter in self.phrase

    def check_complete(self):
        pass
    