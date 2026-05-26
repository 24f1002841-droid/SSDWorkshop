"""Simple calculator GUI built with tkinter."""

import tkinter as tk
from tkinter import font as tkfont

from calculator.core import CalculatorError, apply


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.display_var = tk.StringVar(value="0")
        self.pending_value: float | None = None
        self.pending_operator: str | None = None
        self.reset_on_next_input = False

        self._build_ui()

    def _build_ui(self) -> None:
        display_font = tkfont.Font(family="Helvetica", size=28, weight="bold")
        button_font = tkfont.Font(family="Helvetica", size=16)

        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=display_font,
            justify="right",
            state="readonly",
            readonlybackground="#f5f5f5",
            relief="flat",
            bd=10,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

        buttons = [
            ("C", 1, 0, self.clear),
            ("±", 1, 1, self.toggle_sign),
            ("%", 1, 2, self.percent),
            ("/", 1, 3, lambda: self.set_operator("/")),
            ("7", 2, 0, lambda: self.append_digit("7")),
            ("8", 2, 1, lambda: self.append_digit("8")),
            ("9", 2, 2, lambda: self.append_digit("9")),
            ("*", 2, 3, lambda: self.set_operator("*")),
            ("4", 3, 0, lambda: self.append_digit("4")),
            ("5", 3, 1, lambda: self.append_digit("5")),
            ("6", 3, 2, lambda: self.append_digit("6")),
            ("-", 3, 3, lambda: self.set_operator("-")),
            ("1", 4, 0, lambda: self.append_digit("1")),
            ("2", 4, 1, lambda: self.append_digit("2")),
            ("3", 4, 2, lambda: self.append_digit("3")),
            ("+", 4, 3, lambda: self.set_operator("+")),
            ("0", 5, 0, lambda: self.append_digit("0"), 2),
            (".", 5, 2, self.append_decimal),
            ("=", 5, 3, self.calculate),
        ]

        for spec in buttons:
            label, row, col, command = spec[0], spec[1], spec[2], spec[3]
            colspan = spec[4] if len(spec) > 4 else 1
            btn = tk.Button(
                self.root,
                text=label,
                font=button_font,
                width=4 if colspan == 1 else 9,
                height=2,
                command=command,
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=4,
                pady=4,
            )

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    def _current_value(self) -> float:
        text = self.display_var.get()
        if text in ("", "Error"):
            return 0.0
        return float(text)

    def _set_display(self, value: float | str) -> None:
        if isinstance(value, str):
            self.display_var.set(value)
            return
        if value == int(value):
            self.display_var.set(str(int(value)))
        else:
            self.display_var.set(str(value))

    def append_digit(self, digit: str) -> None:
        current = self.display_var.get()
        if self.reset_on_next_input or current in ("0", "Error"):
            self.display_var.set(digit)
            self.reset_on_next_input = False
        else:
            self.display_var.set(current + digit)

    def append_decimal(self) -> None:
        current = self.display_var.get()
        if self.reset_on_next_input or current == "Error":
            self.display_var.set("0.")
            self.reset_on_next_input = False
        elif "." not in current:
            self.display_var.set(current + ".")

    def clear(self) -> None:
        self.display_var.set("0")
        self.pending_value = None
        self.pending_operator = None
        self.reset_on_next_input = False

    def toggle_sign(self) -> None:
        value = self._current_value()
        self._set_display(-value)

    def percent(self) -> None:
        value = self._current_value()
        self._set_display(value / 100)

    def set_operator(self, operator: str) -> None:
        if self.pending_operator and not self.reset_on_next_input:
            self.calculate()
        self.pending_value = self._current_value()
        self.pending_operator = operator
        self.reset_on_next_input = True

    def calculate(self) -> None:
        if self.pending_value is None or self.pending_operator is None:
            return
        try:
            result = apply(
                self.pending_value,
                self.pending_operator,
                self._current_value(),
            )
        except CalculatorError as exc:
            self.display_var.set("Error")
            self.pending_value = None
            self.pending_operator = None
            self.reset_on_next_input = True
            return

        self._set_display(result)
        self.pending_value = None
        self.pending_operator = None
        self.reset_on_next_input = True


def run() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()
