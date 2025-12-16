# Basic oops 
class StudentManagement:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id =  student_id
        self.marks = marks
    
    def display_student_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Id: {self.student_id}")
        print(f"Student Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks < 0 or self.marks > 100:
          return "Enter Invalid marks"
        switch = {
            'A': lambda: "Excellent" if self.marks >= 90 else None,
            'B': lambda: "Very Good" if self.marks >= 80 else None,
            'C': lambda: "Good" if self.marks >= 70 else None,
            'D': lambda: "Average" if self.marks >= 60 else None,
            'E': lambda: "Need Improvment" if self.marks >= 33 else None,
            'F': lambda: "Fail" if self.marks < 33 else None,
        }
        for grade, condition in switch.items():
            if condition():
                return f"{self.name}, your grade is {grade}, keep it up!"
        
name = input("Enter Student name: \n")        
student_id = input("Enter student roll_no: \n")
marks =  int(input("Enter student's marks: \n"))
s1 = StudentManagement(name, student_id, marks)
s1.display_student_details()
print(s1.calculate_grade())
