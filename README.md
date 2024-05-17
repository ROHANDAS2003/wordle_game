**Wordle Game Documentation**
## Abbreviations
1. **cls**: Command to clear the screen in the command-line interface (CLI). Used in the play\_wordle.py script to clear the screen before displaying the game menu.
1. **txt**: File extension for text files. Used in wordle\_words.txt, which contains a list of words for the game.
1. **str**: Abbreviation for "string". Used in the LetterState and Wordle classes to denote string data types.
1. **bool**: Abbreviation for "boolean". Used in the LetterState class to denote boolean data types.
1. **repr**: Abbreviation for "representation". Used in the LetterState class for the \_\_repr\_\_ method, which returns a string representation of the object.
1. **JSON**: Abbreviation for "JavaScript Object Notation". Not used directly in the documentation, but json is a common abbreviation for JSON data format.
## Introduction 
The Wordle Game is a word-guessing game where players attempt to guess a secret word within a limited number of attempts. It's a popular word puzzle game that challenges players to use logic and deduction to uncover the hidden word.
## Features
- Random selection of secret words from a predefined word list.
- Feedback on each guess, highlighting correct letters and their positions.
- Limited number of attempts per game.
- Instructions and gameplay menu options for user interaction.
- Option to replay the game after completion or exit.
## Files and Components
The Wordle Game consists of the following files and components:

- **play\_wordle.py**: The main script for running the Wordle game. It contains the menu system, gameplay loop, and interaction with the player.
- **wordle.py**: Module containing the Wordle class, representing the core game logic, including managing attempts, evaluating guesses, and determining game state.
- **letter\_state.py**: Module containing the LetterState class, representing the state of a single letter in the game (whether it is in the word and whether it is in the correct position).
- **data/wordle\_words.txt**: A text file containing a list of words that can be used as secret words in the game.
## Cloning the Repository
To clone the Wordle Game project from GitHub, follow these steps:

1. Open your terminal (Command Prompt, PowerShell, or any other terminal emulator).
1. Navigate to the directory where you want to clone the repository.
1. Run the following command: git clone wordle\_game
1. Navigate into the cloned repository directory: cd wordle\_game
## Dependencies
The Wordle Game depends on the following:

- colorama: A Python package used for colored text output in the command line interface.
- random: Python's built-in module for generating random numbers and choices.
- os: Python's built-in module for interacting with the operating system.

Install the dependencies using pip: pip install -r requirements.txt
## Running the Program
To run the Wordle Game program, follow these steps:

1. Ensure you are in the root directory of the cloned repository.
1. Run the play\_wordle.py script using Python: python play\_wordle.py
1. Follow the on-screen instructions to play the game.
## How to Play
To play the Wordle Game:

- Run the play\_wordle.py script.
- Choose an option from the menu:
  - Option 0: Learn how to play the game.
  - Option 1: Start playing the game.
  - Option 2: Exit the game.
- If you choose to play:
  - You'll have a limited number of attempts to guess the secret word.
  - Enter your guess when prompted.
  - The game will provide feedback on your guess, indicating the correct letters and their positions.
- After each attempt, the game will display the results so far, including your remaining attempts.
- If you correctly guess the word within the allotted attempts, you win the game.
- You have the option to play again or exit the game after completing or failing to complete the current game.
## Development
The Wordle Game is developed using Python and follows object-oriented programming principles.
## Future Improvements
Potential improvements for the Wordle Game include:

- Adding more words to the word list for greater variety.
- Implementing different difficulty levels with varying word lengths or number of attempts.
- Adding a scoring system to track and display the player's performance.
## Conclusion
The Wordle Game provides an entertaining and challenging word-guessing experience suitable for players of all ages. Its simple gameplay mechanics and interactive features make it a delightful pastime for word puzzle enthusiasts.

