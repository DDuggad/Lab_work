class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = [0, 0, 0]
        self.total_marks = 0

    def input_details(self):
        self.name = input("Enter the student name: ")
        self.roll_number = input("Enter USN: ")
        self.marks = [int(mark) for mark in input("Enter marks for three subjects: ").split()]
    def calculate_total(self):
        self.total_marks = sum(self.marks)

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks}")
        
student1 = Student()
student1.input_details()
student1.calculate_total()
student1.display_details()
