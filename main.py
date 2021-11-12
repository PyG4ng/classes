class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __gpa(self):
        """
        Calculates and return the gpa (Grade Point Average) of the student,
        raise a valueError message if the student has no grades.

        Returns (int): Grade Point Average

        """
        gpa = 0
        if self.grades:
            for grade in self.grades:
                gpa += sum(self.grades.get(grade)) / len(self.grades.get(grade))
            gpa /= len(self.grades)
        else:
            raise ValueError(f"У {self.name} нет оценок")
        return round(gpa, 2)

    def __str__(self):
        a = ", ".join(self.courses_in_progress) if self.courses_in_progress \
            else "Нет курсов в процессе изучения!"

        b = ", ".join(self.finished_courses) if self.finished_courses \
            else "Нет завершенных курсов!"

        return f'Имя: {self.name}\nФамиля: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__gpa()}\n' \
               f'Курсы в процессе изучения: {a}\n' \
               f'Завершенные курсы: {b}'

    def __lt__(self, other):
        """
        Compares two students by they Grade Point Average and return True or
        False, print error message if the student is not an instance of
        the Student class

        Args:
            other: An instance of the Student class

        Returns: True or False

        """
        if not isinstance(other, Student):
            try:
                name = other.name
            except AttributeError:
                name = other
            print(f'Ошибка! {name} не является студентом')
            return
        else:
            return self.__gpa() < other.__gpa()

    def rate_lecturer(self, lecturer, course, grade):
        """
        Rate lecturer on course
        Args:
            lecturer: An instance of Lecturer class
            course:
            grade:

        Returns:

        """
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __gpa(self):
        gpa = 0
        if self.grades:
            for grade in self.grades:
                gpa += sum(self.grades.get(grade)) / len(self.grades.get(grade))
            gpa /= len(self.grades)
        else:
            raise ValueError(f"У {self.name} нет оценок")
        return round(gpa, 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамиля: {self.surname}\n' \
               f'Средняя оценка за лекции: : {self.__gpa()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            try:
                name = other.name
            except AttributeError:
                name = other
            print(f'{name} не является лектором')
            return
        else:
            return self.__gpa() < other.__gpa()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамиля: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def hws_average_point(students, course):
    """
    Calculates and returns the homeworks average point for all students
    on the course, print the name of students not taking the course or students
    not affiliate to the organisation
    Args:
        students (list): List of students
        course (str): Course taken by students

    Returns (int): Homeworks average point for all students on the course

    """
    total_grades = 0
    real_student = 0
    for student in students:
        if isinstance(student,
                      Student) and course in student.courses_in_progress:
            total_grades += sum(student.grades.get(course)) / len(
                student.grades.get(course))
            real_student += 1
        else:
            try:
                name = student.name
                print(f'{name} не проходит курс {course}')
            except AttributeError:
                name = student
                print(f'{name} не является студентом')
    return total_grades / real_student


def lectors_average_point(lecturers, course):
    """
    Calculates and returns the lecturers average point for all lecturers
    on the course, print the name of lecturers not teaching the course or
    lecturers not affiliate to the organisation
    Args:
        lecturers (list): List of lecturers
        course (str): Course taught by lecturers

    Returns (int): lecturers average point

    """
    total_grades = 0
    real_lecturer = 0
    for lecturer in lecturers:
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached:
            total_grades += sum(lecturer.grades.get(course)) / len(
                lecturer.grades.get(course))
            real_lecturer += 1
        else:
            try:
                name = lecturer.name
                print(f'{name} не читает курс {course}')
            except AttributeError:
                name = lecturer
                print(f'{name} не является лектором')
    return total_grades / real_lecturer


if __name__ == '__main__':
    st_marc = Student('Marc', 'Dupon', 'M')
    st_marc.courses_in_progress += ['Python']
    st_marc.courses_in_progress += ['Git']

    st_emily = Student('Emily', 'Duvent', 'F')
    st_emily.courses_in_progress += ['Python']
    st_emily.courses_in_progress += ['Git']

    rv_bob = Reviewer('Bob', 'Smith')
    rv_bob.courses_attached += ['Python']
    rv_bob.courses_attached += ['Git']

    rv_eva = Reviewer('Eva', 'Stallone')
    rv_eva.courses_attached += ['Python']
    rv_eva.courses_attached += ['Git']

    lc_andrey = Lecturer('Andrey', 'Dusoleil')
    lc_andrey.courses_attached += ['Python']
    lc_andrey.courses_attached += ['Git']

    lc_leila = Lecturer('Leila', 'Panamenko')
    lc_leila.courses_attached += ['Python']
    lc_leila.courses_attached += ['Git']

    rv_bob.rate_hw(st_marc, 'Python', 10)
    rv_bob.rate_hw(st_marc, 'Git', 8)
    rv_bob.rate_hw(st_emily, 'Python', 9)
    rv_bob.rate_hw(st_emily, 'Git', 9)

    rv_eva.rate_hw(st_marc, 'Python', 9)
    rv_eva.rate_hw(st_marc, 'Git', 7)
    rv_eva.rate_hw(st_emily, 'Python', 10)
    rv_eva.rate_hw(st_emily, 'Git', 9)

    st_marc.rate_lecturer(lc_andrey, 'Python', 9)
    st_marc.rate_lecturer(lc_andrey, 'Git', 10)
    st_marc.rate_lecturer(lc_leila, 'Python', 10)
    st_marc.rate_lecturer(lc_leila, 'Git', 10)

    st_emily.rate_lecturer(lc_andrey, 'Python', 10)
    st_emily.rate_lecturer(lc_andrey, 'Git', 9)
    st_emily.rate_lecturer(lc_leila, 'Python', 10)
    st_emily.rate_lecturer(lc_leila, 'Git', 9)

    print(st_emily)
    print()
    print(st_marc)
    print()
    print(st_emily > st_marc)
    print()
    print(lc_andrey)
    print()
    print(lc_leila)
    print()
    print(lc_leila > lc_andrey)
    print()
    print('Emily marks', st_emily.grades)
    print('Marc marks', st_marc.grades)
    print()
    print('Python homeworks average point: ',
          hws_average_point([st_marc, st_emily], 'Python'))
    print('Git homeworks average point: ',
          hws_average_point([st_marc, st_emily], 'Git'))
    print()
    print('Andrey marks', lc_andrey.grades)
    print('Leila marks', lc_leila.grades)
    print()
    print('Lecturers average point for Python course',
          lectors_average_point([lc_leila, lc_andrey], 'Python'))
    print('Lecturers average point for Git course',
          lectors_average_point([lc_leila, lc_andrey], 'Git'))
