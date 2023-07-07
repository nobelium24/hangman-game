from random_word import RandomWords

class Word:
    def __init__(self, word):
        self.word = word
        self.guessedLetters = []

    def displayWord(self):
        displayedWord = ""
        for letter in self.word:
            if letter in self.guessedLetters:
                displayedWord += letter
            else:
                displayedWord += "_"
        return displayedWord

    def checkGuess(self, guess):
        self.guessedLetters.append(guess)
        return guess in self.word
    

class HangManGame:
    def __init__(self):
        random = RandomWords()
        randomWord = random.get_random_word()
        self.word = Word(randomWord)
        self.wrongGuesses = 0
        self.hangingState = [
            """
            ____
            |    |
                |
                |
                |
                |
            """,
            """
            ____
            |    |
            O    |
                |
                |
                |
            """,
            """
            ____
            |    |
            O    |
            |    |
                |
                |
            """,
            """
            ____
            |    |
            O    |
            /|    |
                |
                |
            """,
            """
            ____
            |    |
            O    |
            /|\\   |
                |
                |
            """,
            """
            ____
            |    |
            O    |
            /|\\   |
            /     |
                |
            """,
            """
            ____
            |    |
            O    |
            /|\\   |
            / \\   |
                |
            """
        ]

    def displayASCIIArt(self):
        art = """
        _    _                                         
        | |  | |                                        
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                            |___/                       
        """
        print(art)
        return art   
    
    def displayASCIIArt2(self):
        print(self.hangingState[self.wrongGuesses])

    def displayGameState(self):
        self.displayASCIIArt()
        self.displayASCIIArt2()
        print("New Word: ", self.word.displayWord())
        print("Guessed Letters: ", self.word.guessedLetters)
        print("Incorrect Guesses: ", self.wrongGuesses)

    def getGuess(self):
        while True:
            guess = input("Make a guess: ")
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Don't be stupid, enter a single letter 😒.")

    def checkDuplicate(self):
        while True:
            word = self.getGuess()
            if word in self.word.guessedLetters:
                print("You've made this guess before, baka.")
            else:
                return word

    def run(self):
        print("Welcome to Nobelium's hangman 😁")
        self.displayGameState()

        while self.wrongGuesses < 6:
            guess = self.checkDuplicate()

            if guess is not None:
                if self.word.checkGuess(guess):
                    print("Bravo, a correct guess 😁🥳")
                else:
                    print("Baka! Incorrect guess 😒🤦‍♂️")
                    self.wrongGuesses += 1

            self.displayGameState()
            if "_" not in self.word.displayWord():
                print("Congratulations on winning the game! 🥳😁")
                return

        print("You lost 😭. Try again, the word was actually: ", self.word.word)


game = HangManGame()            
game.run()
