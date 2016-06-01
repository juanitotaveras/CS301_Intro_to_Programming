#print reverse of entered four-digit integer
def main():
    integer = eval(input("Enter an integer: "))
    num1 = integer // 1000
    num2 = (integer // 100 - (num1 * 10))*10
    num3 = (integer // 10 - num1 * 100 - num2)*100
    num4 = (integer - (num1 * 1000 + num2 * 10 + num3 // 10))*1000
    print(num4+num3+num2+num1)
main()
    
