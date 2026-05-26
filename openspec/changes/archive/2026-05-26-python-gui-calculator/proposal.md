## Why

This workshop project needs a small, runnable Python application to demonstrate spec-driven development end to end. A desktop GUI calculator is familiar, easy to validate manually, and exercises UI layout, event handling, and arithmetic logic without external services.

## What Changes

- Add a Python desktop calculator with a graphical window (display + button grid).
- Support basic operations: addition, subtraction, multiplication, division.
- Support digit entry, decimal point, clear, and equals to evaluate the current expression.
- Provide a single entry point to launch the app and brief README instructions to run it.
- Add minimal project metadata (`requirements.txt` or documented stdlib-only approach).

## Capabilities

### New Capabilities

- `gui-calculator`: Desktop calculator UI and evaluation behavior (display, buttons, arithmetic, error handling for invalid input and division by zero).

### Modified Capabilities

- _(none — greenfield project)_

## Impact

- **New code**: Python application under a dedicated package or module (e.g. `calculator/`).
- **Dependencies**: Standard library `tkinter` preferred (ships with most Python installs); no server or database.
- **Systems**: Local desktop only; no APIs or deployment changes.
