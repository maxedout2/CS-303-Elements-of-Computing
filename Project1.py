# File: Project1.py
# Student: Anna Dougharty 
# UT EID: amd5933
# Course Name: CS303E
# 
# Date Created: 3.23.2021
# Date Last Modified: 3.23.2021
# Description of Program: Read in the grades for 7 assignments and find the grade average and course grade for a student.

name = input("Enter the student's name: ")

print("\nHOMEWORKS: ")

def gradecheck(grade):
    if grade <= 10 and grade >=0:
        return True
    else:
        return False
falsegrade = "\tGrade must be in range [0...10]. Try again."

hw1 = int(input("\tEnter HW1 grade: "))
gradecheck(hw1)
while gradecheck(hw1) is False:
    print(falsegrade)
    hw1 = int(input("\tEnter HW1 grade: "))

hw2 = int(input("\tEnter HW2 grade: "))
gradecheck(hw2)
while gradecheck(hw2) is False:
    print(falsegrade)
    hw2 = int(input("\tEnter HW2 grade: "))

hw3 = int(input("\tEnter HW3 grade: "))
gradecheck(hw3)
while gradecheck(hw3) is False:
    print(falsegrade)
    hw3 = int(input("\tEnter HW3 grade: "))

print("\nPROJECTS: ")

def gradecheckp(grade):
    if grade >= 0 and grade <=100:
        return True
    else:
        return False
falsegradep = "\tGrade must be in range [0...100]. Try again."

project1 = int(input("\tEnter Project1 grade: "))
gradecheckp(project1)
while gradecheckp(project1) is False:
    print(falsegradep)
    project1 = int(input("\tEnter Project1 grade: "))

project2 = int(input("\tEnter Project2 grade: "))
gradecheckp(project2)
while gradecheckp(project2) is False:
    print(falsegradep)
    project2 = int(input("\tEnter Project2 grade: "))

print("\nEXAMS: ")

exam1 = int(input("\tEnter Exam1 grade: "))
gradecheckp(exam1)
while gradecheckp(exam1) is False:
    print(falsegradep)
    exam1 = int(input("\tEnter Exam1 grade: "))

exam2 = int(input("\tEnter Exam2 grade: "))
gradecheckp(exam2)
while gradecheckp(exam2) is False:
    print(falsegradep)
    exam2 = int(input("\tEnter Exam2 grade: "))

#Grade report

print("\nGrade report for: ",name)
hwavg = float((hw1+hw2+hw3)/3)*10
print("\tHomework average (30% of grade): ","%.2f"%hwavg)
pavg = float((project1+project2)/2)
print("\tProject average (30% of grade): ","%.2f"%pavg)
exavg = float((exam1+exam2)/2)
print("\tExam average (40% of grade): ","%.2f"%exavg)
totalavg = (hwavg*.3)+(pavg*.3)+(exavg*.4)
print("\tStudent course average: ","%.2f"%totalavg)

if totalavg >=90 and totalavg <=100:
    letter = "A"
elif totalavg >=80 and totalavg <90:
    letter = "B"
elif totalavg >=70 and totalavg <80:
    letter = "C"
elif totalavg >=60 and totalavg <70:
    letter = "D"
elif totalavg >=0 and totalavg <60:
    letter = "F"

print("\tCourse grade (CS303E: Spring, 2021): ",str(letter))
print("\n")

