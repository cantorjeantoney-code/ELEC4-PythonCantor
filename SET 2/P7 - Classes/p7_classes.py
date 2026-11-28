
# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P7 - Classes
# Date: 2026-11-27

# Class 1: Student
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__grade = None
        self.set_grade(grade)

    # Read the private grade
    def get_grade(self):
        return self.__grade

    # Change the private grade with validation
    def set_grade(self, grade):
        try:
            grade = float(grade)

            if 0 <= grade <= 100:
                self.__grade = grade
                return True
            else:
                print("Error: Grade must be between 0 and 100.")
                return False

        except (ValueError, TypeError):
            print("Error: Grade must be a valid number.")
            return False

    # Display student information
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.get_grade())
        print("---------------------------")

    # Update student information
    def update_info(self, name=None, age=None, grade=None):
        if name is not None:
            self.name = name

        if age is not None:
            self.age = age

        if grade is not None:
            self.set_grade(grade)


# Class 2: Subject
class Subject:
    def __init__(self, subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

    def display_subject(self):
        print("Subject:", self.subject_name)
        print("Subject Code:", self.subject_code)


# Class 3: Section
class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    # Add students to the section
    def add_student(self, student):
        self.students.append(student)

    # Display all students in the section
    def list_students(self):
        print("\n========== SCHOOL INFORMATION ==========")
        print("Section:", self.section_name)
        self.subject.display_subject()

        print("\n========== STUDENT LIST ==========")

        for student in self.students:
            student.display_info()


# Create a Subject object
subject1 = Subject("Introduction to Programming", "IT101")

# Create a Section object
section1 = Section("IV-BSIT-A", subject1)

# Create at least three Student objects
student1 = Student("2026001", "Jean Toney Cantor", 20, 90)
student2 = Student("2026002", "Isla Santos", 20, 92)
student3 = Student("2026003", "Alex Reyes", 21, 88)

# Add students to the section
section1.add_student(student1)
section1.add_student(student2)
section1.add_student(student3)

# Update the information of one student
print("Updating student information...")

student1.update_info(
    name="Jean Toney Cantor",
    age=21,
    grade=95
)

# Display all students
section1.list_students()
