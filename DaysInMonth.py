# File: DaysInMonth.py
# Student: Anna Dougharty
# UT EID: amd5933
# Course Name: CS303E
# 
# Date Created: 2.26.21
# Date Last Modified: 2.26.21
# Description of Program: Enter a year and month to find out how many days are in the month

year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

days = 0
name = ""

if month == 1:
    name = "January"
    days = 31
if month == 2:
    name = "February"
    if year%4 == 0:
        days = 29
    else:
        days = 28
if month == 3:
    name = "March"
    days = 31
if month == 4:
    name = "April"
    days = 30
if month == 5:
    name = "May"
    days = 31
if month == 6:
    name = "June"
    days = 30
if month == 7:
    name = "July"
    days = 31
if month == 8:
    name = "August"
    days = 31
if month == 9:
    name = "September"
    days = 30
if month == 10:
    name = "October"
    days = 31
if month == 11:
    name = "November"
    days = 30
if month == 12:
    name == "December"
    days = 31

print(name,year,"has",days,"days")

