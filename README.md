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

1. Execute the `hangman.py` file with Python. This will automatically start a new game of Hangman.
2. Follow the prompts to guess letters one at a time. The game will provide immediate feedback about each guess.
3. Keep guessing letters until you either guess the word correctly or run out of lives.

The game introduces a streamlined way to start and play through a session of Hangman with minimal setup.

## Progress and Learning

The game's development now encapsulates:
- The encapsulation of game logic within a `Hangman` class, providing a structured and object-oriented approach to game development.
- The introduction of a `play_game` function that initializes the game, starts the main game loop, and handles the win/loss conditions. This function simplifies starting a game and abstracts away the setup details.
- Enhanced feedback mechanisms to the user, including a summary of letters guessed so far and the remaining number of unique letters to guess.
- The use of docstrings in the `Hangman` class methods to provide clear documentation and aid understanding for other developers.

These additions and refinements to the project showcase the application of more advanced Python programming concepts, such as class-based organization, loop control, and basic game state management, all while continuing to provide an engaging user experience.

## License

This project is licensed under the [MIT License](LICENSE).
