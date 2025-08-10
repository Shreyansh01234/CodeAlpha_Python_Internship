import random

# ----- Hangman Game -----
# Developed by: <Shreyansh pandey>
# Internship Project: CodeAlpha
# This is a simple console-based hangman game.

def show_intro():
    print("\n🎯 Welcome to My Hangman Challenge!")
    print("Guess the hidden word, one letter at a time.")
    print("You have only 6 wrong attempts. Let's start!\n")

def get_hidden_display(word, correct_letters):
    """Return the display of the word with guessed letters visible."""
    return " ".join([ch if ch in correct_letters else "_" for ch in word])

def play_hangman():
    # Word collection for the game
    word_list = ["python", "alpha", "project", "github", "code"]
    secret_word = random.choice(word_list)

    guessed_correct = set()
    guessed_wrong = set()
    max_attempts = 6

    show_intro()

    while len(guessed_wrong) < max_attempts:
        print("\nWord: ", get_hidden_display(secret_word, guessed_correct))
        print(f"❌ Wrong guesses: {len(guessed_wrong)}/{max_attempts}")
        guess = input("🔹 Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter only a single alphabet letter.")
            continue

        if guess in guessed_correct or guess in guessed_wrong:
            print("⚠ You already tried that letter.")
            continue

        if guess in secret_word:
            guessed_correct.add(guess)
            print("✅ Good guess!")
        else:
            guessed_wrong.add(guess)
            print("❌ Oops! That letter is not in the word.")

        if all(letter in guessed_correct for letter in secret_word):
            print("\n🎉 Congratulations! You guessed the word:", secret_word)
            break
    else:
        print("\n💀 Game Over! The word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
