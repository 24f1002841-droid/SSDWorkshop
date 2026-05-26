## 1. Project setup

- [x] 1.1 Create `calculator/` package with `__init__.py`, `__main__.py`, `app.py`, and `engine.py`
- [x] 1.2 Update README with run instructions (`python -m calculator`) and note `python3-tk` on Linux if needed

## 2. Calculator engine (logic)

- [x] 2.1 Implement `CalculatorEngine` with state for current operand, pending operator, and error flag
- [x] 2.2 Implement digit and decimal input (ignore extra `.` in same operand)
- [x] 2.3 Implement `+`, `-`, `×`, `÷` with chained-operation behavior per spec
- [x] 2.4 Implement `=` to evaluate pending operation and show result
- [x] 2.5 Implement `clear()` resetting display to `0` and all state
- [x] 2.6 Return error state for division by zero; allow recovery via clear

## 3. GUI (tkinter)

- [x] 3.1 Build main window with read-only display (right-aligned) and 4×5 button grid
- [x] 3.2 Wire digit buttons `0–9` and `.` to engine input handlers
- [x] 3.3 Wire operator buttons `+`, `-`, `×`, `÷`, `=`, and `C` to engine
- [x] 3.4 Sync display label/entry with engine output after each action
- [x] 3.5 Set window title and minimum size for usable layout

## 4. Entry point and verification

- [x] 4.1 Implement `__main__.py` to launch `CalculatorApp` and start tkinter main loop
- [x] 4.2 Manually verify spec scenarios: launch, digits, four operations, clear, divide-by-zero error, chained operations
