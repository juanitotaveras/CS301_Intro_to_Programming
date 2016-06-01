def main():
    user_month = eval(input("Enter the month: "))
    user_year = eval(input("Enter the year: "))
    days = 31
    if user_month == 1:
        month = "January"
    elif user_month == 2:
        month = "February"
        if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
            days = 29
        else:
            days = 28
    elif user_month == 3:
        month = "March"
    elif user_month == 4:
        month = "April"
        days = 30
    elif user_month == 5:
        month = "May"
    elif user_month == 6:
        month = "June"
        days = 30
    elif user_month == 7:
        month = "July"
    elif user_month == 8:
        month = "August"
    elif user_month == 9:
        month = "September"
        days = 30
    elif user_month == 10:
        month = "October"
    elif user_month == 11:
        month = "November"
        days = 30
    elif user_month == 12:
        month = "December"
    print (month, user_year, 'has', days, 'days')
main()
