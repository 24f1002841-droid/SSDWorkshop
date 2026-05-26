"""Basic arithmetic operations for the calculator."""

from typing import Callable


class CalculatorError(Exception):
    """Raised when an operation cannot be performed."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise CalculatorError("Cannot divide by zero")
    return a / b


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def apply(left: float, operator: str, right: float) -> float:
    if operator not in OPERATIONS:
        raise CalculatorError(f"Unknown operator: {operator}")
    return OPERATIONS[operator](left, right)
