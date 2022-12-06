# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #set the variable to integer

exam_three = int(input("Input exam grade three: ")) #changed the variable type from str to int and corrected the variable name

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in range(len(grades)): #added the range funtion and set logic loop
  sum = sum + grades[grade] #corrected the operation

avg = sum // len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #put correct quotation
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: #changed elif to else
    letter_grade = "F"

#for grade in grades:  removed the loop and corrected the syntax
print(f'Exams: {grades[0]}, {grades[1]}, {grades[2]}') #getting each element the grades list

print("Average: " +str(avg))

print("Grade: " + letter_grade)

if letter_grade is "F": #corrected the variable name
    print ("Student is failing.") #added brackets
else:
    print ("Student is passing.") #added brackets
