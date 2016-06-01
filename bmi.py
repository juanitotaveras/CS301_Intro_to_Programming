def main():
    pounds = eval(input("Enter weight in pounds: "))
    inches = eval(input("Enter height in inches: "))
    kilos = pounds * 0.45359237
    meters = inches * 0.0254
    bmi = kilos / meters ** 2
    print ('BMI is', bmi)
main()
