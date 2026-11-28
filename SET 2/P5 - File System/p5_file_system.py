
# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P5 - File System
# Date: 2026-11-27

FILENAME = "students.txt"
MIN_STUDENTS = 5


def load_students():
    students = []

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 4:
                    student = {
                        "id": parts[0],
                        "name": parts[1],
                        "course": parts[2],
                        "average": parts[3]
                    }
                    students.append(student)

    except FileNotFoundError:
        print("No existing records found. Starting with an empty list.")

    return students


def save_students(students):
    with open(FILENAME, "w") as file:
        for student in students:
            file.write(
                f"{student['id']}|{student['name']}|"
                f"{student['course']}|{student['average']}\n"
            )


def check_student_count(students):
    total = len(students)

    print("\n===== STUDENT RECORD CHECK =====")
    print("Total Students:", total)

    if total < MIN_STUDENTS:
        remaining = MIN_STUDENTS - total
        print("WARNING: You need at least 5 student records.")
        print("You still need to add", remaining, "more student(s).")
    else:
        print("SUCCESS: You have at least 5 student records.")


def add_student(students):
    print("\n===== ADD STUDENT =====")

    student_id = input("Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return

    name = input("Full Name: ").strip()
    course = input("Course/Section: ").strip()

    if not name or not course or "|" in name or "|" in course:
        print("Invalid or empty student information.")
        return

    try:
        average = float(input("General Average: "))

        if not 0 <= average <= 100:
            print("Average must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid input. Please enter a numeric average.")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "average": str(average)
    }

    students.append(student)
    save_students(students)

    print("Student record added successfully!")
    check_student_count(students)


def display_students(students):
    print("\n===== ALL STUDENT RECORDS =====")

    if not students:
        print("No student records available.")
        check_student_count(students)
        return

    for student in students:
        print("-----------------------------")
        print("Student ID:", student["id"])
        print("Full Name:", student["name"])
        print("Course/Section:", student["course"])
        print("General Average:", student["average"])

    check_student_count(students)


def search_student(students):
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Full Name:", student["name"])
            print("Course/Section:", student["course"])
            print("General Average:", student["average"])
            return

    print("Student record not found.")


def update_student(students):
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("Leave a field blank to keep its current value.")

            name = input("New Full Name: ").strip()
            course = input("New Course/Section: ").strip()
            average_input = input("New General Average: ").strip()

            if name:
                if "|" in name:
                    print("Invalid name.")
                    return
                student["name"] = name

            if course:
                if "|" in course:
                    print("Invalid course/section.")
                    return
                student["course"] = course

            if average_input:
                try:
                    average = float(average_input)

                    if not 0 <= average <= 100:
                        print("Average must be between 0 and 100.")
                        return

                    student["average"] = str(average)

                except ValueError:
                    print("Invalid input. Please enter a numeric average.")
                    return

            save_students(students)
            print("Student record updated successfully!")
            return

    print("Student record not found.")


def main():
    students = load_students()

    check_student_count(students)

    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            check_student_count(students)
            print("Thank you for using Student Record System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
