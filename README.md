# SDD Workshop — Simple Calculator

A minimal Python calculator with a graphical UI (tkinter) and an optional command-line mode.

## Requirements

- Python 3.10+
- tkinter (included with most Python installations; on Debian/Ubuntu: `sudo apt install python3-tk`)

## Run the GUI

```bash
python main.py
```

## Run the CLI

```bash
python main.py --cli
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project layout

```
calculator/
  core.py   # arithmetic logic
  gui.py    # tkinter window
  cli.py    # terminal interface
main.py     # entry point
tests/      # unit tests
```
