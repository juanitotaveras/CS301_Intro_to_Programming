def main():
    final = eval(input("Enter final account value: "))
    rate = eval(input("Enter annual interest rate in percent: "))
    years = eval(input("Enter number of years: "))
    initial = (final) / ((1 + (rate / 100) / (12)) ** (12 * years))
    print ("Initial deposit value is" , initial)
main()
