def main():
    year, day = eval(input("Enter the year and the first week day of the year: "))
    
    for month in range(1, 12 + 1): #for months 1 - 12
        if month == 1:
            print_month = "January " + str(year)
        elif month == 2:
            print_month = "February " + str(year)
        elif month == 3:
            print_month = "March " + str(year)
        elif month == 4:
            print_month = "April " + str(year)
        elif month == 5:
            print_moth =  "May " + str(year)
        elif month == 6:
            print_month = "June " + str(year)
        elif month == 7:
            print_month = "July " + str(year)
        elif month == 8:
            print_month = "August " + str(year)
        elif month == 9:
            print_month = "September " + str(year)
        elif month == 10:
            print_month = "October " + str(year)
        elif month == 11:
            print_month = "November " + str(year)
        elif month == 12:
            print_month = "December " + str(year)
        print (print_month.center(45))
        for hyphen in range(1, 45 + 1): #make line under month
            print("_", end = "")
        print() #skips line
        print_weekdays = ("Sun   Mon   Tue   Wed   Thu   Fri   Sat")
        print(print_weekdays.center(45))
main()
        

'''def main:
    year, first_day = eval(input("Enter the year and first day of the year: "))
    def main():
#prompt user to enter year
    year = eval(input("Enter year between 1900 and 2100: "))
#check year
    while (year < 1900) or (year > 2100):
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
main()'''
