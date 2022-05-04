from datetime import date
from classes import Student, Specialization, Subject, Group, Exam, ExamPoints, Institute
import unittest

class addStudent_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student('Павлов Вячеслав Июльевич', 185774)
        inst = Institute()
        inst.addStudent(student)
        self.assertEqual(len(inst.students), 1)

    def test_adding_2(self):
        student_1 = Student('Павлов Вячеслав Июльевич', 185774)
        student_2 = Student('Иванов Иван Иванович', 185773)
        inst = Institute()
        inst.addStudent(student_1)
        inst.addStudent(student_2)
        self.assertEqual(len(inst.students), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addStudent(123)
        self.assertEqual(len(inst.students), 0)

    def test_adding_4(self):
        student = Student("Иванов Иван Иванович", 123456)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addStudent(student)
            inst.addStudent(student)
        self.assertEqual(len(inst.students), 1)

    def test_adding_5(self):
        student_1 = Student("Иванов Иван Иванович", 123456)
        student_2 = Student("Прокопьев Иван Иванович", 123456)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addStudent(student_1)
            inst.addStudent(student_2)
        self.assertEqual(len(inst.students), 1)

class addSubject_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization('ФИИТ')
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        inst = Institute()
        inst.addSubject(subject)
        self.assertEqual(len(inst.subjects), 1)

    def test_adding_2(self):
        spec = Specialization('ФИИТ')
        subject_1 = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        subject_2 = Subject("Б1.В.01", "Английский язык", 2, 108, spec)
        inst = Institute()
        inst.addSubject(subject_1)
        inst.addSubject(subject_2)
        self.assertEqual(len(inst.subjects), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addSubject([123])
        self.assertEqual(len(inst.subjects), 0)

    def test_adding_4(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addSubject(subject)
            inst.addSubject(subject)
        self.assertEqual(len(inst.subjects), 1)

    def test_adding_5(self):
        spec = Specialization("ФИИТ")
        spec1 = Specialization("ИВТ")
        subj = Subject("Б1.В.25", "Программная инженерия", 5, 144, spec)
        subj1 = Subject("Б1.В.25", "Программная инженерия", 5, 144, spec1)
        inst = Institute()
        inst.addSubject(subj)
        inst.addSubject(subj1)
        self.assertEqual(len(inst.subjects), 2)

class addGroup_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group)
        self.assertEqual(len(inst.groups), 1)

    def test_adding_2(self):
        spec = Specialization('ФИИТ')
        group_1 = Group("М-ФИИТ-21", 2021, spec)
        group_2 = Group("М-ИВТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group_1)
        inst.addGroup(group_2)
        self.assertEqual(len(inst.groups), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addGroup(123)
        self.assertEqual(len(inst.groups), 0)

    def test_adding_4(self):
        inst = Institute()
        with self.assertRaises(Exception):
            group = Group()
            inst.addGroup(group)
        self.assertEqual(len(inst.groups), 0)

    def test_adding_5(self):
        spec = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addGroup(group)
            inst.addGroup(group)
        self.assertEqual(len(inst.groups), 1)

class addSpecs_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 1)

    def test_adding_2(self):
        spec_1 = Specialization("ФИИТ")
        spec_2 = Specialization("ИВТ")
        inst = Institute()
        inst.addSpecs(spec_1)
        inst.addSpecs(spec_2)
        self.assertEqual(len(inst.specs), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addSpecs(123)
        self.assertEqual(len(inst.specs), 0)

    def test_adding_4(self):
        spec = Specialization("ФИИТ")
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addSpecs(spec)
            inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 1)

    def test_adding_5(self):
        inst = Institute()
        with self.assertRaises(Exception):
            spec = Specialization(12)
            inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 0)

    def test_adding_6(self):
        inst = Institute()
        with self.assertRaises(Exception):
            spec = Specialization("")
            inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 0)

class addExam_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam)
        self.assertEqual(len(inst.exams), 1)

    def test_adding_2(self):
        spec = Specialization("ФИИТ")
        subject_1 = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        subject_2 = Subject("Б1.В.01", "Английский язык", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject_1, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        exam_2 = Exam(subject_2, examDate, "2021-2022", "Иванова Иванна Ивановна")
        inst = Institute()
        inst.addExam(exam_1)
        inst.addExam(exam_2)
        self.assertEqual(len(inst.exams), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(123)
        self.assertEqual(len(inst.exams), 0)

    def test_adding_4(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.25", "Методы тестирования", 1, 144, spec)
        exDate = date(2021, 1, 10)
        exam = Exam(subject, exDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        with self.assertRaises(Exception):
            inst.addExam(exam)
            inst.addExam(exam)
        self.assertEqual(len(inst.exams), 1)

    def test_adding_5(self):
        inst = Institute()
        with self.assertRaises(Exception):
            exDate = date(2018, 1, 10)
            exam = Exam(1, exDate, "2021-2022", "Эверстов Владимир Васильевич")
            inst.addExam(exam)
        self.assertEqual(len(inst.exams), 0)

class addExamResult_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints)
        self.assertEqual(len(inst.exam_results), 1)

    def test_adding_2(self):
        student_1 = Student("Павлов Вячеслав Июльевич", 185774)
        student_2 = Student("Иванов Иван Иванович", 185773)
        examPoints_1 = ExamPoints(student_1, 60, 30)
        examPoints_2 = ExamPoints(student_2, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints_1)
        inst.addExamResult(examPoints_2)
        self.assertEqual(len(inst.exam_results), 2)

    def test_adding_3(self):
        inst = Institute()
        with self.assertRaises(Exception):
            ep = ExamPoints(2, 55, 30)
            inst.addExamResult(ep)
        self.assertEqual(len(inst.exam_results), 0)

    def test_adding_4(self):
        inst = Institute()
        with self.assertRaises(Exception):
            student = Student("Иванов Иван Иванович", 123456)
            exPoint = ExamPoints(student, 55.0, 30)
            inst.addExamResult(exPoint)
        self.assertEqual(len(inst.exam_results), 0)

    def test_adding_5(self):
        inst = Institute()
        with self.assertRaises(Exception):
            student = Student("Иванов Иван Иванович", 123456)
            exPoint = ExamPoints(student, 55, 31.0)
            inst.addExamResult(exPoint)
        self.assertEqual(len(inst.exam_results), 0)

if __name__ == '__main__':
    unittest.main()