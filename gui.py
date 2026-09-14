"""
Modern Calculator Graphical User Interface Module

This module implements a dark-themed Tkinter calculator GUI.
It connects user interactions to the core math operations defined in calculator.py.
"""

import tkinter as tk
from tkinter import ttk
import math
import calculator


class ModernCalculatorGUI(tk.Tk):
    """
    Main Tkinter Window Class for the Modern Calculator.

    Inherits from tk.Tk to build the graphical application interface,
    handling layout configuration, button events, keyboard bindings, and history tracking.
    """

    def __init__(self):
        """Initialize window parameters, color scheme, state variables, and layout."""
        super().__init__()

        # Configure root window properties
        self.title("Calculator 2.0")
        self.geometry("380x560")
        self.minsize(340, 500)
        self.configure(bg="#1e1e2e")

        # Safely attempt setting window icon
        try:
            self.iconbitmap(default="")
        except Exception:
            pass

        # Define color palette constants (Catppuccin Mocha Dark Theme)
        self.BG_MAIN = "#1e1e2e"         # Main background color
        self.BG_DISPLAY = "#181825"      # Screen display background
        self.TEXT_PRIMARY = "#cdd6f4"   # Main text color
        self.TEXT_SECONDARY = "#a6adc8" # Secondary label color
        self.BTN_NUM_BG = "#313244"      # Digit button background
        self.BTN_NUM_FG = "#cdd6f4"      # Digit button text color
        self.BTN_NUM_HOVER = "#45475a"   # Digit button hover background
        self.BTN_OP_BG = "#89b4fa"       # Operator button background
        self.BTN_OP_FG = "#11111b"       # Operator button text color
        self.BTN_OP_HOVER = "#b4befe"    # Operator button hover color
        self.BTN_FN_BG = "#45475a"       # Function button background
        self.BTN_FN_FG = "#cdd6f4"       # Function button text color
        self.BTN_FN_HOVER = "#585b70"    # Function button hover color
        self.BTN_EQ_BG = "#a6e3a1"       # Equals button background
        self.BTN_EQ_FG = "#11111b"       # Equals button text color
        self.BTN_EQ_HOVER = "#94e2d5"    # Equals button hover color
        self.BTN_CLEAR_BG = "#f38ba8"    # Clear button background
        self.BTN_CLEAR_FG = "#11111b"    # Clear button text color
        self.BTN_CLEAR_HOVER = "#f5e0dc" # Clear button hover color

        # Internal calculator state tracking variables
        self.current_input = "0"        # Currently typed numeric string
        self.expression = ""            # Active arithmetic expression string
        self.previous_result = None     # Store intermediate calculation result
        self.pending_operator = None    # Store standard operator waiting for next operand
        self.new_input_start = True     # Flag to clear display when new digit is pressed
        self.history = []               # Log of completed evaluation strings

        # Initialize layout widgets and user input bindings
        self._create_layout()
        self._bind_keys()

    def _create_layout(self):
        """Construct display widgets, labels, and button grid layout."""
        # Top header container frame
        header_frame = tk.Frame(self, bg=self.BG_MAIN)
        header_frame.pack(fill=tk.X, padx=16, pady=(12, 4))

        # Title text label
        title_label = tk.Label(
            header_frame,
            text="CALCULATOR 2.0",
            font=("Segoe UI", 10, "bold"),
            fg=self.TEXT_SECONDARY,
            bg=self.BG_MAIN,
            anchor="w",
        )
        title_label.pack(side=tk.LEFT)

        # History log toggle button
        self.history_btn = tk.Button(
            header_frame,
            text="History",
            font=("Segoe UI", 9, "bold"),
            fg=self.TEXT_SECONDARY,
            bg=self.BG_MAIN,
            activebackground=self.BTN_NUM_HOVER,
            activeforeground=self.TEXT_PRIMARY,
            bd=0,
            cursor="hand2",
            command=self._toggle_history_window,
        )
        self.history_btn.pack(side=tk.RIGHT)

        # Screen display frame container
        display_frame = tk.Frame(self, bg=self.BG_DISPLAY, bd=0, highlightthickness=1, highlightbackground="#313244")
        display_frame.pack(fill=tk.X, padx=16, pady=8, ipady=8)

        # Upper small label for showing expression progress
        self.expr_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 11),
            fg=self.TEXT_SECONDARY,
            bg=self.BG_DISPLAY,
            anchor="e",
            padx=12,
        )
        self.expr_label.pack(fill=tk.X)

        # Main prominent numerical result display label
        self.display_label = tk.Label(
            display_frame,
            text="0",
            font=("Segoe UI", 28, "bold"),
            fg=self.TEXT_PRIMARY,
            bg=self.BG_DISPLAY,
            anchor="e",
            padx=12,
        )
        self.display_label.pack(fill=tk.X)

        # Main button grid container
        btn_frame = tk.Frame(self, bg=self.BG_MAIN)
        btn_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=(4, 16))

        # Configure responsive grid weights
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        # Grid button configuration list: (Label text, Row, Col, Category, Lambda Callback)
        button_specs = [
            ("%", 0, 0, "fn", lambda: self._on_percent()),
            ("CE", 0, 1, "clear", lambda: self._on_clear_entry()),
            ("C", 0, 2, "clear", lambda: self._on_clear_all()),
            ("DEL", 0, 3, "fn", lambda: self._on_backspace()),
            ("1/x", 1, 0, "fn", lambda: self._on_reciprocal()),
            ("x2", 1, 1, "fn", lambda: self._on_square()),
            ("sqrt", 1, 2, "fn", lambda: self._on_sqrt()),
            ("/", 1, 3, "op", lambda: self._on_operator("/")),
            ("7", 2, 0, "num", lambda: self._on_digit("7")),
            ("8", 2, 1, "num", lambda: self._on_digit("8")),
            ("9", 2, 2, "num", lambda: self._on_digit("9")),
            ("*", 2, 3, "op", lambda: self._on_operator("*")),
            ("4", 3, 0, "num", lambda: self._on_digit("4")),
            ("5", 3, 1, "num", lambda: self._on_digit("5")),
            ("6", 3, 2, "num", lambda: self._on_digit("6")),
            ("-", 3, 3, "op", lambda: self._on_operator("-")),
            ("1", 4, 0, "num", lambda: self._on_digit("1")),
            ("2", 4, 1, "num", lambda: self._on_digit("2")),
            ("3", 4, 2, "num", lambda: self._on_digit("3")),
            ("+", 4, 3, "op", lambda: self._on_operator("+")),
            ("+/-", 5, 0, "num", lambda: self._on_negate()),
            ("0", 5, 1, "num", lambda: self._on_digit("0")),
            (".", 5, 2, "num", lambda: self._on_digit(".")),
            ("=", 5, 3, "eq", lambda: self._on_equals()),
        ]

        # Dynamically instantiate and place each button in the layout grid
        self.buttons = {}
        for text, row, col, category, cmd in button_specs:
            btn = self._create_button(btn_frame, text, category, cmd)
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            self.buttons[text] = btn

    def _create_button(self, parent, text, category, command):
        """Helper method to construct a styled button widget based on category."""
        if category == "num":
            bg, fg, hover = self.BTN_NUM_BG, self.BTN_NUM_FG, self.BTN_NUM_HOVER
            font = ("Segoe UI", 14, "bold")
        elif category == "op":
            bg, fg, hover = self.BTN_OP_BG, self.BTN_OP_FG, self.BTN_OP_HOVER
            font = ("Segoe UI", 16, "bold")
        elif category == "eq":
            bg, fg, hover = self.BTN_EQ_BG, self.BTN_EQ_FG, self.BTN_EQ_HOVER
            font = ("Segoe UI", 16, "bold")
        elif category == "clear":
            bg, fg, hover = self.BTN_CLEAR_BG, self.BTN_CLEAR_FG, self.BTN_CLEAR_HOVER
            font = ("Segoe UI", 12, "bold")
        else:
            bg, fg, hover = self.BTN_FN_BG, self.BTN_FN_FG, self.BTN_FN_HOVER
            font = ("Segoe UI", 11, "bold")

        # Create button widget
        btn = tk.Button(
            parent,
            text=text,
            font=font,
            bg=bg,
            fg=fg,
            activebackground=hover,
            activeforeground=fg,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=command,
        )

        # Attach hover effect events
        btn.bind("<Enter>", lambda e, b=btn, h=hover: b.configure(bg=h))
        btn.bind("<Leave>", lambda e, b=btn, c=bg: b.configure(bg=c))

        return btn

    def _bind_keys(self):
        """Bind physical keyboard input events to calculator functions."""
        self.bind("<Key>", self._on_key_press)
        self.bind("<Return>", lambda e: self._on_equals())
        self.bind("<BackSpace>", lambda e: self._on_backspace())
        self.bind("<Escape>", lambda e: self._on_clear_all())

    def _on_key_press(self, event):
        """Route typed characters to corresponding handler methods."""
        char = event.char
        if char in "0123456789.":
            self._on_digit(char)
        elif char in "+-*/":
            self._on_operator(char)
        elif char == "=":
            self._on_equals()
        elif char == "%":
            self._on_percent()

    def _update_display(self):
        """Refresh display labels with current state values."""
        # Truncate or format extremely long output text
        if len(self.current_input) > 14:
            try:
                val = float(self.current_input)
                formatted = f"{val:.8g}"
            except ValueError:
                formatted = self.current_input
        else:
            formatted = self.current_input

        # Update label content
        self.display_label.config(text=formatted)
        self.expr_label.config(text=self.expression)

    def _on_digit(self, char):
        """Handle numeric digit and decimal point button inputs."""
        if self.new_input_start:
            if char == ".":
                self.current_input = "0."
            else:
                self.current_input = char
            self.new_input_start = False
        else:
            if char == "." and "." in self.current_input:
                return  # Prevent multiple decimal points
            if self.current_input == "0" and char != ".":
                self.current_input = char
            else:
                self.current_input += char

        self._update_display()

    def _on_operator(self, op):
        """Handle operational (+, -, *, /) button inputs."""
        try:
            num = float(self.current_input)
        except ValueError:
            return

        # Perform intermediate calculation if operator chaining occurs
        if self.previous_result is not None and not self.new_input_start:
            self._compute_intermediate()

        self.previous_result = float(self.current_input)
        self.pending_operator = op
        self.expression = f"{self._format_num(self.previous_result)} {op}"
        self.new_input_start = True
        self._update_display()

    def _compute_intermediate(self):
        """Evaluate ongoing intermediate operator state."""
        if self.previous_result is None or self.pending_operator is None:
            return

        try:
            current_num = float(self.current_input)
            res = self._execute_calculator_func(self.previous_result, self.pending_operator, current_num)

            if res is None:
                self.current_input = "Error"
                self.previous_result = None
                self.pending_operator = None
            else:
                self.current_input = self._format_num(res)
                self.previous_result = res
        except Exception:
            self.current_input = "Error"
            self.previous_result = None
            self.pending_operator = None

    def _execute_calculator_func(self, num1, op, num2):
        """Delegate mathematical execution to calculator module functions."""
        if op == "+":
            return calculator.add(num1, num2)
        elif op == "-":
            return calculator.sub(num1, num2)
        elif op == "*":
            return calculator.mult(num1, num2)
        elif op == "/":
            try:
                return calculator.div(num1, num2)
            except ZeroDivisionError:
                return None
        return num2

    def _on_equals(self):
        """Evaluate current math expression when Equals (=) is selected."""
        if self.pending_operator is None or self.previous_result is None:
            return

        try:
            second_num = float(self.current_input)
            res = self._execute_calculator_func(self.previous_result, self.pending_operator, second_num)

            if res is None:
                self.expression = f"{self._format_num(self.previous_result)} {self.pending_operator} {self._format_num(second_num)} ="
                self.current_input = "Cannot divide by 0"
                self.history.append(f"{self.expression} Error")
            else:
                formatted_res = self._format_num(res)
                self.expression = f"{self._format_num(self.previous_result)} {self.pending_operator} {self._format_num(second_num)} ="
                self.history.append(f"{self.expression} {formatted_res}")
                self.current_input = formatted_res

            # Reset operational states for next expression
            self.previous_result = None
            self.pending_operator = None
            self.new_input_start = True
            self._update_display()
        except Exception:
            self.current_input = "Error"
            self.new_input_start = True
            self._update_display()

    def _on_clear_all(self):
        """Reset calculator completely (C button)."""
        self.current_input = "0"
        self.expression = ""
        self.previous_result = None
        self.pending_operator = None
        self.new_input_start = True
        self._update_display()

    def _on_clear_entry(self):
        """Reset current input entry only (CE button)."""
        self.current_input = "0"
        self.new_input_start = True
        self._update_display()

    def _on_backspace(self):
        """Remove last entered character from display string."""
        if self.new_input_start or self.current_input in ("0", "Error", "Cannot divide by 0"):
            return
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
            self.new_input_start = True
        self._update_display()

    def _on_negate(self):
        """Toggle positive/negative sign (+/- button)."""
        if self.current_input in ("0", "Error", "Cannot divide by 0"):
            return
        if self.current_input.startswith("-"):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = "-" + self.current_input
        self._update_display()

    def _on_percent(self):
        """Convert current input value to percentage value."""
        try:
            val = float(self.current_input) / 100.0
            self.current_input = self._format_num(val)
            self._update_display()
        except ValueError:
            pass

    def _on_square(self):
        """Square the current display number (x^2)."""
        try:
            val = float(self.current_input)
            res = val ** 2
            self.expression = f"sqr({self._format_num(val)})"
            self.current_input = self._format_num(res)
            self.new_input_start = True
            self._update_display()
        except ValueError:
            pass

    def _on_sqrt(self):
        """Compute square root of display number."""
        try:
            val = float(self.current_input)
            if val < 0:
                self.current_input = "Invalid input"
            else:
                res = math.sqrt(val)
                self.expression = f"sqrt({self._format_num(val)})"
                self.current_input = self._format_num(res)
            self.new_input_start = True
            self._update_display()
        except ValueError:
            pass

    def _on_reciprocal(self):
        """Compute reciprocal (1/x) of display number."""
        try:
            val = float(self.current_input)
            if val == 0:
                self.current_input = "Cannot divide by 0"
            else:
                res = 1 / val
                self.expression = f"1/({self._format_num(val)})"
                self.current_input = self._format_num(res)
            self.new_input_start = True
            self._update_display()
        except ValueError:
            pass

    def _format_num(self, num):
        """Format numbers to omit unnecessary trailing decimal zeroes."""
        if isinstance(num, (int, float)):
            if abs(num - round(num)) < 1e-10:
                return str(int(round(num)))
            return f"{num:.8g}"
        return str(num)

    def _toggle_history_window(self):
        """Open a secondary modal window displaying calculation history log."""
        hist_win = tk.Toplevel(self)
        hist_win.title("Calculation History")
        hist_win.geometry("300x400")
        hist_win.configure(bg=self.BG_MAIN)

        title = tk.Label(
            hist_win,
            text="HISTORY LOG",
            font=("Segoe UI", 11, "bold"),
            fg=self.TEXT_PRIMARY,
            bg=self.BG_MAIN,
            py=10,
        )
        title.pack()

        listbox = tk.Listbox(
            hist_win,
            bg=self.BG_DISPLAY,
            fg=self.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            selectbackground=self.BTN_NUM_HOVER,
            bd=0,
            highlightthickness=0,
        )
        listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        if not self.history:
            listbox.insert(tk.END, "No history yet.")
        else:
            for item in reversed(self.history):
                listbox.insert(tk.END, item)


if __name__ == "__main__":
    app = ModernCalculatorGUI()
    app.mainloop()
