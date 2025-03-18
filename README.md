# Hangman Game

## Overview

This is a Python implementation of the classic word-guessing game, **Hangman**. The game challenges players to guess a hidden word by suggesting letters or entire words within a limited number of attempts. It includes difficulty levels (`easy`, `medium`, and `hard`) and hints for each word to enhance gameplay.

The project consists of two files:
1. **`hangman.py`**: Contains the main game logic.
2. **`words.py`**: Contains a list of words and their corresponding hints.

This README provides detailed instructions on how to play the game, its features, and how to set it up locally.

---

## Table of Contents

1. [Features](#features)
2. [How to Play](#how-to-play)
3. [Game Rules](#game-rules)
4. [Setup Instructions](#setup-instructions)
5. [Dependencies](#dependencies)
6. [File Structure](#file-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Difficulty Levels**: Choose between three difficulty levels:
  - **Easy**: Words with ≤ 5 letters.
  - **Medium**: Words with 6–8 letters.
  - **Hard**: Words with > 8 letters.
  
- **Hints**: Each word comes with a hint to help players guess the word.

- **Interactive Gameplay**:
  - Guess individual letters or the entire word.
  - Request hints during gameplay by typing `hint`.

- **Dynamic ASCII Art**: Displays the hangman's state based on remaining attempts.

- **Replayability**: Option to restart the game after finishing a round.

- **Error Handling**:
  - Prevents invalid inputs (e.g., numbers, empty strings).
  - Handles duplicate guesses gracefully.

---

## How to Play

1. **Start the Game**:
   - Run the `hangman.py` script.
   - Select a difficulty level (`easy`, `medium`, or `hard`).

2. **Guess the Word**:
   - The game displays a hidden word as underscores (`_ _ _ _`) and provides a hint.
   - Enter a letter or the full word to make a guess.

3. **Use Hints**:
   - Type `hint` during your turn to see the hint again.

4. **Win or Lose**:
   - You win by guessing all the letters or the full word correctly.
   - You lose if you exhaust all six attempts.

5. **Replay**:
   - After finishing a round, choose whether to play again or exit.

---

## Game Rules

- Players have **6 attempts** to guess the word.
- Each incorrect guess reduces the number of remaining attempts.
- Correctly guessed letters are revealed in the word.
- Duplicate guesses do not count against the player but will notify them.
- If the player guesses the word correctly before losing all attempts, they win.

---

## Setup Instructions

### Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```

2. **Install Dependencies**:
   - This project does not require any external libraries beyond Python's standard library.

3. **Run the Game**:
   - Execute the following command to start the game:
     ```bash
     python hangman.py
     ```

4. **Enjoy Playing**:
   - Follow the on-screen instructions to play the game.

---

## Dependencies

- **Python 3.x**: The game is written in Python and requires no additional libraries.

---

## File Structure

```
hangman-game/
├── hangman.py          # Main game logic
├── words.py            # List of words and hints
├── README.md           # Documentation (this file)
└── LICENSE             # License information
```

- **`hangman.py`**:
  - Contains the core game logic, including difficulty selection, word guessing, and ASCII art rendering.

- **`words.py`**:
  - A dictionary (`word_hints`) containing words and their associated hints. Used to dynamically select words based on difficulty.

---

## Contributing

We welcome contributions to improve the game! Here’s how you can contribute:

1. **Fork the Repository**:
   - Click the "Fork" button on GitHub to create a copy of the repository.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```

3. **Make Changes**:
   - Add new words and hints to `words.py`.
   - Improve the game logic or add new features to `hangman.py`.

4. **Test Your Changes**:
   - Run the game to ensure everything works as expected.

5. **Submit a Pull Request**:
   - Push your changes to your fork and open a pull request on the original repository.

---

## License

This project is licensed under the **APACHE 2.0 License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by the classic Hangman game.
- Thanks to contributors who helped expand the word list and improve gameplay.

---

## Contact

For questions, feedback, or suggestions, feel free to reach out:

- **GitHub Issues**: Open an issue in the repository.
- **Email**: [ashishofficial231@gmail.com]

---

Happy gaming! 🎮
