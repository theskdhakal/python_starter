students_marks=input("Input a list of students marks: ").split()

for n in range(0,len(students_marks)):
    students_marks[n]=int(students_marks[n])
print(students_marks)



highest_marks=0

for mark in students_marks:
    if mark >highest_marks:
        highest_marks=mark
    

print(f"the highest marks is {highest_marks}")