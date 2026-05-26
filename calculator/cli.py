"""Command-line calculator interface."""

from calculator.core import CalculatorError, OPERATIONS, apply


def run_cli() -> None:
    print("Simple Calculator (type 'quit' to exit)")
    print("Supported operators:", ", ".join(OPERATIONS))

    while True:
        try:
            left_raw = input("\nFirst number: ").strip()
            if left_raw.lower() in ("quit", "exit", "q"):
                break
            left = float(left_raw)

            operator = input("Operator (+, -, *, /): ").strip()
            if operator.lower() in ("quit", "exit", "q"):
                break

            right_raw = input("Second number: ").strip()
            if right_raw.lower() in ("quit", "exit", "q"):
                break
            right = float(right_raw)

            result = apply(left, operator, right)
            print(f"Result: {result}")
        except CalculatorError as exc:
            print(f"Error: {exc}")
        except ValueError:
            print("Error: Please enter valid numbers.")

    print("Goodbye!")
