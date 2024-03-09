import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list   # word_list: list - A list of words
        self.word = random.choice(self.word_list).lower()  # The word to be guessed, picked randomly from the word_list. 
        self.word_guessed = ['_' for _ in self.word] #  A list of the letters of the word, with _ for each letter not yet guessed. 
        # For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
        # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.num_letters = len(set(self.word))  # num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives # num_lives: int - The number of lives the player has at the start of the game.
        self.list_of_guesses = [] # A list of the guesses that have already been tried. Set  to an empty list initially

    # Method to check the player's guess against the selected word
    def _check_guess(self, guess):
        guess = guess.lower()  # Converts the guess to lowercase for comparison
        # If the guess is in the word, update the word_guessed to reflect the correct guess
        if guess in self.word:
            print(f"Good guess, {guess} is in the word")
            # Loop through each letter in the word to find matches and reveal them
            for index, letter in enumerate(self.word):
                # Replace the underscore with the guessed letter if it matches
                if letter == guess:
                    self.word_guessed[index] = letter
            # After revealing the guessed letter, print the current state of word_guessed
            print(f"{self.word_guessed}, self.word_guessed")
            self.num_letters -= 1  # Decrease the count of unique letters yet to be guessed
        else:
            self.num_lives -= 1 # Decreasing the number of lives by one
            print(f"{guess} is not in the word, try again, you have {self.num_lives} remaining") # Informing the user the guess is incorrect, and the remaining attempts they have


    # Method to prompt the player to guess a letter
    def ask_for_input(self):
        while True:  # Loop indefinitely until a valid guess is made
            guess = input("Enter a single letter: ")
            # Validate the input; it must be a single alphabetic character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Check if the guessed letter has already been tried
            elif guess in self.list_of_guesses:
                print(f"You already tried the letter {guess}")
            else:
                # If the guess is valid and not yet tried, check the guess
                self._check_guess(guess)



test = Hangman(["Banana", "Cheese", "Dates"])


print(f"{test.word} word")
print(f"{test.word_guessed} word_guessed")
print(f"{test.word_list} word_list")
print(f"{test.num_letters} num_letter")
print(f"{test.num_lives} num_lives")
print(f"{test.list_of_guesses} list_of_guesses")


print(test.ask_for_input())
