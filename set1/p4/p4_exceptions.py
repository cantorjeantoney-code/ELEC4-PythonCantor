
# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P4 - Exceptions
# Date: 2026-11-27

def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


def open_file():
    try:
        filename = input("Enter file name: ").strip()

        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)

    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n===== EXCEPTION HANDLER =====")
        print("1. Division")
        print("2. Open File")
        print("3. Exit")

        try:
            choice = input("Choose an option: ").strip()

            if choice == "1":
                division()

            elif choice == "2":
                open_file()

            elif choice == "3":
                print("Exiting program.")
                break

            else:
                print("Invalid menu selection. Please choose 1, 2, or 3.")

        except Exception as error:
            print("An unexpected error occurred:", error)

        finally:
            print("Returning to menu...")


if __name__ == "__main__":
    main()
