# Testy do kodu szykem2
import unittest

from kol2_gr2 import *


class Students_tests(unittest.TestCase):
    def setUp(self):
        self.name = "testName"
        self.surname = "testSurname"
        self.clas = "testClass"
        self.grades = []
        self.test_instance = Student(self.name, self.surname, self.clas)

    def test_should_init_properly(self):
        self.assertEquals(self.test_instance.name, self.name)
        self.assertEquals(self.test_instance.surname, self.surname)
        self.assertEquals(self.test_instance.clas, self.clas)
        self.assertEquals(self.test_instance.grades, self.grades)

    def test_should_add_grade(self):
        expected_grade = 4
        self.test_instance.add_grade(expected_grade)
        self.assertEquals(len(self.test_instance.grades), 1)
        self.assertIn(expected_grade, self.test_instance.grades)

    def test_should_get_average_for_student(self):
        test_grades = [3, 3, 4, 2]
        expected_average = 3.0
        for x in test_grades: self.test_instance.add_grade(x)
        self.assertEquals(self.test_instance.average(), expected_average)

    def test_should_not_allow_negative_grade(self):
        negative_grade = -2
        self.test_instance.add_grade(negative_grade)
        self.assertNotIn(negative_grade, self.test_instance.grades)

    def test_should_handle_empty_average(self):
        expected_average = 0.0
        self.assertEquals(self.test_instance.average(), expected_average)


class Log_entry_tests(unittest.TestCase):
    def setUp(self):
        test_students = [Student("Szymon", "Kubasiak", "1A"), Student("Tomasz", "Laz", "1A"),
                         Student("Andrzej", "Jakis", "2A"), Student("Ktos", "Jakis", "1A"),
                         Student("Mikolaj", "Cos", "1A"),
                         Student("Kajetan", "Lipensky", "1A")]
        self.test_instance = Student("testName", "testSurname", "testClass")
        self.subject = "testSubject"
        self.present = [test_students[0], test_students[1], test_students[3], test_students[4]]
        self.absent = [test_students[5]]
        self.test_instance = Log_entry(self.subject, self.present, self.absent)

    def test_should_init_properly(self):
        self.assertEquals(self.test_instance.subject, self.subject)
        self.assertEquals(self.test_instance.present, self.present)
        self.assertEquals(self.test_instance.absent, self.absent)


class Log_book_tests(unittest.TestCase):
    def setUp(self):
        self.test_students = [Student("Szymon", "Kubasiak", "1A"), Student("Tomasz", "Laz", "1A"),
                              Student("Andrzej", "Jakis", "2A"), Student("Ktos", "Jakis", "1A"),
                              Student("Mikolaj", "Cos", "1A"),
                              Student("Kajetan", "Lipensky", "1A")]
        self.students = []
        self.entries = []
        self.test_entry = Log_entry("testSubject",
                                    [self.test_students[0], self.test_students[1], self.test_students[3],
                                     self.test_students[4]],
                                    [self.test_students[5]])
        self.test_instance = Log_book(self.test_students)

    def test_should_init_properly(self):
        self.assertEquals(len(self.test_instance.students), 6)
        self.assertEquals(len(self.test_instance.entries), 0)

    def test_should_add_entry(self):
        self.test_instance.add_entry(self.test_entry)
        self.assertIn(self.test_entry, self.test_instance.entries)
        self.assertEquals(len(self.test_instance.entries), 1)

    def test_should_not_add_invalid_entry(self):
        invalid_entry = Student("InvalidS", "InvalidS", "InvalidS")
        self.assertRaises(ValueError, self.test_instance.add_entry, invalid_entry)

    def test_should_get_school_average(self):
        test_grades = [4, 5, 3]
        expected_average = 4.0;
        for x in self.test_students:
            for g in test_grades: x.add_grade(g)

        self.assertEquals(self.test_instance.average(), expected_average)

    def test_should_get_class_average(self):
        class_students = [x for x in self.test_students if x.clas == "1A"]
        test_grades = [4, 5, 3]
        expected_class_average = 4.0
        test_clas = "1A"
        for s in class_students:
            for i in test_grades: s.add_grade(i)

        self.assertEquals(self.test_instance.class_average(test_clas), expected_class_average)

    def test_should_handle_empty_grade_list(self):
        expected_average = 0.0
        self.assertEquals(self.test_instance.average(), expected_average)
        self.assertEquals(self.test_instance.class_average(), expected_average)

    def test_should_not_add_grade_with_all_absent_students(self):
        self.test_entry = Log_entry("testSubject", [],
                                    [self.test_students[0], self.test_students[1], self.test_students[3],
                                     self.test_students[4],
                                     self.test_students[5]])
        self.test_instance = Log_book(self.test_students)
        test_grades = [4, 5, 3]
        expected_average = 0.0;
        for x in self.test_students:
            for g in test_grades: x.add_grade(g)

        self.assertEquals(self.test_instance.average(), expected_average)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
