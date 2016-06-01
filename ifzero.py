def main():
    num1 = 1
    pos = 0
    neg = 0
    total = 0
    count = -1
    while num1 != 0:
        num1 = eval(input("Enter an integer, the input ends if it is 0: "))
        if num1 > 0:
            pos += 1
        if num1 < 0:
            neg += 1
        total += num1
        count += 1
    mean = total / count
    
    print ("The number of positives is", pos)
    print ("The number of negatives is", neg)
    print ("The total is", total)
    print ("The average is", mean)
main()
