# Hangman (Tkinter GUI)

A simple graphical Hangman game built with Python and Tkinter.  
The player guesses letters to reveal a hidden word while a hangman is drawn for each wrong guess.

## Features

- Graphical window using `tkinter`
- Custom `Window`, `Point`, `Line`, and `Circle` classes for drawing
- Text input for single-letter guesses
- Visual hangman scaffold and body parts drawn as the player makes mistakes
- Win and lose detection with a “New Game” button to play again

## How It Works

- A random word is chosen from `wordlist.py` (`words` list).
- The current progress is shown as underscores (`_ _ _`) for each letter.
- The player types a single letter and clicks **Guess** (or presses Enter).
- Correct guesses reveal letters; incorrect guesses:
  - Increase the `wrong_guesses` counter
  - Draw the next part of the hangman:
    1. Head (circle)
    2. Body
    3. Left leg
    4. Right leg
    5. Left arm
    6. Right arm
- The game ends when:
  - All letters are guessed (win), or
  - `wrong_guesses` reaches 6 (lose).
- After the game ends, a **New Game** button appears and resets:
  - The chosen word
  - The hint display
  - The hangman drawing
  - The input field

## Project Structure

The project directory is named `Hangman` and contains:

- `main.py`  
  Entry point. Sets up the `Window` and Tkinter UI, chooses the random word, and handles core game logic (`process_guess`, `reset_game`, `display_man`).

- `image.py`  
  Drawing and window abstractions:
  - `Window`: wraps a Tk root and canvas, plus a simple game loop
  - `Point`: represents an (x, y) coordinate
  - `Line`: draws lines on the canvas
  - `Circle`: draws circles (used for the hangman head)

- `Guess_input.py`  
  Input widget for guesses:
  - `GuessInput` class: manages the guess entry box, “Guess” button, Enter-key binding, and enabling/disabling input.

- `wordlist.py`  
  Contains `words`, a list of possible secret words for the game.

- `README.md`  
  This documentation file.

- `__pycache__/`  
  Automatically generated Python bytecode cache (can be ignored).

## Requirements

- Python 3.x
- Tkinter (usually included with standard Python installs)

## How to Run

1. Open a terminal in the `Hangman` directory (the one containing `main.py`).
2. Make sure Python 3 is installed.
3. Run:

   ```bash
   python3 main.py
4. A window titled "Hangman" will open and you can start guessing letters.


## Possible Improvements

- Display a list of letters that have already been guessed.
- Add more visual feedback (e.g., colors or animations).
- Add difficulty levels with different word lists.
- Limit the allowed characters more clearly and show error messages for invalid input.
- Track and display a score across multiple games.
