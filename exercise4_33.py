def main():
    num = eval(input("Enter a decimal value (0 to 15): "))
    if 0 < num < 15:
        num = hex(num).upper()
        print ("The hex value is", num[2:7])
    else:
        print ("Invalid input")
main()
