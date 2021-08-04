import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("Johann", "Alberts")
        self.assertEqual(student.full_name, "Johann Alberts")

    def test_alert_santa(self):
        student = Student("Draco", "Malfoy")
        student.alert_santa()
        self.assertTrue(student.naughty_list)

    def test_student_email(self):
        student = Student("Harry", "Potter")
        self.assertEqual(student.email(), "harry.potter@hogwarts.com")


if __name__ == "__main__":
    unittest.main()
