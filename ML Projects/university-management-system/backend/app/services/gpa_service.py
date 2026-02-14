GRADE_POINTS = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

def calculate_gpa(enrollments):
    total_points = 0
    total_credits = 0

    for e in enrollments:
        if e.grade in GRADE_POINTS:
            points = GRADE_POINTS[e.grade] * e.course.credit_hours
            total_points += points
            total_credits += e.course.credit_hours

    return total_points / total_credits if total_credits else 0
