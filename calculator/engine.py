from __future__ import annotations

from typing import Optional, Tuple


class CalculatorEngine:
    """
    Pure calculator logic (no tkinter).

    Tracks:
      - current operand being edited (string for display precision)
      - pending operator and accumulated left operand
      - error state after divide-by-zero
    """

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self._error: bool = False
        self._acc: Optional[float] = None
        self._pending_op: Optional[str] = None  # '+', '-', '*', '/'
        self._operand_new: bool = True
        self._current_operand: str = "0"

    @property
    def display(self) -> str:
        if self._error:
            return "Error"
        return self._current_operand if self._current_operand else "0"

    def input_digit(self, digit: str) -> str:
        if self._error:
            return self.display

        if self._operand_new:
            # Start fresh operand.
            self._current_operand = digit
            self._operand_new = False
            return self.display

        if self._current_operand == "0":
            # Replace leading zero.
            self._current_operand = digit
        else:
            self._current_operand += digit
        return self.display

    def input_decimal(self) -> str:
        if self._error:
            return self.display

        if self._operand_new:
            self._current_operand = "0."
            self._operand_new = False
            return self.display

        if "." not in self._current_operand:
            self._current_operand += "."

        return self.display

    def input_operator(self, op: str) -> str:
        """
        op must be one of: '+', '-', '*', '/'.
        """
        if self._error:
            return self.display

        if self._pending_op is None:
            # First operator: latch the accumulated value.
            self._acc = self._parse_current_operand()
            self._pending_op = op
            self._operand_new = True
            return self.display

        if not self._operand_new:
            # Apply pending op to acc and current operand.
            res, err = self._apply(self._acc, self._pending_op, self._parse_current_operand())
            if err:
                self._error = True
                self._pending_op = None
                self._acc = None
                self._current_operand = "0"
                self._operand_new = True
                return self.display

            self._acc = res
            self._current_operand = self._format_number(res)

        # Update pending operator for chained operations.
        self._pending_op = op
        self._operand_new = True
        return self.display

    def input_equals(self) -> str:
        if self._error:
            return self.display

        if self._pending_op is None:
            return self.display

        left = self._acc if self._acc is not None else self._parse_current_operand()
        right = self._parse_current_operand()

        res, err = self._apply(left, self._pending_op, right)
        if err:
            self._error = True
            self._pending_op = None
            self._acc = None
            self._current_operand = "0"
            self._operand_new = True
            return self.display

        self._pending_op = None
        self._acc = res
        self._current_operand = self._format_number(res)
        self._operand_new = True
        return self.display

    def _parse_current_operand(self) -> float:
        try:
            return float(self._current_operand)
        except ValueError:
            return 0.0

    def _apply(self, a: float, op: str, b: float) -> Tuple[float, bool]:
        if op == "+":
            return a + b, False
        if op == "-":
            return a - b, False
        if op == "*":
            return a * b, False
        if op == "/":
            if b == 0.0:
                return 0.0, True
            return a / b, False
        raise ValueError(f"Unsupported operator: {op}")

    def _format_number(self, n: float) -> str:
        # Show integer-looking results without ".0".
        rounded = round(n)
        if abs(n - rounded) < 1e-12:
            return str(int(rounded))

        s = f"{n:.10f}".rstrip("0").rstrip(".")
        return s if s else "0"

