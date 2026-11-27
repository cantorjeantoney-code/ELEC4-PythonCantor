# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P2 - Student Utils
# Date: 2026-11-27

import student_utils
from student_utils import determine_pass_fail
from datetime import datetime

grades = []

print("=== STUDENT GRADE CALCULATOR ===")

for i in range(5):
    while True:
        try:
            grade = float(input("Enter grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Invalid input. Please enter a grade from 0 to 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

average = student_utils.calculate_average(grades)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)
result = determine_pass_fail(average)

current_date = datetime.now()

print("\n--- STUDENT GRADE REPORT ---")
print("Generated:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Status: {result}")
