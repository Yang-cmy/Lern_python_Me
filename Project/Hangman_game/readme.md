# Hangman Game in Python

Hangman is a classic word-guessing game. Its origins are not exactly known but it appears to date back to Victorian times. A player writes down the first and last letters of a word and another player guesses the letters in between.

- Program randomly selects a word from a list of secret words.
- Player has limited chances to guess the word.
- When a correct letter is guessed, it is revealed in its correct position.
- Player wins if all letters are guessed before running out of chances.

## Steps to Build the Game

1. Create a list of words and randomly select one.
2. Display blanks (_) for each letter in the word.
3. Take a letter as input from the user.
4. Check whether the letter exists in the word.
5. Reveal correct letters and track wrong guesses.
6. Display the Hangman drawing after each incorrect guess.
7. End the game when the word is guessed or all chances are used.