# TO find out the Average Height of the student
# 156 178 165 171 187
students_height=input("Input a list of students height.").split()
for n in range (0, len(students_height)):
 students_height[n]=int(students_height[n])
print(students_height)

total_height= 0
for height in students_height:
 total_height+=height
print(f"The total height of the student is {total_height}")

number_of_student=0
for student in students_height:
 number_of_student+=1
print(f"The number of students are {number_of_student}")

average_height=round(total_height/number_of_student)
print(f"The average height is {average_height}")