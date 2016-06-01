def main():
    loan = eval(input("Loan Amount: "))
    years = eval(input("Number of Years: "))
    print ("Interest Rate", end = "    ")
    print ("Monthly Payment", end = "    ")
    print ("Total Payment")
    print()
    interest = 5
    while interest <= 8.000:
        month_interest = interest / 1200
        month_pay = (loan*month_interest / (1 - 1 / (1 + month_interest) ** (years * 12)))*10
        year_pay = month_pay * years * 12
        print (str(round(interest, 3)) + "%", end = "    ")
        print (round(month_pay, 2), end = "    ")
        print (round(year_pay, 2))
        interest += 0.125
main()
