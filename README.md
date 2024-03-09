# Hangman

Hangman is a classic game in which one player thinks of a word, and the other player tries to guess it within a certain number of attempts. This implementation allows you to play against the computer, which randomly selects a word for you to guess.

## Description

This project is a Python-based implementation of the classic Hangman game. The computer randomly chooses a word from a predefined list, and the user tries to guess it one letter at a time. The aim of the project is to offer a fun and interactive way to engage with the traditional Hangman game while practicing and demonstrating basic Python programming concepts.

## Installation

To play this version of Hangman, follow these simple steps:

1. Clone this repository to your local machine.
2. Ensure Python is installed on your system.
3. Navigate to the directory where you cloned the repository.
4. Run the `hangman.py` script using Python.

## Usage

To start the game:

1. Execute the `hangman.py` file with Python.
2. The game will prompt you to guess a letter.
3. Enter your guesses one letter at a time.
4. The game provides immediate feedback on your guess, indicating whether it's correct, incorrect, or if it's a letter you've already tried.
5. If your guess is incorrect, the game will notify you and update you on the remaining number of lives.
6. The game continues until you either guess the word correctly or run out of lives.

## Progress and Learning

So far, the game has developed to include:
- Random word selection from a list, giving you a new challenge each time you play.
- Continuous prompting for the user's guess until a valid letter is entered, ensuring engagement throughout the gameplay.
- Detailed feedback to the user on each guess, including whether the guessed letter is in the word, if it's a letter already tried, and updates on the remaining lives for incorrect guesses.
- Introduction of a lives system, where the player starts with a default number of lives, and each incorrect guess reduces this count, adding a layer of challenge to the game.
- Functions to organize the code logically: `check_guess` for checking the guess and updating the game state accordingly, and `ask_for_input` for managing user input and maintaining the game flow.

This incremental development approach, along with the introduction of a lives tracking system, helps in understanding basic Python syntax, functions, loops, conditionals, and the fundamentals of building interactive applications.

## License

This project is licensed under the [MIT License](LICENSE).
