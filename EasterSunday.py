# File: EasterSunday.py
# Description: Program that prints Easter Sunday for any year
# Student Name: Juanito Taveras
# Student UT EID: jmt3686
# Course Name: CS 303E
# Unique Number: 52700
# Date Created: 9/19/2014
# Date Last Modified: 9/21/2014

def main():
#prompt user to enter year
#generate day
    y = eval(input("Enter the year: "))
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h)//319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
#n is month
    if n == 4:
        print('In', y , 'Easter Sunday is on' , p , 'April')
    else:
        print('In' , y, 'Easter Sunday is on' , p , 'March')
main()
