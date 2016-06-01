def main():
    tuition = 10000
    year = 0
    while year < 10:
        tuition = tuition + (tuition * 0.05)
        year += 1
    print (round(tuition, 2))

    year2 = 0
    total = 0
    while year2 < 4:
        if year2 != 0:
            tuition = tuition + (tuition * 0.05)
        total += tuition
        year2 += 1  
    print (round(total, 2))
main()

