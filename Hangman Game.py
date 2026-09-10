import random

# 1. Predefined list of 5 words
word_list = ["python", "coding", "program", "laptop", "screen"]

# Select a random word from the list
secret_word = random.choice(word_list)

# 2. Track guessed letters and allowed incorrect attempts
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("--- Welcome to Hangman Game ---")

# 3. Main game loop
while incorrect_guesses < max_attempts:
    # Display the current word progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    
    # Check if the player has guessed the full word
    if "_" not in display_word:
        print("\nCongratulations! You won and guessed the word!")
        break

    # Get player input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    # Add the guess to our tracker
    guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess.")
        incorrect_guesses += 1

# Game over condition if player runs out of turns
if incorrect_guesses == max_attempts:
    print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")
