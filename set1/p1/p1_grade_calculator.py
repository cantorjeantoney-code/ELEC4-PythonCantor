
# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-25

def enter_grades():
    grades = []

    while len(grades) < 5:
        try:
            grade = float(input("Enter a grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return grades


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    if compute_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


def show_results(grades):
    if not grades:
        print("No grades yet. Choose option 1 first.")
        return

    print("\n--- GRADE REPORT ---")
    print(f"Grades: {grades}")
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")


def main():
    grades = []

    while True:
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            show_results(grades)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()


# A local variable is created inside a function
# and can only be used within that function.
#
# A global variable is defined outside functions
# and can be accessed throughout the module.
#
# This program passes the grades list as a parameter
# instead of using a global variable.
