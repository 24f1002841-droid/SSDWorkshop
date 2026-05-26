#!/usr/bin/env python3
"""Entry point for the calculator application."""

import argparse

from calculator.cli import run_cli


def main() -> None:
    parser = argparse.ArgumentParser(description="A simple Python calculator")
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in command-line mode instead of the GUI",
    )
    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        from calculator.gui import run

        run()


if __name__ == "__main__":
    main()
