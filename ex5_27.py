def main():
    for i in range(10000, 100001, 10000):
        total = 0
        for j in range(1, 1 + i):
            num = (((-1)**(j + 1))/(2*j - 1))
            total += num
        pi = 4 * total
        print (pi)
main()
                
