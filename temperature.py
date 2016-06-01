def main():
    temp = int(input("Enter the temperature in Fahrenheit between -58 and 41: "))
    wind = int(input("Enter the wind speed greater than or equal to 2 miles per hour: "))
    if -58 < temp < 41 and wind >= 2:
        chill = 35.74 + (0.6215 * temp) - (35.75 * wind ** 0.16) + (0.4275 * temp * wind ** 0.16)
        print (chill)
    else:
        print ("Enter valid input")
main()
