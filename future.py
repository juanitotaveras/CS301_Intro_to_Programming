def main():
    investment_amount = eval(input("Enter investment amount: "))
    annual_rate = eval(input("Enter annual interest rate: "))
    years = eval(input("Enter number of years: "))
    accumulated = investment_amount * (1 + annual_rate / 1200) ** (years * 12)
    print ('Accumulated value is' , accumulated)
main()
