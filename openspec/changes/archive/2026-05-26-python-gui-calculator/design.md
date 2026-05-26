## Context

The repository is a spec-driven development workshop with no application code yet. The calculator will be the first runnable artifact: a single-process desktop app using Python's standard library so setup stays minimal for participants.

## Goals / Non-Goals

**Goals:**

- Deliver a working four-function calculator in a resizable window.
- Separate UI (tkinter widgets, layout) from calculation logic for clarity and light testing.
- Handle common edge cases: division by zero, malformed expressions, consecutive operators.
- Document how to run the app (`python -m calculator` or equivalent).

**Non-Goals:**

- Scientific functions (sin, log, memory registers).
- Keyboard shortcuts beyond optional basic support.
- Packaging as `.exe`/`.app` or publishing to PyPI.
- Web or mobile UI.
- Persistent history or settings.

## Decisions

### 1. GUI toolkit: `tkinter`

**Choice:** Use `tkinter` (stdlib).

**Rationale:** No extra install on typical Python 3 builds; sufficient for buttons, labels, and grid layout.

**Alternatives:** PyQt/PySide (heavier dependency), CustomTkinter (nicer styling but extra package).

### 2. Layout: display + 4×5 button grid

**Choice:** One read-only display (`Entry` or `Label`) and buttons for digits `0–9`, `.`, `+`, `-`, `×`, `÷`, `C`, `=`.

**Rationale:** Matches familiar calculator UX; simple to wire with `grid()`.

### 3. Expression model: chained binary operations

**Choice:** Track `current_value`, `pending_operator`, and `operand_ready` flag. On `=`, apply pending operation. New digit after operator starts a fresh operand.

**Rationale:** Avoids `eval()` on user input (security and parsing surprises). Behavior matches basic desk calculators.

**Alternatives:** Full expression parser with operator precedence (more complex than needed for “simple” scope).

### 4. Module structure

**Choice:**

```
calculator/
  __init__.py
  __main__.py      # entry: python -m calculator
  app.py           # tkinter window and event bindings
  engine.py        # CalculatorEngine class (pure logic)
```

**Rationale:** `engine.py` can be unit-tested without spinning up the GUI.

### 5. Error display

**Choice:** Show `Error` on display for division by zero or invalid state; `C` resets engine and display.

**Rationale:** Simple feedback without modal dialogs.

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| `tkinter` missing on minimal Linux Python (`python3-tk` not installed) | Document install step in README |
| Float rounding (e.g. `0.1 + 0.2`) | Accept for workshop scope; optional rounding on display only |
| Chained `=` behavior differs from some calculators | Document expected behavior in spec scenarios |

## Migration Plan

N/A — greenfield. Participants clone repo, install `python3-tk` if needed, run `python -m calculator`.

## Open Questions

- None blocking implementation; keyboard input can be a follow-up if time permits.
