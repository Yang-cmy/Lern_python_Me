#Number Guessing Game

import random
secret_number = random.randint(1, 100)

guess = int(input("Take a guess: "))

while guess != secret_number:
    