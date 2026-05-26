from __future__ import annotations

import tkinter as tk

from .engine import CalculatorEngine


class CalculatorApp:
    def __init__(self) -> None:
        self.engine = CalculatorEngine()

        self.root = tk.Tk()
        self.root.title("Python GUI Calculator")
        self.root.minsize(320, 420)

        # Top: display
        self.display_var = tk.StringVar(value=self.engine.display)
        self.display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            justify="right",
            font=("Arial", 24),
            bd=2,
            relief=tk.GROOVE,
            state="readonly",
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Bottom: button grid (4x5)
        self._build_button_grid()

        # Make resizing sensible.
        for c in range(4):
            self.root.grid_columnconfigure(c, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)

    def run(self) -> None:
        self.root.mainloop()

    def _build_button_grid(self) -> None:
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

        for r in range(5):
            btn_frame.grid_rowconfigure(r, weight=1)
        for c in range(4):
            btn_frame.grid_columnconfigure(c, weight=1)

        def add_button(text: str, row: int, col: int, on_click) -> None:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Arial", 16),
                command=lambda: self._handle(on_click),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Grid layout (4 columns x 5 rows)
        # Row 0:  C   ÷   ×   -
        add_button("C", 0, 0, self.engine.clear)
        add_button("÷", 0, 1, lambda: self.engine.input_operator("/"))
        add_button("×", 0, 2, lambda: self.engine.input_operator("*"))
        add_button("-", 0, 3, lambda: self.engine.input_operator("-"))

        # Row 1: 7   8   9   +
        add_button("7", 1, 0, lambda: self.engine.input_digit("7"))
        add_button("8", 1, 1, lambda: self.engine.input_digit("8"))
        add_button("9", 1, 2, lambda: self.engine.input_digit("9"))
        add_button("+", 1, 3, lambda: self.engine.input_operator("+"))

        # Row 2: 4   5   6   (blank)
        add_button("4", 2, 0, lambda: self.engine.input_digit("4"))
        add_button("5", 2, 1, lambda: self.engine.input_digit("5"))
        add_button("6", 2, 2, lambda: self.engine.input_digit("6"))

        # Row 3: 1   2   3   (blank)
        add_button("1", 3, 0, lambda: self.engine.input_digit("1"))
        add_button("2", 3, 1, lambda: self.engine.input_digit("2"))
        add_button("3", 3, 2, lambda: self.engine.input_digit("3"))

        # Row 4: 0   .   (blank)   =
        add_button("0", 4, 0, lambda: self.engine.input_digit("0"))
        add_button(".", 4, 1, self.engine.input_decimal)
        add_button("=", 4, 3, self.engine.input_equals)

    def _handle(self, func) -> None:
        # Apply engine action then refresh display.
        func()
        self.display_var.set(self.engine.display)

