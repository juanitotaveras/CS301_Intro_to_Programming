def main():
    day = eval(input("Enter today's day: "))
    elapsed = eval(input("Enter the number of days elapsed since today: "))
    future = day + (elapsed % 7)
    if day == 0:
        day = 'Sunday'
    elif day == 1:
        day = 'Monday'
    elif day == 2:
        day = 'Tuesday'
    elif day == 3:
        day = 'Wednesday'
    elif day == 4:
        day = 'Thursday'
    elif day == 5:
        day = 'Friday'
    elif day == 6:
        day = 'Saturday'
    if future == 0:
        future = 'Sunday'
    elif future == 1:
        future = 'Monday'
    elif future == 2:
        future = 'Tuesday'
    elif future == 3:
        future = 'Wednesday'
    elif future == 4:
        future = 'Thursday'
    elif future == 5:
        future = 'Friday'
    elif future == 6:
        future = 'Saturday'

    print ('Today is', day, 'and the future day is', future)
main()
