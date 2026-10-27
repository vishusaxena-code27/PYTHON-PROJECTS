class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("\n----- Student Report -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())
        print("Grade:", self.calculate_grade())


# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks for 5 subjects
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Creating student object
student = Student(name, roll_no, marks)

# Display complete student report
student.display_report()