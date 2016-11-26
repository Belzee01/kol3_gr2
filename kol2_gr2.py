#!/usr/bin/python
from __future__ import division
from random import randint


class Student(object):
    def __init__(self, name, surname, clas):
        self.name = name
        self.surname = surname
        self.clas = clas
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)


class Log_entry(object):
    def __init__(self, subject, present, absent):
        self.subject = subject
        self.present = present
        self.absent = absent

    def __str__(self):
        return self.subject + " " + str(self.present / (self.present + self.absent))


class Log_book(object):
    def __init__(self, students):
        self.students = students
        self.entries = []

    def add_entry(self, entry):
        if not isinstance(entry, Log_entry):
            raise ValueError("Wrong entry type")

        self.entries.append(entry)

    def average(self):
        grades = []
        for student in self.students:
            grades.extend(student.grades)

        return sum(grades) / len(grades)

    def class_average(self, clas):
        grades = []
        for student in self.students:
            if clas == student.clas:
                grades.extend(student.grades)

        return sum(grades) / len(grades)


if __name__ == "__main__":
    students = []
    students.append(Student("Szymon", "Kubasiak", "1A"))
    students.append(Student("Tomasz", "Laz", "1A"))
    students.append(Student("Andrzej", "Jakis", "2A"))
    students.append(Student("Ktos", "Jakis", "1A"))
    students.append(Student("Mikolaj", "Cos", "1A"))
    students.append(Student("Kajetan", "Lipensky", "1A"))

    logbook = Log_book(students)
    logbook.add_entry(Log_entry("Science", [students[0], students[1], students[3], students[4]], [students[5]]))
    for i in range(3):
        for j in range(6):
            students[j].add_grade(randint(1, 6))

    print("School average: " + str(logbook.average()))
    print("1A average: " + str(logbook.class_average("1A")))
    print("2A average: " + str(logbook.class_average("2A")))