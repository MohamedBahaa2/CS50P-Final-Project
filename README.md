# CS50P-Final-Project
## CLI Hangman Game

#### Video Demo: (https://www.youtube.com/watch?v=g2wxbzvFL-A)

#### Description:
This project is a non-graphical command-line-based Hangman game with integrated features such as a word database and a scoring system. The game allows users to guess letters of a randomly selected word within a limited number of attempts, just like the traditional Hangman game. Key features of the game include:

- **Word Database**: A built-in word list from which the game randomly selects a word each round.
- **Score System**: Players earn points for correctly guessing words, and their scores are recorded for each game session.
- **Command-Line Interface**: The game is played entirely through the command line, providing an interactive experience for users without a graphical interface.
- **Feedback Mechanism**: After each guess, the player is informed whether their guess was correct or incorrect, and the state of the word is displayed.
- **Game Over Conditions**: The game ends either when the player successfully guesses the word or uses up all their attempts, resulting in a "game over."

#### How to Play:
1. The player starts the game and is presented with a series of underscores representing the letters of a randomly chosen word.
2. The player guesses a letter by typing it into the terminal.
3. For each correct guess, the letter is revealed in its correct position(s) in the word. For incorrect guesses, the player loses one attempt.
4. The game continues until the player either correctly guesses the word or runs out of attempts.
5. The player's score is calculated based on their performance, and the game may offer the option to play again.
