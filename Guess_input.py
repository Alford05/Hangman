import tkinter as tk

class GuessInput:
    def __init__(self, parent, process_guess_callback):
        """
        Creates a guess input component
        
        Parameters:
        - parent: the tkinter container to place this widget in
        - process_guess_callback: function to call when a guess is submitted
        """
        self.parent = parent
        self.process_guess = process_guess_callback
        
        # Create a frame to hold the input elements
        self.frame = tk.Frame(parent)
        self.frame.pack(pady=10)
        
        # Create the entry widget
        self.guess_entry = tk.Entry(self.frame, width=2, font=('Arial', 14))
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        
        # Create submit button
        self.submit_button = tk.Button(self.frame, text="Guess", command=self.submit_guess)
        self.submit_button.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to submit
        self.guess_entry.bind("<Return>", lambda event: self.submit_guess())
        self.guess_entry.focus_set()
    
    def submit_guess(self):
        """Validate and process the guess"""
        letter = self.guess_entry.get().lower()
        if len(letter) == 1 and letter.isalpha():
            self.process_guess(letter)
            self.guess_entry.delete(0, tk.END)  # Clear entry
        self.guess_entry.focus()  # Keep focus on entry field
    
    def pack(self, **kwargs):
        """Pack the frame with any additional arguments"""
        self.frame.pack(**kwargs)

    def disable(self):
        """Disable the input field and button when the game is over"""
        self.guess_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.guess_entry.unbind("<Return>")

    def enable(self):
        """Re-enable the input field for a new game """
        self.guess_entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)
        self.guess_entry.bind("<Return>", lambda event: self.submit_guess())
        self.guess_entry.focus_set()


        