class Class:

    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return round(float(sum(self.grades) / len(self.grades)), 2)

    def __repr__(self):
        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}'
