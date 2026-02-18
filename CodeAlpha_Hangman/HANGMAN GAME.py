import random

words = ["python", "apple", "chair", "tiger", "plant"]

secret_word = random.choice(words)

guessed_letters = []

display_word = ["_"] * len(secret_word)

incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! Attempts left: {max_incorrect - incorrect_guesses}\n")

if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("❌ Game Over! The word was:", secret_word)
 