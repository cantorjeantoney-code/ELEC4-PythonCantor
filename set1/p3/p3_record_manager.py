
# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P3 - Record Manager
# Date: 2026-11-27

students = []
student_keys = set()

def add_student():
    name = input("Student name: ").strip()
    key = name.casefold()

    if not name:
        print("Name cannot be empty.")
    elif key in student_keys:
        print("That student is already in the list.")
    else:
        students.append(name)
        student_keys.add(key)
        print("Student added.")

def remove_student():
    name = input("Name to remove: ").strip()
    key = name.casefold()

    if key not in student_keys:
        print("Student not found.")
        return

    for existing in students:
        if existing.casefold() == key:
            students.remove(existing)
            break

    student_keys.remove(key)
    print("Student removed.")

def search_student():
    query = input("Partial name to search: ").strip().casefold()
    matches = [name for name in students if query in name.casefold()]
    print("\n".join(matches) if matches else "No matching student found.")

def display_students():
    print(f"\nTotal students: {len(students)}")

    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")

def main():
    while True:
        print("\n1. Add\n2. Remove\n3. Search\n4. Display all\n5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting Student Record Manager.")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()

# A list stores the student names in an ordered collection.
# A set stores normalized names to check duplicates efficiently.
# Case-folding treats names with different capitalization as duplicates.
# The list is sorted alphabetically when displaying students.
