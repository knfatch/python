#Hangman Game---------------------------------------------------
import random

#Hangman Word Attributes ---------------------------------------
rnd_number = random.randint(0, 3)
words = ['python', 'java', 'kotlin', 'javascript']
hangman_word = words[rnd_number]

#Game State Code -----------------------------------------------
hangman_word_check = list(hangman_word)
blank_counter = len(hangman_word)
word_blanks = []
while blank_counter > 0:
    word_blanks.append("_")
    blank_counter -= 1
word_length = len(hangman_word)
guessed_letters = []
game_end = 0

#Game Processing Code ------------------------------------------
hangman_count = len(hangman_word)
attempts = 6
print(f"The word has {word_length} characters. Can you guess it before running out of attempts? Attempts: {attempts}.")
print("*************************************")
while (attempts >= 1) and (hangman_count >= 1):
    print(f'Word: {word_blanks}')
    player_guess = input("Guess a letter: ")
    if player_guess.isalpha():
        letter_check = guessed_letters.count(player_guess)
        guessed_letters.append(player_guess)
        if letter_check == 0:
            guess_check = hangman_word.count(player_guess)
            if guess_check == 0:
                print("The guess is incorrect!")
                attempts -= 1
                print(f"You have {attempts} guess remainging.")
            else:
                print(f"{player_guess} is in the word. It appears {guess_check} times.")
                hangman_count -= guess_check
                while guess_check > 0:
                    letter_index = hangman_word_check.index(player_guess)
                    word_blanks.insert(letter_index, player_guess)
                    del word_blanks[letter_index + 1]
                    if guess_check > 1:
                        hangman_word_check.insert(letter_index, 0)
                        del hangman_word_check[letter_index + 1]
                    guess_check -= 1
        else:
            print("You have already guess that letter. Please guess a different letter.")
    else:
        print("Invalid input. Please enter a letter.")

#Endgame Results Output -------------------------------------------
if attempts == 0:
    print(f"Sorry, you ran out of attempts. The word was {hangman_word}.")
else:
    print(f"Congratulations! The word was {hangman_word}. You guessed it!")