import random

# 1. Predefined list of 5 words
words = ["python", "programming", "developer", "computer", "hangman"]

# Select a random word from the list
secret_word = random.choice(words)

# Initialize game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")

# Main game loop
while incorrect_guesses < max_attempts:
    # Display the current progress of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    
    # Check if the player has guessed all letters
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        break

    # Get player input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the guess to our history
    guessed_letters.append(guess)

    # Process the guess
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Incorrect guess!")
        incorrect_guesses += 1

# If the player runs out of attempts
if incorrect_guesses == max_attempts:
    print(f"\nGame Over! The word was: {secret_word}")
