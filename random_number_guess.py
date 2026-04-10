import random

rnd_number = random.randint(1, 100)  # Computer picks a number
nmb_guessed = 0
attempts = 0
print(rnd_number) #For testing reasons
print("I'm thinking of a number between 1 and 100...can you guess it? ")
while nmb_guessed == 0:
    user_guess = int(input("Enter your guess: "))
    try:
        if user_guess == rnd_number:
            attempts += 1
            print(f"Congratulations, you did it! The number was {rnd_number}. Number of attempts: {attempts}.")
            nmb_guessed += 1
        elif (user_guess < 1) or (user_guess > 100):
            print("Guess was out of range. Try guessing a number from 1 to 100.")
        elif user_guess < rnd_number:
            attempts += 1
            print("Guess was too low. Guess higher.")
        else:
            attempts += 1
            print("Guess was too high. Guess lower.")
    except ValueError:
        print("Wrong Input Detected! Try guessing a number: ")