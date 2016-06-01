def main():
    num = 100
    count = 0
    while num <= 200:
        if ((num % 5 == 0) and (num % 6 != 0)) or ((num % 5 != 0) and (num % 6 == 0)):
            count += 1
            if count < 10:
                print (format(num, "5d"), end = ' ')
            elif count > 10:
                print (format(num, "5d"), end = ' ')
        num += 1
main()

