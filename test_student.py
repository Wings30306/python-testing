import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass method")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass method")

    def setUp(self):
        # print("setUp method")
        self.student = Student("John", "Doe")

    # def tearDown(self):
    #     print("tearDown method")

    def test_full_name(self):
        # print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        # print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_student_email(self):
        # print("test_student_email")
        self.assertEqual(self.student.email, "john.doe@hogwarts.com")

    def test_extension(self):
        old_end_date = self.student.end_date
        self.student.extension(30)
        self.assertEqual(
            self.student.end_date,
            old_end_date + timedelta(days=30)
        )


if __name__ == "__main__":
    unittest.main()
