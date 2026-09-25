import random

words = ["apple", "banana", "mango", "orange", "grapes", "papaya"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hnagman game")
name = input("Your name:")
name.strip()

if name == '':
    name = 'player'

print(name)

while wrong_guesses < max_attempts:
    display = ''

    for letter in word:
        if letter in guessed:
            display += letter + ''
        else:
            display += "_"

    print(hangman[wrong_guesses])
    print("word", display)

    if '_' not in display:
        print('YOU WON :D')
        print(f'The correct word was {word}')
        break

    guess = input("Your Guess:").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print('please enter one char')
        continue

    if guess in guessed:
        print("you already guessed that letter")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct Guess")
    else:
        wrong_guesses += 1
        print("Incorrect Guess")

else:
    print(hangman[-1])
    print("Game Over!")
    print("The fruit was:", word)

