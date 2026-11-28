# Name: JEAN TONEY S. CANTOR
# Section: IV-BSIT-A
# Activity: P2 - Student Utils Module
# Date: 2026-11-27

def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_pass_fail(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
