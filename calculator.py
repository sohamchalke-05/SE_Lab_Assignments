"""Program of Basic Calculator"""
class Calculator:
    """Basic Operations in Calculator"""
    def add(self, a, b):
        """Adding 2 Values"""
        return a + b

    def subtract(self, a, b):
        """Subtracting 2 Values"""
        return a - b

    def multiply(self, a, b):
        """Multiplying 2 Values"""
        return a * b

    def divide(self, a, b):
        """Dividing 2 Values"""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
