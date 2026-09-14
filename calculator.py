"""
Calculator Core Operations Module

This module provides basic arithmetic operations including addition, subtraction,
multiplication, and division with error handling for division by zero.
"""

def add(a: float, b: float) -> float:
    """
    Calculate the sum of two numbers.

    Parameters:
        a (float): First addend.
        b (float): Second addend.

    Returns:
        float: The sum of a and b.
    """
    # Perform standard addition
    return a + b


def sub(a: float, b: float) -> float:
    """
    Calculate the difference between two numbers.

    Parameters:
        a (float): Minuend.
        b (float): Subtrahend.

    Returns:
        float: The difference (a - b).
    """
    # Perform standard subtraction
    return a - b


def mult(a: float, b: float) -> float:
    """
    Calculate the product of two numbers.

    Parameters:
        a (float): First factor.
        b (float): Second factor.

    Returns:
        float: The product of a and b.
    """
    # Multiply the two input values
    return a * b


def div(a: float, b: float) -> float:
    """
    Calculate the quotient of two numbers.

    Parameters:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        float: The quotient (a / b).

    Raises:
        ZeroDivisionError: If the divisor b is zero.
    """
    # Validate that divisor is non-zero to prevent illegal arithmetic
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    # Perform standard float division
    return a / b
