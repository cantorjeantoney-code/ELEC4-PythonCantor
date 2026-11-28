# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P8 - Inheritance and Polymorphism
# Date: 2026-11-27

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print(f"I am student {self.name}, age {self.age}, taking {self.course}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"I am teacher {self.name}, age {self.age}, teaching {self.subject}.")

def main():
    people = [
        Student("Alex Santos", 20, "BSIT"),
        Teacher("Jordan Reyes", 35, "Programming"),
        Student("Jamie Cruz", 21, "BSIT")
    ]
    for person in people:
        person.introduce()

if __name__ == "__main__":
    main()

# Inheritance is shown when Student and Teacher receive common attributes from Person.
# Both child classes call super().__init__() to initialize the parent's name and age.
# Polymorphism is shown when the same introduce() call produces different output.
# The program stores both child-object types in one list and calls their overridden method.
