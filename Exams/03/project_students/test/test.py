from project_students.student_report_card import StudentReportCard

from unittest import TestCase, main

class TestStudent_report(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard('Ivan', 5)

    def test_init(self):
        student = StudentReportCard('Ivan', 1)

        self.assertEqual('Ivan', student.student_name)
        self.assertEqual(1, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_name_setter(self):
        name = ""

        with self.assertRaises(ValueError) as ex:
            StudentReportCard(name, 5)
        self.assertEqual('Student Name cannot be an empty string!', str(ex.exception))

    def test_year_setter(self):
        year = 13
        with self.assertRaises(ValueError) as ex:
            StudentReportCard('Ivan', year)
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_year_setter_1(self):
        year = 0
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard('Ivan', year)
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_year_setter_2(self):
        year = 12
        student = StudentReportCard('Ivan', year)

        self.assertEqual(12, student.school_year)

    def test_add_grade(self):
        grades_by_subject = {}
        grades_by_subject['Math'] = 4.50
        result = self.student.add_grade('Math', 4.50)

        self.assertEqual({'Math': [4.50]}, self.student.grades_by_subject)
        self.assertTrue('Math' in self.student.grades_by_subject)

    def test_add_grade_1(self):
        grades_by_subject = {'Math': [4.50]}
        self.student.add_grade('Math', 4.50)
        result = self.student.add_grade('Math', 5.50)

        self.assertEqual({'Math': [4.50, 5.50]}, self.student.grades_by_subject)
        self.assertTrue(5.50 in self.student.grades_by_subject['Math'])

    def test_average_grade_by_subject(self):
        grades_by_subject = {'Math': [4.50, 5.50]}
        result = f'Math: 5.00'
        self.student.add_grade('Math', 4.50)
        self.student.add_grade('Math', 5.50)

        self.assertEqual(result, self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        grades_by_subject = {'Math': [4.50, 5.50], 'History': [6.00, 6.00]}
        result = f"Average Grade: 5.50"
        self.student.add_grade('Math', 4.50)
        self.student.add_grade('Math', 5.50)
        self.student.add_grade('History', 6.00)
        self.student.add_grade('History', 6.00)

        self.assertEqual(result, self.student.average_grade_for_all_subjects())

    def test_repr_(self):
        grades_by_subject = {'Math': [4.50, 5.50], 'History': [6.00, 6.00]}
        result = 'Name: Ivan\n' \
                 'Year: 5\n' \
                 '----------\n'\
                 'Math: 5.00\n'\
                 'History: 6.00\n'\
                 '----------\n'\
                 'Average Grade: 5.50'

        self.student.add_grade('Math', 4.50)
        self.student.add_grade('Math', 5.50)
        self.student.add_grade('History', 6.00)
        self.student.add_grade('History', 6.00)

        self.assertEqual(result, self.student.__repr__())


if __name__ == "__main__":
    main()
