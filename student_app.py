# student.py

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, marks):
        student = Student(roll_no, name, marks)
        self.students.append(student)
        return student

    def get_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def remove_student(self, roll_no):
        student = self.get_student(roll_no)
        if student:
            self.students.remove(student)
            return True
        return False

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(1, "Ravi", 85)
    sms.add_student(2, "Sita", 90)

    for s in sms.students:
        print(s.display())