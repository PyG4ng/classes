def get_gpa(param):
    """
    Calculates and returns the gpa (Grade Point Average) of the instance.
    Raises a valueError message if the instance has no grades.

    Args:
        param: Student/Lecturer instance

    Returns (int): Grade Point Average:

    """
    gpa = 0
    if param.grades:
        for grade in param.grades:
            gpa += sum(param.grades.get(grade)) / len(param.grades.get(grade))
        gpa /= len(param.grades)
    else:
        raise ValueError(f"У {param.name} нет оценок")
    return round(gpa, 2)


def compare(param, other, class_):
    """
    Compares two instances of class_ by they Grade Point Average and returns
    True or False. Prints error message if the one to compare to is not an
    instance of class_ .

    Args:
        param: Instance of class_
        other: An instance of class_
        class_: class. In our case: Student or Lecturer

    Returns: True or False

    """
    if not isinstance(other, class_):
        try:
            name = other.name
        except AttributeError:
            name = other
        print(f'{name} не является участником')
        return
    else:
        return get_gpa(param) < get_gpa(other)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __gpa(self):
        # """
        # Calculates and returns the gpa (Grade Point Average) of a student
        # for all courses.
        # Raises a valueError message if the student has no grades.
        #
        # Returns (int): Grade Point Average
        #
        # """

        # Using function to avoid redundant code
        return get_gpa(self)

        # gpa = 0
        # if self.grades:
        #     for grade in self.grades:
        #         gpa += sum(self.grades.get(grade)) / len(self.grades.get(grade))
        #     gpa /= len(self.grades)
        # else:
        #     raise ValueError(f"У {self.name} нет оценок")
        # return round(gpa, 2)

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
        # """
        # Compares two students by they Grade Point Average and returns True or
        # False. Prints error message if the one to compare to is not an instance
        # of the Student class.
        #
        # Args:
        #     other: An instance of the Student class
        #
        # Returns: True or False
        #
        # """

        # Using function to avoid redundant code
        return compare(self, other, Student)

        # if not isinstance(other, Student):
        #     try:
        #         name = other.name
        #     except AttributeError:
        #         name = other
        #     print(f'Ошибка! {name} не является студентом')
        #     return
        # else:
        #     return self.__gpa() < other.__gpa()

    def rate_lecturer(self, lecturer, course, grade):
        """
        Gives a grade to a lecturer on a course. Will append the grade to a
        list of grades if the lecturer has already a grade on that course.
        Args:
            lecturer: An instance of Lecturer class
            course (str): course teaching by the lecturer
            grade (int): grade value

        Returns: Add course as key and list of grades as value
        to the lecturer.grades dictionary
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
        # """
        # Calculates and returns the gpa (Grade Point Average) of a lecturer
        # for all courses.
        # Raises a valueError message if the lecturer has no grades.
        #
        # Returns (int): Grade Point Average
        # """

        # Using function to avoid redundant code
        return get_gpa(self)

        # gpa = 0
        # if self.grades:
        #     for grade in self.grades:
        #         gpa += sum(self.grades.get(grade)) / len(self.grades.get(grade))
        #     gpa /= len(self.grades)
        # else:
        #     raise ValueError(f"У {self.name} нет оценок")
        # return round(gpa, 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамиля: {self.surname}\n' \
               f'Средняя оценка за лекции: : {self.__gpa()}'

    def __lt__(self, other):
        # """
        # Compares two lecturers by they Grade Point Average and returns True or
        # False. Prints error message if the one to compare to is not an instance
        # of the Lecturer class.
        #
        # Args:
        #     other: An instance of the Lecturer class
        #
        # Returns (bool): True or False
        #
        # """
        # Using function to avoid redundant code
        return compare(self, other, Lecturer)

        # if not isinstance(other, Lecturer):
        #     try:
        #         name = other.name
        #     except AttributeError:
        #         name = other
        #     print(f'{name} не является лектором')
        #     return
        # else:
        #     return self.__gpa() < other.__gpa()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамиля: {self.surname}'

    def rate_hw(self, student, course, grade):
        """
        Gives a grade to a student on a course. Will append the grade to a
        list of grades if the student has already a grade on that course.
        Args:
            student: An instance of Student class
            course (str): Course being taken by the student
            grade (int): grade value

        Returns: Add course as key and list of grades as value
        to the student.grades dictionary
        """
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_point(members, course):
    """
    Calculates and returns average point for all students / lecturers on the
    course. Prints the name of students / lecturers not taking part to the
    course or students..
    Args:
        members (list): List of students / lecturers instances of
        Student / Lecturer class
        course (str): Course taken/taught by students/lecturers

    Returns (int): Average point for all students/lecturers on the course

    """
    total_grades = 0
    real_member = 0
    for member in members:
        if isinstance(member, Student) and course in member.courses_in_progress \
                or isinstance(member,
                              Lecturer) and course in member.courses_attached:
            total_grades += sum(member.grades.get(course)) / len(
                member.grades.get(course))
            real_member += 1
        else:
            try:
                name = member.name
                print(f'{name} не участник курса {course}')
            except AttributeError:
                name = member
                print(f'{name} не является участником данной программы')
    return total_grades / real_member


def hws_average_point(students, course):
    return average_point(students, course)


def lecturers_average_point(lecturers, course):
    return average_point(lecturers, course)


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
    print('Emily > Marc')
    print(st_emily > st_marc)
    print()

    print(lc_andrey)
    print()
    print(lc_leila)
    print()
    print('Leila < Andrey')
    print(lc_leila < lc_andrey)
    print()

    print(rv_bob)
    print()
    print(rv_eva)
    print()

    print('Оценки Emily: ', st_emily.grades)
    print('Оценки Marc: ', st_marc.grades)
    print()
    print('Средняя оценка за дз по курсу Python: ',
          hws_average_point([st_marc, st_emily], 'Python'))
    print('Средняя оценка за дз по курсу Git: ',
          hws_average_point([st_marc, st_emily], 'Git'))
    print()

    print('Оценки Andrey: ', lc_andrey.grades)
    print('Оценки Leila: ', lc_leila.grades)
    print()
    print('Средняя оценка за лекции всех лекторов в рамках курса Python: ',
          lecturers_average_point([lc_leila, lc_andrey], 'Python'))
    print('Средняя оценка за лекции всех лекторов в рамках курса Git: ',
          lecturers_average_point([lc_leila, lc_andrey], 'Git'))
