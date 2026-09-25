import random


WORDS = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]

MAX_WRONG_GUESSES = 12


def welcome():
    print("Welcome to the word guessing game!")
    name = input("Tell me your name: ").strip() or "Player"
    print(f"Good luck, {name}!")


def display_word(word, guesses):
    return " ".join(char if char in guesses else "_" for char in word)


def get_guess(guesses):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
        elif guess in guesses:
            print("You already guessed that letter.")
        else:
            return guess


def play_game():
    word = random.choice(WORDS)
    guesses = set()
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"\nWord: {display_word(word, guesses)}")
        print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = get_guess(guesses)
        guesses.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(char in guesses for char in word):
            print(f"\nYou win! The word was '{word}'.")
            return

    print(f"\nYou lose! The word was '{word}'.")


def main():
    welcome()

    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
