import pytest
from calculator import Calculator  # Replace with actual file/module name

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 10) == -10

def test_multiply(calc):
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(0, 100) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(10, 0)
