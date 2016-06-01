#Have user input number of minutes and convert/output that in years and days
def main():
    minutes = int(input("Enter the number of minutes: "))
    years = minutes // (60 * 24 * 365)
# Days must be total minutes minus years times minutes then divided by number min in days
    days = (minutes - (years * (60 * 24 * 365))) // (60 * 24)
    print (minutes, "minutes is approximately" , years, "years and", days, "days")
main()

