# Calculator App

A Python calculator application featuring both a Graphical User Interface (GUI) built with Tkinter and an interactive Command-Line Interface (CLI) mode.

## Overview

The Calculator App provides basic and intermediate mathematical computation capabilities. The core math logic is encapsulated separately in a dedicated module, allowing both desktop GUI and terminal interfaces to share the exact same underlying logic.

## Key Features

- Graphical Interface (GUI): Modern dark-themed window constructed with Tkinter, supporting mouse clicks, full keyboard input bindings, hover states, and calculation history log.
- Command-Line Interface (CLI): Interactive terminal mode supporting operation chaining.
- Modular Design: Clean separation between GUI view components, CLI controller routines, and arithmetic logic.
- Exception Handling: Graceful error trapping for division by zero and invalid input formats.

## System Requirements

- Python 3.8 or higher.
- Tkinter library (included by default in standard Python Windows installations).

## Installation and Execution

### Running the GUI Application (Default)
To launch the graphical window interface, execute:
```bash
python main.py
```

### Running the CLI Application
To launch the interactive command-line mode in terminal, pass the `--cli` flag:
```bash
python main.py --cli
```

## Project File Structure

```
calculator-app/
│
├── calculator.py   # Core math module (addition, subtraction, multiplication, division)
├── gui.py          # Tkinter graphical user interface implementation
├── main.py         # Primary application entry point routing CLI/GUI execution
├── .gitignore      # Standard Git exclusion file
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License.
