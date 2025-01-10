student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_score_db={}

for student in student_scores:
    if 100>= student_scores[student] >=91:
        student_score_db[student]="Outstanding"

    elif 90 >=student_scores[student]>=81:
        student_score_db[student]="Exceeds Expectations"
    elif 80 >=student_scores[student]>=71:
        student_score_db[student]="Acceptable"
    elif student_scores[student] <= 70:
        student_score_db[student]="Fail"

print(student_score_db)