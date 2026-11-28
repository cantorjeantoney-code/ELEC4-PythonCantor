# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P6 - Recursion
# Date: 2026-11-27
# Base case: If n is 0, return 1.
# Recursive call: Multiply n by factorial of n - 1.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Base cases: If n is 0, return 0. If n is 1, return 1.
# Recursive call: Add the two previous Fibonacci numbers.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: If n is 0, return 0.
# Recursive call: Add n to the sum of numbers from 1 to n - 1.
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: If the list is empty, return False.
# Recursive call: Search the remaining list for the target.
def search(items, target):
    if len(items) == 0:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


# Main Program
while True:
    print("\n=== RECURSION PROGRAM ===")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Sum of Numbers")
    print("4. Search")
    print("5. Exit")

    choice = input("Choose a function: ")

    if choice == "1":
        try:
            n = int(input("Enter a number: "))

            if n < 0:
                print("Please enter a non-negative number.")
            else:
                print("Factorial:", factorial(n))

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            n = int(input("Enter the number of terms: "))

            if n < 0:
                print("Please enter a non-negative number.")
            else:
                print("Fibonacci sequence:")
                for i in range(n):
                    print(fibonacci(i), end=" ")
                print()

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        try:
            n = int(input("Enter a number: "))

            if n < 0:
                print("Please enter a non-negative number.")
            else:
                print("Sum:", sum_numbers(n))

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "4":
        items = input("Enter list items separated by spaces: ").split()
        target = input("Enter target to search: ")

        result = search(items, target)

        print("Search result:", result)

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
