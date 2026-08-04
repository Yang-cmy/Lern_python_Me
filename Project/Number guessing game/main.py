import random
secret_number = random.randint(1, 100)
user_choice = None
attempt = 0

print("welcome to the Number Guessing game")
print("I'm thinking of a number between 1 and 100.")

while user_choice != secret_number:

    try:
        user_choice = int(input("Take a guess: "))
        attempt += 1

        if user_choice > secret_number:
            print("Too High")
        elif user_choice < secret_number:
            print("Too Low")

    except ValueError:
            print("Please enter a valid number!")


print(f"Congreate You Guesssed the number {secret_number} in {attempt} attempt")

#this is a pass maybe?
#in the end try and except is use just like this huh, Dont really understande but i kinda get the point maybe?
#indentation in python is very important try and except should not be under if elif else block or it will cause the error