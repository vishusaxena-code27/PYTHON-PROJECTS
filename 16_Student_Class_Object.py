# Create a class
class Student:

    # Function to store student details
    def set_details(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Function to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Create object
student = Student()

# Take input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))

# Store details
student.set_details(name, roll_no, marks)

# Display details
student.display_details()