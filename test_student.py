import pytest
from student import Student  # Replace with actual file/module name

@pytest.fixture
def student():
    """Fixture to create a Student instance."""
    return Student("John Doe")

def test_add_grade(student):
    student.add_grade(90)
    assert student.grades == [90]

    student.add_grade(85)
    assert student.grades == [90, 85]

    with pytest.raises(ValueError):
        student.add_grade(150)

def test_average_grade(student):
    assert student.average_grade() == 0  # No grades yet
    student.add_grade(90)
    student.add_grade(80)
    assert student.average_grade() == 85

def test_grade_letter(student):
    student.add_grade(95)
    assert student.grade_letter() == 'A'

    student.grades = [80, 85]
    assert student.grade_letter() == 'B'
