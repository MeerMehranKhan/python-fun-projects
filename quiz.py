import tkinter as tk
from tkinter import messagebox
import random

TIMER_SECONDS = 30

QUESTIONS = [
    # General Knowledge
    {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"], "answer": "Da Vinci"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "Which country has the largest population?", "options": ["USA", "India", "China", "Russia"], "answer": "India"},
    {"question": "What is the chemical symbol for gold?", "options": ["Go", "Gd", "Au", "Ag"], "answer": "Au"},
    {"question": "How many days are in a leap year?", "options": ["364", "365", "366", "367"], "answer": "366"},
    {"question": "Which is the longest river in the world?", "options": ["Amazon", "Yangtze", "Mississippi", "Nile"], "answer": "Nile"},
    {"question": "What is the smallest country in the world?", "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "answer": "Vatican City"},
    {"question": "Which language has the most native speakers?", "options": ["English", "Spanish", "Mandarin", "Hindi"], "answer": "Mandarin"},
    {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "answer": "Canberra"},
    {"question": "How many strings does a standard guitar have?", "options": ["4", "5", "6", "7"], "answer": "6"},
    {"question": "Which metal is liquid at room temperature?", "options": ["Lead", "Mercury", "Gallium", "Cesium"], "answer": "Mercury"},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "answer": "Mount Everest"},
    {"question": "Which organ produces insulin?", "options": ["Liver", "Kidney", "Pancreas", "Spleen"], "answer": "Pancreas"},
    {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
    {"question": "What is the capital of Brazil?", "options": ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"], "answer": "Brasilia"},
    {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": "Mercury"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": "Diamond"},

    # Science
    {"question": "What is the speed of light (approx)?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "100,000 km/s"], "answer": "300,000 km/s"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi Body"], "answer": "Mitochondria"},
    {"question": "How many bones are in the adult human body?", "options": ["196", "206", "216", "226"], "answer": "206"},
    {"question": "What is the atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": "6"},
    {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": "Saturn"},
    {"question": "What is the chemical formula for water?", "options": ["HO", "H2O", "H3O", "OH2"], "answer": "H2O"},
    {"question": "What force keeps planets in orbit around the Sun?", "options": ["Magnetism", "Friction", "Gravity", "Tension"], "answer": "Gravity"},
    {"question": "What is the most abundant gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "answer": "Nitrogen"},
    {"question": "How many chromosomes do humans have?", "options": ["23", "44", "46", "48"], "answer": "46"},
    {"question": "What is the unit of electrical resistance?", "options": ["Volt", "Ampere", "Ohm", "Watt"], "answer": "Ohm"},
    {"question": "Which vitamin is produced when skin is exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
    {"question": "What is the boiling point of water at sea level?", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": "100°C"},
    {"question": "What part of the eye controls the amount of light entering?", "options": ["Retina", "Cornea", "Iris", "Lens"], "answer": "Iris"},
    {"question": "Which blood type is the universal donor?", "options": ["A+", "B-", "O-", "AB+"], "answer": "O-"},

    # Programming / Tech
    {"question": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Core Processing Unit"], "answer": "Central Processing Unit"},
    {"question": "Which language is known as the 'mother of all languages'?", "options": ["Python", "C", "Assembly", "FORTRAN"], "answer": "C"},
    {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "HighText Machine Language", "HyperText Machine Language", "HyperTool Markup Language"], "answer": "HyperText Markup Language"},
    {"question": "Which data structure uses LIFO order?", "options": ["Queue", "Stack", "Array", "Tree"], "answer": "Stack"},
    {"question": "What is the output of: type(3.14) in Python?", "options": ["int", "float", "double", "decimal"], "answer": "float"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "What does 'RAM' stand for?", "options": ["Read Access Memory", "Random Access Memory", "Rapid Access Memory", "Read And Memory"], "answer": "Random Access Memory"},
    {"question": "Which company created the Python programming language?", "options": ["Google", "Microsoft", "Guido van Rossum", "Apple"], "answer": "Guido van Rossum"},
    {"question": "What does 'OOP' stand for in programming?", "options": ["Object Oriented Programming", "Ordered Object Process", "Open Object Protocol", "Output Oriented Process"], "answer": "Object Oriented Programming"},
    {"question": "What symbol is used for single-line comments in Python?", "options": ["//", "/*", "#", "--"], "answer": "#"},
    {"question": "Which of these is NOT a Python data type?", "options": ["list", "tuple", "array", "dict"], "answer": "array"},
    {"question": "What does CSS stand for?", "options": ["Computer Style Sheets", "Cascading Style Sheets", "Creative Style System", "Colorful Style Sheets"], "answer": "Cascading Style Sheets"},
    {"question": "Which data structure uses FIFO order?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
    {"question": "What is the base of binary number system?", "options": ["2", "8", "10", "16"], "answer": "2"},
    {"question": "What does 'API' stand for?", "options": ["Application Programming Interface", "Applied Process Integration", "Automated Program Input", "Application Process Input"], "answer": "Application Programming Interface"},

    # History & Culture
    {"question": "In which year did World War II end?", "options": ["1943", "1944", "1945", "1946"], "answer": "1945"},
    {"question": "Who was the first person to walk on the Moon?", "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "John Glenn"], "answer": "Neil Armstrong"},
    {"question": "Which ancient wonder was located in Alexandria?", "options": ["Colossus of Rhodes", "Lighthouse of Alexandria", "Hanging Gardens", "Statue of Zeus"], "answer": "Lighthouse of Alexandria"},
    {"question": "What year did the Berlin Wall fall?", "options": ["1987", "1988", "1989", "1991"], "answer": "1989"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Homer"], "answer": "William Shakespeare"},
    {"question": "Which empire was ruled by Genghis Khan?", "options": ["Ottoman", "Roman", "Mongol", "Persian"], "answer": "Mongol"},
    {"question": "In which country was the first modern Olympic Games held?", "options": ["France", "UK", "Greece", "USA"], "answer": "Greece"},
    {"question": "Who was the first President of the United States?", "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "answer": "George Washington"},
    {"question": "Which war was fought between the North and South of the USA?", "options": ["World War I", "Revolutionary War", "Civil War", "Spanish-American War"], "answer": "Civil War"},
    {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Guglielmo Marconi"], "answer": "Alexander Graham Bell"},
    {"question": "In which year did the Titanic sink?", "options": ["1910", "1912", "1914", "1916"], "answer": "1912"},

    # Math
    {"question": "What is the value of Pi (to 2 decimal places)?", "options": ["3.12", "3.14", "3.16", "3.18"], "answer": "3.14"},
    {"question": "What is the square root of 144?", "options": ["11", "12", "13", "14"], "answer": "12"},
    {"question": "What is 15% of 200?", "options": ["25", "30", "35", "40"], "answer": "30"},
    {"question": "What is 7 factorial (7!)?", "options": ["2520", "4320", "5040", "7200"], "answer": "5040"},
    {"question": "What is the sum of angles in a triangle?", "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
    {"question": "What is 2 to the power of 10?", "options": ["512", "1024", "2048", "4096"], "answer": "1024"},
    {"question": "What is the next prime number after 7?", "options": ["8", "9", "10", "11"], "answer": "11"},
    {"question": "If a circle has radius 7, what is its area? (π ≈ 3.14)", "options": ["43.96", "49", "153.86", "21.98"], "answer": "153.86"},
    {"question": "What is the Roman numeral for 50?", "options": ["L", "C", "D", "V"], "answer": "L"},
    {"question": "How many degrees are in a full circle?", "options": ["180°", "270°", "360°", "450°"], "answer": "360°"},
]


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.configure(bg="#0d1117")
        self.root.resizable(False, False)

        self.questions = []
        self.current_index = 0
        self.score = 0
        self.answered = False
        self.time_left = TIMER_SECONDS
        self._timer_id = None

        self._build_ui()
        self.start_game()

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#161b22", pady=12)
        header.pack(fill="x")

        tk.Label(
            header, text="QUIZ GAME", bg="#161b22", fg="#f0f6fc",
            font=("Courier", 20, "bold")
        ).pack()

        # Progress & Score bar
        info_frame = tk.Frame(self.root, bg="#0d1117", pady=8)
        info_frame.pack(fill="x", padx=30)

        self.progress_label = tk.Label(
            info_frame, text="", bg="#0d1117", fg="#8b949e",
            font=("Courier", 11)
        )
        self.progress_label.pack(side="left")

        self.score_label = tk.Label(
            info_frame, text="", bg="#0d1117", fg="#3fb950",
            font=("Courier", 11, "bold")
        )
        self.score_label.pack(side="right")

        # Timer bar frame
        timer_frame = tk.Frame(self.root, bg="#0d1117")
        timer_frame.pack(fill="x", padx=30, pady=(0, 4))

        self.timer_label = tk.Label(
            timer_frame, text="", bg="#0d1117", fg="#58a6ff",
            font=("Courier", 12, "bold")
        )
        self.timer_label.pack(side="left")

        # Canvas progress bar
        self.bar_canvas = tk.Canvas(
            timer_frame, height=8, bg="#21262d",
            highlightthickness=0
        )
        self.bar_canvas.pack(side="left", fill="x", expand=True, padx=(10, 0))

        # Question box
        q_frame = tk.Frame(self.root, bg="#161b22", padx=24, pady=20)
        q_frame.pack(fill="x", padx=20, pady=(5, 10))

        self.question_label = tk.Label(
            q_frame, text="", bg="#161b22", fg="#f0f6fc",
            font=("Courier", 13), wraplength=480, justify="left"
        )
        self.question_label.pack()

        # Options
        self.option_buttons = []
        self.options_frame = tk.Frame(self.root, bg="#0d1117")
        self.options_frame.pack(padx=20, pady=5, fill="x")

        for i in range(4):
            btn = tk.Button(
                self.options_frame,
                text="", font=("Courier", 11),
                bg="#161b22", fg="#c9d1d9",
                activebackground="#1f2937", activeforeground="#f0f6fc",
                relief="flat", anchor="w", padx=16, pady=10,
                cursor="hand2", wraplength=460, justify="left",
                command=lambda i=i: self.check_answer(i)
            )
            btn.pack(fill="x", pady=4)
            self.option_buttons.append(btn)

        # Feedback label
        self.feedback_label = tk.Label(
            self.root, text="", bg="#0d1117",
            font=("Courier", 11, "bold"), pady=6
        )
        self.feedback_label.pack()

        # Next button
        self.next_btn = tk.Button(
            self.root, text="Next  ->", font=("Courier", 11, "bold"),
            bg="#238636", fg="#f0f6fc",
            activebackground="#2ea043", activeforeground="#f0f6fc",
            relief="flat", padx=24, pady=8, cursor="hand2",
            command=self.next_question, state="disabled"
        )
        self.next_btn.pack(pady=15)

    def start_game(self):
        self.questions = random.sample(QUESTIONS, 15)
        self.current_index = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        self._cancel_timer()
        self.answered = False
        self.time_left = TIMER_SECONDS
        q = self.questions[self.current_index]

        options = q["options"][:]
        random.shuffle(options)
        self.current_options = options

        self.progress_label.config(
            text=f"Question {self.current_index + 1} / {len(self.questions)}"
        )
        self.score_label.config(text=f"Score: {self.score}")
        self.question_label.config(text=q["question"])
        self.feedback_label.config(text="")
        self.next_btn.config(state="disabled")

        labels = ["A", "B", "C", "D"]
        for i, btn in enumerate(self.option_buttons):
            btn.config(
                text=f"  {labels[i]}.  {options[i]}",
                bg="#161b22", fg="#c9d1d9",
                state="normal"
            )

        self._tick()

    def _tick(self):
        self._update_timer_ui()
        if self.time_left > 0 and not self.answered:
            self.time_left -= 1
            self._timer_id = self.root.after(1000, self._tick)
        elif not self.answered:
            self._time_up()

    def _update_timer_ui(self):
        self.timer_label.config(text=f"  {self.time_left}s")

        # Color shifts: green -> yellow -> red
        ratio = self.time_left / TIMER_SECONDS
        if ratio > 0.5:
            color = "#3fb950"
        elif ratio > 0.25:
            color = "#d29922"
        else:
            color = "#f85149"

        self.timer_label.config(fg=color)

        # Draw progress bar
        self.bar_canvas.update_idletasks()
        w = self.bar_canvas.winfo_width()
        if w < 2:
            w = 300
        fill_w = int(w * ratio)
        self.bar_canvas.delete("all")
        self.bar_canvas.create_rectangle(0, 0, fill_w, 8, fill=color, outline="")

    def _cancel_timer(self):
        if self._timer_id is not None:
            self.root.after_cancel(self._timer_id)
            self._timer_id = None

    def _time_up(self):
        self.answered = True
        correct = self.questions[self.current_index]["answer"]
        for i, btn in enumerate(self.option_buttons):
            btn.config(state="disabled")
            if self.current_options[i] == correct:
                btn.config(bg="#1a4731", fg="#3fb950")
        self.feedback_label.config(
            text=f"Time's up! Answer: {correct}", fg="#d29922"
        )
        if self.current_index + 1 == len(self.questions):
            self.next_btn.config(text="See Results", state="normal")
        else:
            self.next_btn.config(text="Next  ->", state="normal")

    def check_answer(self, index):
        if self.answered:
            return

        self._cancel_timer()
        self.answered = True
        selected = self.current_options[index]
        correct = self.questions[self.current_index]["answer"]

        for i, btn in enumerate(self.option_buttons):
            btn.config(state="disabled")
            if self.current_options[i] == correct:
                btn.config(bg="#1a4731", fg="#3fb950")
            elif i == index and selected != correct:
                btn.config(bg="#4a1a1a", fg="#f85149")

        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="#3fb950")
        else:
            self.feedback_label.config(
                text=f"Wrong! Answer: {correct}", fg="#f85149"
            )

        self.score_label.config(text=f"Score: {self.score}")

        if self.current_index + 1 == len(self.questions):
            self.next_btn.config(text="See Results", state="normal")
        else:
            self.next_btn.config(text="Next  ->", state="normal")

    def next_question(self):
        self.current_index += 1
        if self.current_index >= len(self.questions):
            self.show_results()
        else:
            self.load_question()

    def show_results(self):
        total = len(self.questions)
        pct = (self.score / total) * 100

        if pct == 100:
            grade, color = "Perfect! Trophy", "#f0e68c"
        elif pct >= 80:
            grade, color = "Great job!", "#3fb950"
        elif pct >= 60:
            grade, color = "Not bad!", "#d29922"
        elif pct >= 40:
            grade, color = "Keep practicing!", "#f85149"
        else:
            grade, color = "Better luck next time.", "#8b949e"

        result_win = tk.Toplevel(self.root)
        result_win.title("Results")
        result_win.configure(bg="#0d1117")
        result_win.resizable(False, False)

        tk.Label(
            result_win, text="RESULTS", bg="#0d1117", fg="#f0f6fc",
            font=("Courier", 18, "bold"), pady=20
        ).pack()

        tk.Label(
            result_win,
            text=f"{self.score} / {total}",
            bg="#0d1117", fg=color,
            font=("Courier", 40, "bold")
        ).pack()

        tk.Label(
            result_win, text=f"{pct:.0f}%",
            bg="#0d1117", fg="#8b949e",
            font=("Courier", 16)
        ).pack()

        tk.Label(
            result_win, text=grade,
            bg="#0d1117", fg=color,
            font=("Courier", 14, "bold"), pady=10
        ).pack()

        btn_frame = tk.Frame(result_win, bg="#0d1117", pady=15)
        btn_frame.pack()

        tk.Button(
            btn_frame, text="Play Again", font=("Courier", 11, "bold"),
            bg="#238636", fg="#f0f6fc", relief="flat",
            padx=20, pady=8, cursor="hand2",
            command=lambda: [result_win.destroy(), self.start_game()]
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame, text="Quit", font=("Courier", 11, "bold"),
            bg="#21262d", fg="#f0f6fc", relief="flat",
            padx=20, pady=8, cursor="hand2",
            command=self.root.quit
        ).pack(side="left", padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("540x620")
    app = QuizGame(root)
    root.mainloop()