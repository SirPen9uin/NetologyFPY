class Student():

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def _avr_grade(self):
        all_grades = []
        for value_list in self.grades.values():
            all_grades.extend(value_list)
        return round(sum(all_grades) / len(all_grades), 1)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за задания: {self._avr_grade()} \nКурсы в процессе обучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._avr_grade() < other._avr_grade()


class Mentor():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def _avr_grade(self):
        all_grades = []
        for value_list in self.grades.values():
            all_grades.extend(value_list)
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._avr_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lector!')
            return
        return self._avr_grade() < other._avr_grade()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def avr_grade_students(students, course):
    all_grades = []
    for student in students:
        if course in student.courses_in_progress:
            all_grades.append(student.grades[course])
    total_sum = 0
    total_el = 0
    for grade in all_grades:
        total_sum += sum(grade)
        total_el += len(grade)

    return round(total_sum/total_el, 1)


def avr_grade_lecturers(lecturers, course):
    all_grades = []
    for lectur in lecturers:
        if course in lectur.courses_attached:
            all_grades.append(lectur.grades[course])
    total_sum = 0
    total_el = 0
    for grade in all_grades:
        total_sum += sum(grade)
        total_el += len(grade)
    return round(total_sum/total_el, 1)

potter = Student('Harry', 'Potter', 'male')
malfoy = Student('Drako', 'Malfoy', 'male')
potter.courses_in_progress.append('Python')
potter.courses_in_progress.append('Git')
malfoy.courses_in_progress.append('Git')
potter.finished_courses.append('Git')
malfoy.finished_courses.append('Python')
snape = Lecturer('Severus', 'Snape')
hagred = Lecturer('Rubeus', 'Hagred')
snape.courses_attached.append('Python')
hagred.courses_attached.append('Git')
dumbledor = Reviewer('Albus', 'Dumbledor')
mcgonagal = Reviewer('Minerva', 'Mcgonagal')
dumbledor.courses_attached.append('Python')
mcgonagal.courses_attached.append('Git')
potter.rate_lecture(snape, 'Python', 7)
potter.rate_lecture(snape, 'Python', 9)
potter.rate_lecture(snape, 'Python', 5)
malfoy.rate_lecture(hagred, 'Git', 6)
malfoy.rate_lecture(hagred, 'Git', 7)
malfoy.rate_lecture(hagred, 'Git', 4)
dumbledor.rate_hw(potter, 'Python', 10)
dumbledor.rate_hw(potter, 'Python', 10)
dumbledor.rate_hw(potter, 'Python', 10)
mcgonagal.rate_hw(potter, 'Git', 9)
mcgonagal.rate_hw(potter, 'Git', 9)
mcgonagal.rate_hw(potter, 'Git', 9)
mcgonagal.rate_hw(malfoy, 'Git', 8)
mcgonagal.rate_hw(malfoy, 'Git', 7)
mcgonagal.rate_hw(malfoy, 'Git', 3)
print(potter)
print(malfoy)
print(snape)
print(hagred)
print(dumbledor)
print(mcgonagal)
students = []
students.append(potter)
students.append(malfoy)
lecturers = []
lecturers.append(snape)
lecturers.append(hagred)
print(avr_grade_students(students, 'Git'))
print(avr_grade_lecturers(lecturers, 'Python'))