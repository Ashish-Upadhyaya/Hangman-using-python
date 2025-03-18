import random

# Import the word_hints dictionary from words.py
from words import word_hints

def get_word(difficulty="medium"):
    """
    Selects a random word based on difficulty level.
    :param difficulty: 'easy', 'medium', or 'hard'
    :return: A word from the word_hints dictionary
    """
    if difficulty == "easy":
        filtered_words = [word for word in word_hints.keys() if len(word) <= 5]
    elif difficulty == "hard":
        filtered_words = [word for word in word_hints.keys() if len(word) > 8]
    else:  # medium
        filtered_words = [word for word in word_hints.keys() if 5 < len(word) <= 8]

    if not filtered_words:
        raise ValueError("No words available for the selected difficulty.")
    
    return random.choice(filtered_words).upper()

def play(word):
    """
    Main gameplay loop for Hangman.
    :param word: The word to guess
    """
    hint = word_hints[word.lower()]  # Get the hint for the word
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(f"Here's a hint: {hint}")  # Display the hint
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word (type 'hint' to see the hint again): ").upper().strip()

        # Handle hint request
        if guess.lower() == "hint":
            print(f"Hint: {hint}")
            continue

        # Validate input
        if not guess:
            print("Input cannot be empty. Please try again.")
            continue
        if not guess.isalpha():
            print("Invalid input. Please enter a letter or word.")
            continue

        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word):  # Guessing the entire word
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess. Please enter a single letter, the full word, or type 'hint'.")

        # Display current state
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    # End of game
    if guessed:
        print("Congratulations! You guessed the word. You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

def display_hangman(tries):
    """
    Displays the hangman ASCII art based on remaining tries.
    :param tries: Number of tries left
    :return: Corresponding ASCII art
    """
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def main():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hangman!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower().strip()

    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower().strip()

    while True:
        word = get_word(difficulty)
        play(word)
        replay = input("Do you want to play again? (Y/N): ").upper().strip()
        if replay != "Y":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()