#  File: Day.py

#  Description: Program in which the user enters the day, month, and year, and it prints out the day of the week for that date.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created: 9/24/14

#  Date Last Modified: 9/26/14

def main():
#prompt user to enter year
    year = eval(input("Enter year between 1900 and 2100: "))
#check year
    while (year <= 1900) or (year >= 2100):
        year = eval(input("Enter year between 1900 and 2100: "))
        month = 0
    if (1900 < year < 2100):
        month = eval(input("Enter month: "))
#check month
        while (month < 1) or (month > 12):
            month = eval(input("Enter month: "))
        if (1 <= month <= 12):
            day = eval(input("Enter day: "))
#adjust
    if month == 1:
        year -= 1
        a = 11
        while (day < 1) or (day > 31):
            day = eval(input("Enter day: "))
#check day for leap year
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            while (day < 1) or (day > 29):
                day = eval(input("Enter day: "))
            if 1 <= day <= 29:
                year -= 1
                a = 12
        else:
            while (day < 1) or (day > 28):
                day = eval(input("Enter day: "))
            if 1 <= day <= 28:
                year -= 1
                a = 12
#adjust for everything else
    else:
        while (day < 1) or (day > 31):
            day = eval(input("Enter day: "))
        a = month - 2
#adjust the other variables
    b = day
    if year < 2000:
        c = year - 1900
        d = 19
    else:
        c = year - 2000
        d = 20
#Compute!
    w = (13 * a - 1)//5
    x = c//4
    y = d//4
    z = w + x + y + b + c - 2 * d
    r = z % 7 #Take care of the negative values of r
    r = (r + 7) % 7
#Match outputted value with correct day
    if r == 0:
        weekday = "Sunday"
    elif r == 1:
        weekday = "Monday"
    elif r == 2:
        weekday = "Tuesday"
    elif r == 3:
        weekday = "Wednesday"
    elif r == 4:
        weekday = "Thursday"
    elif r == 5:
        weekday = "Friday"
    elif r == 6:
        weekday = "Saturday"
#now just print and you're done!
    print ('The day is' , weekday)
main()
    
