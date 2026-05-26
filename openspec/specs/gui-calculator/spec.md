# gui-calculator Specification

## Purpose
TBD - created by archiving change python-gui-calculator. Update Purpose after archive.
## Requirements
### Requirement: Application launches with calculator window

The system SHALL open a desktop window titled for the calculator with a visible display area and a grid of buttons when started via the documented entry command.

#### Scenario: Launch from module

- **WHEN** the user runs `python -m calculator` from the project root
- **THEN** a GUI window appears with a display and digit/operator buttons

### Requirement: Digit and decimal entry

The system SHALL append digits and a single decimal point to the current operand shown on the display when the user presses digit or `.` buttons.

#### Scenario: Enter multi-digit number

- **WHEN** the user presses `1`, then `2`, then `3`
- **THEN** the display shows `123`

#### Scenario: Decimal point once per operand

- **WHEN** the user presses `3`, `.`, `1`, `.`, `4`
- **THEN** the display shows `3.14` (second `.` ignored for same operand)

### Requirement: Basic arithmetic operations

The system SHALL support addition, subtraction, multiplication, and division between two operands using `+`, `-`, `×`, and `÷` buttons followed by `=`.

#### Scenario: Addition

- **WHEN** the user enters `7`, presses `+`, enters `5`, presses `=`
- **THEN** the display shows `12`

#### Scenario: Subtraction

- **WHEN** the user enters `10`, presses `-`, enters `3`, presses `=`
- **THEN** the display shows `7`

#### Scenario: Multiplication

- **WHEN** the user enters `4`, presses `×`, enters `6`, presses `=`
- **THEN** the display shows `24`

#### Scenario: Division

- **WHEN** the user enters `15`, presses `÷`, enters `3`, presses `=`
- **THEN** the display shows `5`

### Requirement: Clear resets state

The system SHALL reset the calculator state and show `0` on the display when the user presses `C`.

#### Scenario: Clear after input

- **WHEN** the user has entered digits or an operation and presses `C`
- **THEN** the display shows `0` and a new calculation can begin

### Requirement: Division by zero shows error

The system SHALL display `Error` and refuse a numeric result when division by zero is attempted.

#### Scenario: Divide by zero

- **WHEN** the user enters `8`, presses `÷`, enters `0`, presses `=`
- **THEN** the display shows `Error`

#### Scenario: Recover after error

- **WHEN** the display shows `Error` and the user presses `C`
- **THEN** the display shows `0` and the calculator accepts new input

### Requirement: Chained operations

The system SHALL apply the pending operator to the current result when the user presses a new operator before pressing `=`.

#### Scenario: Chain add then multiply

- **WHEN** the user enters `2`, `+`, `3`, `×`, `4`, `=`
- **THEN** the display shows `20` (i.e. (2+3)×4)

