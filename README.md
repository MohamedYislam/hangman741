

# Hangman

Hangman is a classic game where one player thinks of a word, and the other player tries to guess it within a certain number of attempts. This implementation allows you to play against the computer, which randomly selects a word for you to guess.

## Description

This project is a Python-based implementation of the classic Hangman game. The computer randomly chooses a word from a predefined list, and the user attempts to guess it, one letter at a time. The aim of the project is to provide a fun and interactive way to engage with the traditional game of Hangman while practicing and demonstrating basic Python programming concepts.

## Requirements

- Python 3.x

Ensure Python 3 is installed on your system to run this game. You can download it from [python.org](https://www.python.org/downloads/).

## Setting Up

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/MohamedYislam/hangman741.git
   ```

2. After cloning, navigate to the project directory:

   ```
   cd hangman741
   ```

3. To start playing the game, run:

   ```
   python3 hangman.py
   ```

## Usage

To start the game:

1. Execute the `hangman.py` file with Python. This action will automatically start a new game of Hangman.
2. Follow the prompts to guess letters one at a time. The game will provide immediate feedback about each guess.
3. Continue guessing letters until you either correctly guess the word or run out of lives.

This game introduces a streamlined method to begin and progress through a session of Hangman with minimal setup.

## Progress and Learning

The development of the game now encompasses:
- Encapsulation of game logic within a `Hangman` class, offering a structured and object-oriented approach to game development.
- Introduction of a `play_game` function that initializes the game, commences the main game loop, and manages the win/loss conditions. This function simplifies the game's start process and abstracts the setup details.
- Enhanced feedback mechanisms for the user, including a summary of letters guessed and the remaining number of unique letters to guess.
- Use of docstrings in the `Hangman` class methods to provide clear documentation and assist understanding for other developers.

These improvements and refinements to the project showcase the application of advanced Python programming concepts, such as class-based organization, loop control, and basic game state management, all while maintaining an engaging user experience.

## License

This project is licensed under the [MIT License](LICENSE).


