import random


class Hangman:
    """
    A class to represent a Hangman game.

    Attributes:
        word_list (list of str): A list of words for the game.
        num_lives (int): The number of incorrect guesses allowed.
        word (str): The word to be guessed, selected randomly at the start.
        word_guessed (list of str): The current state of guesses, initially all underscores.
        num_letters (int): The number of unique letters in the word that haven't been guessed yet.
        list_of_guesses (list of str): Letters that have been guessed so far.
    """
    
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new instance of the Hangman game.

        Parameters:
            word_list (list of str): The list of potential words to guess.
            num_lives (int): The initial number of lives the player has.
        """
        self.word_list = word_list
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def _check_guess(self, guess):
        """
        Checks the player's guess against the word and updates the game state accordingly.
        Parameters:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess, {guess} is in the word")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            print(f"{' '.join(self.word_guessed)}")
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"{guess} is not in the word, try again, you have {self.num_lives} remaining")

    def ask_for_input(self):
        """
        Continuously prompts the player to guess a letter until a valid guess is made.
        """
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried the letter {guess}")
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Starts the Hangman game with a given list of words.
    
    Parameters:
        word_list (list of str): The list of words to use in the game.
    """
    game = Hangman(word_list, num_lives=5)

    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()

    if game.num_letters == 0:
        print("Congratulations, You've won")
    else:
        print("You lost")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
