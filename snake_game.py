import tkinter as tk
import random

# ── Config ────────────────────────────────────────────────────────────────────
WIDTH        = 600
HEIGHT       = 600
CELL         = 20
ROWS         = HEIGHT // CELL
COLS         = WIDTH  // CELL
START_SPEED  = 120          # ms between frames (lower = faster)
SPEED_STEP   = 5            # ms faster every 5 food eaten
MIN_SPEED    = 50

# ── Colors ────────────────────────────────────────────────────────────────────
BG           = "#0d1117"
GRID_COLOR   = "#161b22"
SNAKE_HEAD   = "#3fb950"
SNAKE_BODY   = "#238636"
SNAKE_OUTLINE= "#0d1117"
FOOD_COLOR   = "#f85149"
FOOD_OUTLINE = "#ff7b72"
TEXT_COLOR   = "#f0f6fc"
DIM_COLOR    = "#8b949e"
OVERLAY_BG   = "#161b22"


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self._build_ui()
        self._bind_keys()
        self.new_game()

    # ── UI setup ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Top bar
        bar = tk.Frame(self.root, bg="#161b22", pady=8)
        bar.pack(fill="x")

        tk.Label(bar, text="SNAKE", bg="#161b22", fg=TEXT_COLOR,
                 font=("Courier", 18, "bold")).pack(side="left", padx=16)

        self.score_label = tk.Label(bar, text="Score: 0", bg="#161b22",
                                     fg=SNAKE_HEAD, font=("Courier", 13, "bold"))
        self.score_label.pack(side="left", padx=10)

        self.high_label = tk.Label(bar, text="Best: 0", bg="#161b22",
                                    fg=DIM_COLOR, font=("Courier", 11))
        self.high_label.pack(side="right", padx=16)

        self.level_label = tk.Label(bar, text="Level: 1", bg="#161b22",
                                     fg=DIM_COLOR, font=("Courier", 11))
        self.level_label.pack(side="right", padx=10)

        # Canvas
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT,
                                 bg=BG, highlightthickness=0)
        self.canvas.pack()

        # Bottom hint
        hint = tk.Frame(self.root, bg=BG, pady=6)
        hint.pack(fill="x")
        tk.Label(hint, text="Arrow keys / WASD to move   |   P to pause   |   R to restart",
                 bg=BG, fg=DIM_COLOR, font=("Courier", 9)).pack()

    def _bind_keys(self):
        self.root.bind("<KeyPress>", self._on_key)

    # ── Game state ────────────────────────────────────────────────────────────
    def new_game(self):
        self._cancel_loop()
        self.direction   = "Right"
        self.next_dir    = "Right"
        self.snake       = [(ROWS // 2, COLS // 2 - i) for i in range(3)]
        self.score       = 0
        self.high_score  = getattr(self, "high_score", 0)
        self.speed       = START_SPEED
        self.level       = 1
        self.food_eaten  = 0
        self.paused      = False
        self.game_over   = False
        self._place_food()
        self._draw()
        self._show_overlay("SNAKE", "Press any arrow key to start", show_restart=False)
        self.waiting_start = True

    def _place_food(self):
        empty = [(r, c) for r in range(ROWS) for c in range(COLS)
                 if (r, c) not in self.snake]
        self.food = random.choice(empty)

    # ── Main loop ─────────────────────────────────────────────────────────────
    def _loop(self):
        if self.paused or self.game_over:
            return
        self._move()
        self._draw()
        if not self.game_over:
            self._after_id = self.root.after(self.speed, self._loop)

    def _cancel_loop(self):
        after_id = getattr(self, "_after_id", None)
        if after_id:
            self.root.after_cancel(after_id)
            self._after_id = None

    def _move(self):
        self.direction = self.next_dir
        head_r, head_c = self.snake[0]

        dr, dc = {"Up": (-1,0), "Down": (1,0),
                  "Left": (0,-1), "Right": (0,1)}[self.direction]
        new_head = (head_r + dr, head_c + dc)

        # Wall collision
        if not (0 <= new_head[0] < ROWS and 0 <= new_head[1] < COLS):
            self._end_game()
            return

        # Self collision
        if new_head in self.snake:
            self._end_game()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score      += 10
            self.food_eaten += 1
            self._place_food()
            self._update_hud()

            # Level up every 5 food
            if self.food_eaten % 5 == 0:
                self.level += 1
                self.speed  = max(MIN_SPEED, self.speed - SPEED_STEP)
        else:
            self.snake.pop()

    def _end_game(self):
        self.game_over  = True
        self.high_score = max(self.high_score, self.score)
        self._draw()
        self._show_overlay(
            "GAME OVER",
            f"Score: {self.score}   Best: {self.high_score}",
            show_restart=True
        )

    # ── Drawing ───────────────────────────────────────────────────────────────
    def _draw(self):
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_food()
        self._draw_snake()

    def _draw_grid(self):
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c * CELL, r * CELL
                x2, y2 = x1 + CELL, y1 + CELL
                self.canvas.create_rectangle(x1, y1, x2, y2,
                                              fill=BG, outline=GRID_COLOR, width=1)

    def _draw_snake(self):
        for i, (r, c) in enumerate(self.snake):
            x1, y1 = c * CELL + 2, r * CELL + 2
            x2, y2 = x1 + CELL - 4, y1 + CELL - 4
            color = SNAKE_HEAD if i == 0 else SNAKE_BODY
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                          fill=color, outline=SNAKE_OUTLINE,
                                          width=1)
            # Eyes on head
            if i == 0:
                self._draw_eyes(r, c)

    def _draw_eyes(self, r, c):
        cx = c * CELL + CELL // 2
        cy = r * CELL + CELL // 2
        offsets = {
            "Right": [(4, -3), (4, 3)],
            "Left":  [(-4, -3), (-4, 3)],
            "Up":    [(-3, -4), (3, -4)],
            "Down":  [(-3, 4), (3, 4)],
        }
        for dx, dy in offsets.get(self.direction, [(4, -3), (4, 3)]):
            self.canvas.create_oval(cx+dx-2, cy+dy-2, cx+dx+2, cy+dy+2,
                                     fill="#0d1117", outline="")

    def _draw_food(self):
        r, c = self.food
        x1, y1 = c * CELL + 3, r * CELL + 3
        x2, y2 = x1 + CELL - 6, y1 + CELL - 6
        self.canvas.create_oval(x1, y1, x2, y2,
                                 fill=FOOD_COLOR, outline=FOOD_OUTLINE, width=2)

    def _show_overlay(self, title, subtitle, show_restart=True):
        cx, cy = WIDTH // 2, HEIGHT // 2

        self.canvas.create_rectangle(cx-180, cy-70, cx+180, cy+70,
                                      fill=OVERLAY_BG, outline="#30363d", width=2)
        self.canvas.create_text(cx, cy - 28, text=title,
                                 fill=SNAKE_HEAD, font=("Courier", 22, "bold"))
        self.canvas.create_text(cx, cy + 8, text=subtitle,
                                 fill=TEXT_COLOR, font=("Courier", 11))
        if show_restart:
            self.canvas.create_text(cx, cy + 40, text="Press R to restart",
                                     fill=DIM_COLOR, font=("Courier", 10))

    def _update_hud(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.high_label.config(text=f"Best: {max(self.high_score, self.score)}")
        self.level_label.config(text=f"Level: {self.level}")

    # ── Input ─────────────────────────────────────────────────────────────────
    _OPPOSITES = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    _KEY_MAP   = {
        "Up": "Up",    "w": "Up",    "W": "Up",
        "Down": "Down","s": "Down",  "S": "Down",
        "Left": "Left","a": "Left",  "A": "Left",
        "Right":"Right","d": "Right","D": "Right",
    }

    def _on_key(self, event):
        key = event.keysym

        # Start on first arrow press
        if getattr(self, "waiting_start", False):
            if key in self._KEY_MAP:
                self.waiting_start = False
                self.canvas.delete("all")
                self._draw()
                self._after_id = self.root.after(self.speed, self._loop)
            return

        if key in ("r", "R"):
            self.new_game()
            return

        if key in ("p", "P") and not self.game_over:
            self.paused = not self.paused
            if self.paused:
                self._show_overlay("PAUSED", "Press P to continue", show_restart=False)
            else:
                self._draw()
                self._after_id = self.root.after(self.speed, self._loop)
            return

        if key in self._KEY_MAP:
            new_dir = self._KEY_MAP[key]
            if new_dir != self._OPPOSITES.get(self.direction):
                self.next_dir = new_dir


if __name__ == "__main__":
    root = tk.Tk()
    app  = SnakeGame(root)
    root.mainloop()