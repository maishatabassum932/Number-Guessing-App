import tkinter as tk
from tkinter import messagebox
from random import randint

# --- Modern Pastel Theme ---
BG_COLOR = "#f6f5f7"         # Soft off-white
HEADER_COLOR = "#7f5af0"     # Pastel purple
BTN_COLOR = "#2cb67d"        # Pastel green
BTN_HOVER = "#7f5af0"        # Pastel purple for hover
TEXT_COLOR = "#16161a"       # Dark text
ENTRY_BG = "#fffffe"         # White entry
ENTRY_FG = "#16161a"
PLACEHOLDER_COLOR = "#a7a9be"
RESULT_CORRECT = "#2cb67d"
RESULT_WRONG = "#f25f4c"
RESULT_HINT = "#7f5af0"
FONT_HEADER = ("Poppins", 22, "bold")
FONT_LABEL = ("Poppins", 13)
FONT_BTN = ("Poppins", 12, "bold")

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Number Guessing Game ✨")
        self.root.geometry("440x480")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.number = randint(1, 100)
        self.attempts = 0

        # Decorative Top Bar
        self.top_bar = tk.Frame(root, bg=HEADER_COLOR, height=8)
        self.top_bar.pack(fill="x", side="top")

        # Header
        self.header = tk.Label(
            root, text="Guess the Number!", bg=BG_COLOR, fg=HEADER_COLOR, font=FONT_HEADER, pady=18
        )
        self.header.pack(pady=(30, 10))

        # Instructions
        self.instructions = tk.Label(
            root,
            text="I'm thinking of a number between 1 and 100.\nCan you guess it?",
            bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_LABEL
        )
        self.instructions.pack(pady=(0, 18))

        # Entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            root, font=FONT_LABEL, justify="center", bg=ENTRY_BG, fg=PLACEHOLDER_COLOR,
            insertbackground=ENTRY_FG, textvariable=self.entry_var, relief="flat", bd=2, highlightthickness=2, highlightbackground=HEADER_COLOR
        )
        self.entry.pack(ipady=8, ipadx=5, pady=(0, 8))
        self.entry.insert(0, "Enter your guess")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        # Guess Button
        self.guess_btn = tk.Button(
            root, text="Guess!", bg=BTN_COLOR, fg="white", font=FONT_BTN,
            activebackground=BTN_HOVER, activeforeground="white", command=self.check_guess, cursor="hand2",
            relief="flat", bd=0, padx=18, pady=6
        )
        self.guess_btn.pack(pady=(10, 0))
        self.guess_btn.bind("<Enter>", lambda e: self.guess_btn.config(bg=BTN_HOVER))
        self.guess_btn.bind("<Leave>", lambda e: self.guess_btn.config(bg=BTN_COLOR))

        # Result Label
        self.result = tk.Label(
            root, text="", bg=BG_COLOR, fg=HEADER_COLOR, font=FONT_LABEL
        )
        self.result.pack(pady=(24, 0))

        # Reset Button
        self.reset_btn = tk.Button(
            root, text="Restart Game", bg="#f25f4c", fg="white", font=FONT_BTN,
            activebackground="#ffb4a2", activeforeground="white", command=self.reset_game, cursor="hand2",
            relief="flat", bd=0, padx=12, pady=4
        )
        self.reset_btn.pack(pady=(30, 0))
        self.reset_btn.bind("<Enter>", lambda e: self.reset_btn.config(bg="#ffb4a2"))
        self.reset_btn.bind("<Leave>", lambda e: self.reset_btn.config(bg="#f25f4c"))

        # Decorative Emoji
        self.bg_emoji = tk.Label(
            root, text="🌈", font=("Segoe UI Emoji", 100), fg="#e4e4e4", bg=BG_COLOR
        )
        self.bg_emoji.place(relx=0.5, rely=0.82, anchor="center")

        self.input_active = True

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter your guess":
            self.entry.delete(0, tk.END)
            self.entry.config(fg=ENTRY_FG)

    def add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Enter your guess")
            self.entry.config(fg=PLACEHOLDER_COLOR)

    def check_guess(self):
        if not self.input_active:
            return
        guess = self.entry.get()
        if guess == "Enter your guess" or not guess.strip():
            self.result.config(text="Please enter a number!", fg=RESULT_WRONG)
            self.entry.delete(0, tk.END)
            return
        if not guess.isdigit():
            self.result.config(text="Numbers only, please!", fg=RESULT_WRONG)
            self.entry.delete(0, tk.END)
            return
        guess = int(guess)
        if not (1 <= guess <= 100):
            self.result.config(text="Guess must be between 1 and 100!", fg=RESULT_WRONG)
            self.entry.delete(0, tk.END)
            return
        self.attempts += 1
        if guess == self.number:
            self.result.config(
                text=f"🎉 Correct! You guessed it in {self.attempts} tries.", fg=RESULT_CORRECT
            )
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed the number {self.number} in {self.attempts} attempts!",
            )
            self.input_active = False
            self.entry.config(state="disabled")
            self.guess_btn.config(state="disabled")
        elif guess < self.number:
            self.result.config(text="🔻 Too low! Try again.", fg=RESULT_HINT)
            self.entry.delete(0, tk.END)
        else:
            self.result.config(text="🔺 Too high! Try again.", fg=RESULT_HINT)
            self.entry.delete(0, tk.END)

    def reset_game(self):
        self.number = randint(1, 100)
        self.attempts = 0
        self.entry.config(state="normal")
        self.guess_btn.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Enter your guess")
        self.entry.config(fg=PLACEHOLDER_COLOR)
        self.result.config(text="")
        self.input_active = True
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()