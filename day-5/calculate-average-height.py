students_height=input("Input a list of students height: ").split()

for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)


sum=0
count=0

for height in students_height:
  sum += height
  count +=1

average_height=round(sum/count)

print(f"the average height of class is {average_height}")