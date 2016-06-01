def main():
    monthly_saving = eval(input("Enter the monthly saving amount: "))
    monthly_interest = 1.00417
    month1 = monthly_saving * monthly_interest
    month2 = (monthly_saving + month1) * monthly_interest
    month3 = (monthly_saving + month2) * monthly_interest
    month4 = (monthly_saving + month3) * monthly_interest
    month5 = (monthly_saving + month4) * monthly_interest
    month6 = (monthly_saving + month5) * monthly_interest
    print (month6)
main()
