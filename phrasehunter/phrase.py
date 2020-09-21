class Phrase:

    def __init__(self, phrase):

        self.phrase = phrase.lower()


    def __str__(self):

        return self.phrase


    def display(self, guesses):

        for i in range(len(self.phrase)):
            if self.phrase[i] in guesses:
                print(f"{self.phrase[i]} ", end= "")
            elif self.phrase[i] == " ":
                print("  ", end= "")
            else:
                print("_ ", end= "")
        print("\n")


    def check_letter(self, letter):

        return letter in self.phrase


    def check_complete(self, guesses):
        
        complete = True

        for letter in self.phrase:
            if letter == " ":
                continue
            if letter not in guesses:
                complete = False

        return complete