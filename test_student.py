# test_student.py
import unittest
from student_app import StudentManagementSystem

class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.sms = StudentManagementSystem()

    def test_add_student(self):
        student = self.sms.add_student(1, "Ravi", 85)
        self.assertEqual(student.name, "Ravi")

    def test_get_student(self):
        self.sms.add_student(2, "Sita", 90)
        student = self.sms.get_student(2)
        self.assertIsNotNone(student)
        self.assertEqual(student.marks, 90)

    def test_remove_student(self):
        self.sms.add_student(3, "Kiran", 70)
        result = self.sms.remove_student(3)
        self.assertTrue(result)

    def test_remove_nonexistent_student(self):
        result = self.sms.remove_student(99)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()