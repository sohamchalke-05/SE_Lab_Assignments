"""Giving Grades of Student"""
class Student:
    """Custome Class to store Grades of Student"""
    def __init__(self, name):
        """Initialize the name and list of grade"""
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Adding Grades of Student"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def average_grade(self):
        """Taking Avearge of Grades"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def grade_letter(self):
        """Giving Grade Letters on the Marks"""
        avg = self.average_grade()
        if avg >= 90:
            return 'A'
        if avg >= 80:
            return 'B'
        if avg >= 70:
            return 'C'
        if avg >= 60:
            return 'D'
        return 'F'
