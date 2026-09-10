import random

# Predefined list of 5 words
word_list = ["python", "coding", "program", "laptop", "screen"]

# Pick a random word from the list
secret_word = random.choice(word_list)

# Track guessed letters and allowed incorrect attempts
guessed_letters = set()
incorrect_guesses = 0
max_attempts = 6

print("--- Welcome to Hangman Game ---")

# Main game loop
while incorrect_guesses < max_attempts:
    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"\nWord: {display_word.strip()}")
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    
    # Check if the player has revealed the whole word
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        break
        
    # Get player input
    guess = input("Guess a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
        
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue
        
    # Add the guess to tracked letters
    guessed_letters.add(guess)
    
    # Check if the guess is in the secret word
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses += 1

# Game over condition if they run out of attempts
if incorrect_guesses == max_attempts:
    print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")
