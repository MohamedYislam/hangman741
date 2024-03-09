"""
Create a function that will run all the code to run the game as expected. 
You should begin by creating a new script called milestone_5.py. 
Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.


Step 1:
Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

Create a variable called num_lives and assign it to 5
Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game
Pass word_list and num_lives as arguments to the game object
Create a while loop and set the condition to True. In the body of the loop, do the following:
Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'
Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
Step 2:
Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.
"""



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
        """
        Checks the player's guess against the word and updates the game state accordingly.

        Parameters:
            guess (str): The letter guessed by the player.

        Returns:
            None
        """
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
        """
        Continuously prompts the player to guess a letter until a valid guess is made.

        Returns:
            None
        """
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
                self.list_of_guesses.append(guess) # Updating the array to keep count of all valid guesses.
                print(self.list_of_guesses)
                break;


def play_game(word_list):
    num_lives = 5

    game = Hangman(word_list, num_lives)

    while True:
        print(f"{game.num_letters}, num_letters")
        if num_lives == 0:
            print("You lost")
            break;
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations, You've won")
            break;

play_game(["Mercury", "Venus", "Earth", "Mars"])