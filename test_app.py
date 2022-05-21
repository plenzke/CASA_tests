import unittest
import argparse
from unittest.mock import patch, call
from io import StringIO
from app import args
from app import add_stud
from app import add_spec
from app import add_group
from app import add_subj
from app import add_exam
from app import add_exam_result

class TestApp(unittest.TestCase):

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        arg = argparse.Namespace(student_name='Pavlov Viacheslav', student_code=123236)
        add_stud(arg)
        self.assertEqual(mock_output.getvalue(),
                         'Student(fio=\'Pavlov Viacheslav\', id=123236)\n')

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_output, mock_input):
        arg = argparse.Namespace(spec_name='ФИИТ')
        add_spec(arg)
        self.assertEqual(mock_output.getvalue(),
                         'Specialization(name=\'ФИИТ\')\n')

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_output, mock_input):
        arg = argparse.Namespace(group_name='М-ФИИТ-21', group_year=2021, group_spec="ФИИТ")
        add_group(arg)
        self.assertEqual(mock_output.getvalue(),
                         'Group(name=\'М-ФИИТ-21\', year=2021, spec=Specialization(name=\''
                         'ФИИТ\'))\n')

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_7(self, mock_output, mock_input):
        arg = argparse.Namespace(id='Б1.В.25', subject_name='Программная инженерия', subject_semester=5, subject_hours=144, subject_spec='ФИИТ')
        add_subj(arg)
        self.assertEqual(mock_output.getvalue(),
                         'Subject(id=\'Б1.В.25\', name=\'Программная инженерия\', semester=5, hours=144, '
                         'spec=Specialization(name=\'ФИИТ\'))\n')

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_9(self, mock_output, mock_input):
        arg = argparse.Namespace(exam_subject='Б1.В.25', exam_date='10.07.2020', exam_year='2020', exam_lecturer='Эверстов В.В.')
        add_exam(arg)
        self.assertEqual(mock_output.getvalue(),
                         'Exam(subject=Subject(id=\'Б1.В.25\', name=\'Программная инженерия\', semester=5, hours=144, '
                         'spec=Specialization(name=\'ФИИТ\')), '
                         'examDate=datetime.date(2020, 7, 10), year=\'2020\', lecturer_fio=\'Эверстов В.В.\')\n')

    @patch('builtins.input', side_effect=args)
    @patch('sys.stdout', new_callable=StringIO)
    def test_11(self, mock_output, mock_input):
        arg = argparse.Namespace(exam_result_student=123456, exam_points=60, exam_result_points=30)
        add_exam_result(arg)
        self.assertEqual(mock_output.getvalue(),
                         'ExamPoints(student=Student(fio=\'Иванов Иван Иванович\', id=123456), Points=60, examPoints=30)\n')