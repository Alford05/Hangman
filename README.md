# Hangman (Tkinter GUI)

A simple graphical Hangman game built with Python and Tkinter. A solid improvement on the old CLI hangman design    
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

## File Overview

- `main.py`  
  - Sets up the `Window` and Tkinter UI
  - Chooses the random word
  - Handles game logic (`process_guess`, `reset_game`, `display_man`)

- `image.py`  
  - `Window`: wraps a Tk root and canvas, plus a simple game loop
  - `Point`: represents an (x, y) coordinate
  - `Line`: draws lines on the canvas
  - `Circle`: draws circles (used for the hangman head)

- `Guess_input.py`  
  - `GuessInput` class
  - Handles:
    - The text entry for guesses
    - The “Guess” button
    - Enabling/disabling input when the game ends

- `wordlist.py`  
  - Contains `words`, a list of possible secret words for the game.

## Requirements

- Python 3.x
- Tkinter (usually included with standard Python installs)

## How to Run

1. Make sure all the files (`main.py`, `image.py`, `Guess_input.py`, `wordlist.py`) are in the same directory.
2. Install Python 3 if you haven’t already.
3. Run:

   ```bash
   python3 main.py

   