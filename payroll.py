def main():
    name = input("Enter employee's name: ")
    hours_worked = eval(input("Enter number of hours worked in a week: "))
    hourly_rate = eval(input("Enter hourly pay rate: "))
    fed_tax = eval(input("Enter federal tax withholding rate: "))
    state_tax = eval(input("Enter state tax withholding rate: "))
    gross_pay = hours_worked * hourly_rate
    total_deduction = gross_pay * fed_tax + gross_pay * state_tax 
    print ('Employee name:', name)
    print ('Hours Worked:', hours_worked)
    print ('Pay Rate: $',hourly_rate)
    print ('Gross Pay: $',gross_pay)
    print ('Deductions:')
    print ('    Federal Withholding (20.0%): $', gross_pay * fed_tax)
    print ('    State Withholding (9.0%): $' , gross_pay * state_tax)
    print ('    Total Deduction: $', total_deduction)
    print ('Net Pay: $', gross_pay - total_deduction)
main()
