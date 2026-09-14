def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def mult(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def div(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
