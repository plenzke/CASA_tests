from datetime import date
from classes import Student, Specialization, Subject, Group, Exam, ExamPoints
import unittest

class TestCases(unittest.TestCase):
    def testcase_student(self):
        student = Student("Иванов Иван", 185774)
        self.assertEqual("Иванов Иван", student.fio)
        self.assertEqual(185774, student.id)

    def testcase_specialization(self):
        spec = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", spec.name)

    def testcase_group(self):
        spec = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, spec)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(spec, group.spec)
        self.assertEqual(2021, group.year)

    def testcase_subject(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        self.assertEqual("Б1.В.02", subject.id)
        self.assertEqual("Методы тестирования и верификации программных продуктов", subject.name)
        self.assertEqual(2, subject.semester)
        self.assertEqual(108, subject.hours)
        self.assertEqual(spec, subject.spec)

    def testcase_examPoints(self):
        student = Student("Иванов Иван", 185774)
        examPoints = ExamPoints(student, 60, 30)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(60, examPoints.Points)
        self.assertEqual(30, examPoints.examPoints)

    def testcase_exam(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        self.assertEqual(subject, exam.subject)
        self.assertEqual(examDate, exam.examDate)
        self.assertEqual("2021-2022", exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lecturer_fio)

if __name__ == '__main__':
    unittest.main()