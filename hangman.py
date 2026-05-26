import tkinter as tk
from tkinter import messagebox
import random

WORDS = [
    "python", "hangman", "keyboard", "monitor", "algorithm",
    "variable", "function", "recursion", "database", "network",
    "compiler", "terminal", "frontend", "backend", "developer",
    "elephant", "giraffe", "dolphin", "volcano", "gravity",
    "universe", "biology", "chemistry", "philosophy", "economics"
]

MAX_WRONG = 6


def draw_hangman(canvas, wrong):
    canvas.delete("all")

    # Gallows
    canvas.create_line(20, 230, 180, 230, width=3, fill="#e0e0e0")   # base
    canvas.create_line(60, 230, 60, 20,  width=3, fill="#e0e0e0")    # pole
    canvas.create_line(60, 20, 140, 20,  width=3, fill="#e0e0e0")    # top
    canvas.create_line(140, 20, 140, 50, width=3, fill="#e0e0e0")    # rope

    if wrong >= 1:  # head
        canvas.create_oval(120, 50, 160, 90, width=3, outline="#ef5350")

    if wrong >= 2:  # body
        canvas.create_line(140, 90, 140, 160, width=3, fill="#ef5350")

    if wrong >= 3:  # left arm
        canvas.create_line(140, 110, 110, 140, width=3, fill="#ef5350")

    if wrong >= 4:  # right arm
        canvas.create_line(140, 110, 170, 140, width=3, fill="#ef5350")

    if wrong >= 5:  # left leg
        canvas.create_line(140, 160, 110, 195, width=3, fill="#ef5350")

    if wrong >= 6:  # right leg
        canvas.create_line(140, 160, 170, 195, width=3, fill="#ef5350")


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.word = ""
        self.guessed = set()
        self.wrong_count = 0

        self._build_ui()
        self.new_game()

    def _build_ui(self):
        # Title
        tk.Label(
            self.root, text="HANGMAN", bg="#1a1a2e", fg="#e0e0e0",
            font=("Courier", 22, "bold"), pady=10
        ).grid(row=0, column=0, columnspan=2)

        # Canvas for drawing
        self.canvas = tk.Canvas(
            self.root, width=200, height=240,
            bg="#16213e", highlightthickness=0
        )
        self.canvas.grid(row=1, column=0, padx=20, pady=10)

        # Right side frame
        right = tk.Frame(self.root, bg="#1a1a2e")
        right.grid(row=1, column=1, padx=20, pady=10, sticky="n")

        # Wrong guesses counter
        self.wrong_label = tk.Label(
            right, text="", bg="#1a1a2e", fg="#ef5350",
            font=("Courier", 13, "bold")
        )
        self.wrong_label.pack(pady=(0, 10))

        # Word display
        self.word_label = tk.Label(
            right, text="", bg="#1a1a2e", fg="#80cbc4",
            font=("Courier", 20, "bold")
        )
        self.word_label.pack(pady=10)

        # Wrong letters
        tk.Label(
            right, text="Wrong guesses:", bg="#1a1a2e",
            fg="#888", font=("Courier", 10)
        ).pack()
        self.wrong_letters_label = tk.Label(
            right, text="", bg="#1a1a2e", fg="#ef9a9a",
            font=("Courier", 12)
        )
        self.wrong_letters_label.pack(pady=(0, 10))

        # Keyboard buttons
        self.btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.letter_buttons = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        rows = ["abcdefghi", "jklmnopqr", "stuvwxyz"]

        for r, row_letters in enumerate(rows):
            row_frame = tk.Frame(self.btn_frame, bg="#1a1a2e")
            row_frame.pack()
            for ch in row_letters:
                btn = tk.Button(
                    row_frame, text=ch.upper(), width=3, height=1,
                    font=("Courier", 10, "bold"),
                    bg="#16213e", fg="#e0e0e0",
                    activebackground="#0f3460", activeforeground="#80cbc4",
                    relief="flat", bd=0, cursor="hand2",
                    command=lambda c=ch: self.guess(c)
                )
                btn.pack(side="left", padx=2, pady=2)
                self.letter_buttons[ch] = btn

        # New game button
        tk.Button(
            self.root, text="New Game", font=("Courier", 11, "bold"),
            bg="#0f3460", fg="#80cbc4", activebackground="#16213e",
            relief="flat", padx=20, pady=6, cursor="hand2",
            command=self.new_game
        ).grid(row=3, column=0, columnspan=2, pady=15)

    def new_game(self):
        self.word = random.choice(WORDS)
        self.guessed = set()
        self.wrong_count = 0

        draw_hangman(self.canvas, 0)
        self._refresh_display()

        for btn in self.letter_buttons.values():
            btn.config(state="normal", bg="#16213e", fg="#e0e0e0")

    def guess(self, letter):
        if letter in self.guessed:
            return

        self.guessed.add(letter)
        btn = self.letter_buttons[letter]

        if letter in self.word:
            btn.config(bg="#1b5e20", fg="#a5d6a7", state="disabled")
        else:
            self.wrong_count += 1
            btn.config(bg="#b71c1c", fg="#ef9a9a", state="disabled")
            draw_hangman(self.canvas, self.wrong_count)

        self._refresh_display()
        self._check_game_over()

    def _refresh_display(self):
        # Word with blanks
        display = "  ".join(
            ch if ch in self.guessed else "_" for ch in self.word
        )
        self.word_label.config(text=display)

        # Wrong count
        self.wrong_label.config(
            text=f"Lives: {MAX_WRONG - self.wrong_count} / {MAX_WRONG}"
        )

        # Wrong letters list
        wrong_letters = sorted(
            ch for ch in self.guessed if ch not in self.word
        )
        self.wrong_letters_label.config(
            text="  ".join(ch.upper() for ch in wrong_letters) if wrong_letters else ""
        )

    def _check_game_over(self):
        # Win
        if all(ch in self.guessed for ch in self.word):
            messagebox.showinfo(
                "You won!",
                f"Nice! The word was '{self.word.upper()}' 🎉"
            )
            self.new_game()
            return

        # Lose
        if self.wrong_count >= MAX_WRONG:
            # Reveal the word
            self.word_label.config(
                text="  ".join(self.word.upper()),
                fg="#ef5350"
            )
            messagebox.showinfo(
                "Game Over",
                f"The word was '{self.word.upper()}'. Better luck next time!"
            )
            self.new_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
