from image import Window, Point, Line, Circle
from Guess_input import GuessInput
from wordlist import words
import tkinter as tk
import sys
import random

def main():
    screen_x = 1000
    screen_y = 1000

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    def draw_line(canvas, x1, y1, x2, y2, color="black"):
        line = Line(Point(x1, y1), Point(x2, y2))
        canvas.draw_line(line, color)

    # Draw the hangman scaffold
    draw_line(win, 100, 950, 950, 950, color="red")
    draw_line(win, 100, 930, 950, 930, color="red")
    draw_line(win, 200, 930, 200, 100, color="red")
    draw_line(win, 250, 930, 250, 100, color="red")
    draw_line(win, 200, 100, 550, 100, color="red")
    draw_line(win, 450, 100, 450, 190, color="red") 

    #Access the tkinter root and canvas
    canvas = win.get_canvas()
    root = canvas.master

    answer = random.choice(words)

    #variables to be used later as code develops
    guessed_letters = set()
    hint = ["_"] * len(answer)
    wrong_guesses = 0


    #Drawing the image for wrong letter guesses
    def display_man(wrong_guesses):
        if wrong_guesses == 1:
            canvas = win.get_canvas()
            my_circle = Circle(center_x=450, center_y=265, radius=75)
            my_circle.draw(canvas=canvas, fill_color="white")
        elif wrong_guesses == 2:
            draw_line(win, 450, 340, 450, 590, color="black")
        elif wrong_guesses == 3:
            draw_line(win, 450, 590, 350, 790, color="black")
        elif wrong_guesses == 4:    
            draw_line(win, 450, 590, 550, 790, color="black")
        elif wrong_guesses == 5:    
            draw_line(win, 450, 430, 300, 300, color="black")
        elif wrong_guesses == 6:
            draw_line(win, 450, 430, 600, 300, color="black")

                                                                      

    #Define how to process a guess
    def process_guess(letter):
        nonlocal wrong_guesses, guessed_letters, hint
        nonlocal reset_button
        if letter in guessed_letters:
            message_label.config(text=f"You already guessed '{letter}'!", fg="orange")
            return
        
        guessed_letters.add(letter)

        if letter in answer:
            message_label.config(text=f"Good guess! '{letter}' is in the word.", fg="green")
            for i in range(len(answer)):
                if answer[i] == letter:
                    hint[i] = letter
            hint_label.config(text=" ".join(hint))
        else:
            message_label.config(text=f"Sorry, '{letter}' is not in the word.", fg="red")
            wrong_guesses += 1
            display_man(wrong_guesses)

        if "_" not in hint:
            guess_input.guess_entry.delete(0, tk.END) 
            message_label.config(text="YOU WIN!! Congratulations!", fg="green", font=("Arial", 20, "bold"))
            guess_input.disable()
            reset_button = tk.Button(root, text="New Game", font=("Arial", 18), command=lambda: reset_game())
            reset_button.pack(pady=10)
        elif wrong_guesses >= 6:
            guess_input.guess_entry.delete(0, tk.END) 
            message_label.config(text=f"YOU LOSE! The word is '{answer}'", fg="red", font=("Arial", 20, "bold"))
            guess_input.disable()
            reset_button = tk.Button(root, text="New Game", font=("Arial", 18), command=lambda: reset_game())
            reset_button.pack(pady=10)
    

    #Wimdow Inserts
    input_frame = tk.Frame(root)
    input_frame.pack(pady=20)

    hint_label = tk.Label(input_frame, text=" ".join(hint), font=("Arial", 24))
    hint_label.pack(side=tk.LEFT, padx=(0, 20))
    
    label = tk.Label(input_frame, text="Enter your guess:", font=("Arial", 14))
    label.pack(side=tk.LEFT)

    message_label = tk.Label(root, text="", font=("Arial", 16))
    message_label.pack(pady=10)
                                                  
    guess_input = GuessInput(input_frame, process_guess)
    guess_input.pack(side=tk.LEFT, padx=(10, 0))  

    reset_button = None

    # Create a reset button
    def reset_game():
        nonlocal reset_button
        reset_button.destroy()
        nonlocal wrong_guesses, guessed_letters, hint
        guessed_letters = set()
        wrong_guesses = 0
        nonlocal answer 
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        hint_label.config(text=" ".join(hint))
        message_label.config(text="")
        guess_input.enable()
        canvas.delete("all")
        draw_line(win, 100, 950, 950, 950, color="red")
        draw_line(win, 100, 930, 950, 930, color="red")
        draw_line(win, 200, 930, 200, 100, color="red")
        draw_line(win, 250, 930, 250, 100, color="red")
        draw_line(win, 200, 100, 550, 100, color="red")
        draw_line(win, 450, 100, 450, 190, color="red")


    win.wait_for_close()


main()

