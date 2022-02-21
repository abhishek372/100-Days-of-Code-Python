# Program to print the grade of the student marks 

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Neville": 62,
    "Hermine": 99,
}

# Empty dictionary
student_grades = {}

# Checks for every key in student
for student in student_scores:
    score = student_scores[student]
    if score>=91 and score<=100:
        grades = "Outstanding"
        student_grades[student] = grades
    elif score>=81 and score<=90:
        grades = "Exceeds Expectations"
        student_grades[student] = grades
    elif score>=71 and score<=80:
        grades = "Acceptable"
        student_grades[student] = grades
    elif score<=70:
        grades = "Fail"
        student_grades[student] = grades

print(student_grades)
