#Testy do kodu szykem2 
import unittest
from kol2_gr2 import *

import math
class StudentTests(unittest.TestCase()):
	def setUp(self):
		self.name = "Test Name"
		self.surname = "Test Surname"
		self.clas = "Test Class 1"
		self.grade = []
		self.test_grade = 4
		self.test_instance = Student(self.name, self.surname, self.clas)		
		
	def should_init_properly_test(self):
		self.assertEqual(self.test_instance.name, self.name)
		self.assertEqual(self.test_instance.surname, self.surname)
		self.assertEqual(self.test_instance.clas, self.clas)
		self.assertEqual(len(self.test_instance.grade)), 0)

	def should_add_grade_test(self):
		self.test_instance.add_grade(self.test_grade)
		self.assertEqual(len(self.test_instance.grade), 1)
		self.assertIn(self.test_grade, self.test_insatnce.grade)
		
	def should_get_average_score_test(self):
		test_instance.add_grade(3)
		self.assertEqual(test_instance.average(), 3.5)
		
class Log_entry(unittest.TestCase()):
	def setUp(self):
		students = []
		students.append(Student("Szymon", "Kubasiak", "1A"))
		students.append(Student("Tomasz", "Laz", "1A"))
		students.append(Student("Andrzej", "Jakis", "2A"))
		students.append(Student("Ktos", "Jakis", "1A"))
		self.subject = "Test Subject"
		self.present = [students[0], students[1]]
		self.absent = [students[2], students[3]]
		self.test_instance = Log_entry(self.subject, self.presnt, self.absent)
		
	def should_init_properly(self):
		self.assertEqual(self.test_instance.subject, self.subject)
		self.assertEqual(self.test_instance.present, self.present)
		self.assertEqual(self.test_instance.absent, self.absent)
		
	def should_return_str_test(self):
		self.assertEqual(str(self.test_instance), "Test Subject ")
		