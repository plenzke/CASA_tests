from datetime import date
from classes import Student, Specialization, Subject, Group, Exam, ExamPoints, Institute
import unittest

class getStudent_testcase(unittest.TestCase):
    inst = Institute()

    def test_get_1(self):
        student_1 = Student("Иванов Иван Иванович", 123456)
        self.inst.addStudent(student_1)
        student_2 = self.inst.getStudent(123456)
        self.assertEqual(student_1, student_2)

    def test_get_2(self):
        student_1 = Student("Иванов Иван Иванович", 123456)
        with self.assertRaises(Exception):
            student_2 = self.inst.getStudent("asd")

    def test_get_3(self):
        student_1 = Student("Иванов Иван Иванович", 123456)
        with self.assertRaises(Exception):
            student_2 = self.inst.getStudent(123444)

class getSubject_testcase(unittest.TestCase):
    inst = Institute()

    def test_get_1(self):
        spec = Specialization("ИВТ")
        subject_1 = Subject("Б1.В.25", "Программная инженерия", 5, 144, spec)
        self.inst.addSubject(subject_1)
        subject_2 = self.inst.getSubject("Б1.В.25")
        self.assertEqual(subject_1, subject_2)

    def test_get_2(self):
        spec = Specialization("ИВТ")
        subject_1 = Subject("Б1.В.25", "Программная инженерия", 5, 144, spec)
        with self.assertRaises(Exception):
            subject_2 = self.inst.getSubject(123)

    def test_get_3(self):
        spec = Specialization("ИВТ")
        subject_1 = Subject("Б1.В.25", "Программная инженерия", 5, 144, spec)
        with self.assertRaises(Exception):
            subject_2 = self.inst.getSubject("Б2.В.45")

class getGroup_testcase(unittest.TestCase):
    def test_get_1(self):
        spec = Specialization("ФИИТ")
        group_1 = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group_1)
        group_2 = inst.getGroup("М-ФИИТ-21")
        self.assertEqual(group_1, group_2)

    def test_get_2(self):
        spec = Specialization("ФИИТ")
        group_1 = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group_1)
        with self.assertRaises(Exception):
            group_2 = inst.getGroup(123)

    def test_get_3(self):
        spec = Specialization("ФИИТ")
        group_1 = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group_1)
        with self.assertRaises(Exception):
            group_2 = inst.getGroup("М-ФИИТ-22")

class getSpec_testcase(unittest.TestCase):
    def test_get_1(self):
        spec_1 = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec_1)
        spec_2 = inst.getSpec("ФИИТ")
        self.assertEqual(spec_1, spec_2)

    def test_get_2(self):
        spec_1 = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec_1)
        with self.assertRaises(Exception):
            spec_2 = inst.getSpec(123)

    def test_get_3(self):
        spec_1 = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec_1)
        with self.assertRaises(Exception):
            spec_2 = inst.getSpec("ИВТ")

class getExam_testcase(unittest.TestCase):
    def test_get_1(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam_1)
        exam_2 = inst.getExam("Методы тестирования и верификации программных продуктов", date(2022, 1, 1))
        self.assertEqual(exam_1, exam_2)

    def test_get_2(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam_1)
        with self.assertRaises(Exception):
            exam = inst.getExam(123, date(2022, 1, 1))

    def test_get_3(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam_1)
        with self.assertRaises(Exception):
            exam = inst.getExam("Методы тестирования и верификации программных продуктов", 123)

    def test_get_4(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam_1)
        with self.assertRaises(Exception):
            exam_2 = inst.getExam("Методы тестиров", date(2022, 1, 1))

class getExamPoints_testcase(unittest.TestCase):
    def test_get_1(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints_1 = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints_1)
        examPoints_2 = inst.getExamPoints(185774)
        self.assertEqual(examPoints_1, examPoints_2)

    def test_get_2(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints_1 = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints_1)
        with self.assertRaises(Exception):
            examPoints_2 = inst.getExamPoints("asd")

    def test_get_3(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints_1 = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints_1)
        with self.assertRaises(Exception):
            examPoints_2 = inst.getExamPoints(185777)

if __name__ == '__main__':
    unittest.main()
