def main():
    x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))
    a = y1 - y2
    b = -(x1 - x2)
    c = y3 - y4
    d = -(x3 - x4)
    e = x1*a + y1*b
    f = x3*c + y3*d
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    if (a*d - b*c) == 0:
        print ("The two lines are parallel")
    else:
        print ("The intersecting point is at", (x, y))
main()  
