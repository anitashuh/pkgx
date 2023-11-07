import random

# List of words to guess
words = ["python", "codespaces", "github", "programming", "challenge", "coding"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")

    while attempts > 0:
        display = display_word(word_to_guess, guessed_letters)
        print("\nWord to guess: " + display)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Input should be a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter before.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if word_to_guess == display_word(word_to_guess, guessed_letters):
                print("\nCongratulations! You've successfully guessed the word:", word_to_guess)
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("The letter is not in the word. Remaining attempts:", attempts)

    if attempts == 0:
        print("\nYou've run out of attempts. The correct word was:", word_to_guess)

if __name__ == "__main__":
    play_game()
