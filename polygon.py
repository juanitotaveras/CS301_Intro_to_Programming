import math
def main():
    num_sides = eval(input("Enter the number of sides: "))
    side = eval(input("Enter the side: "))
    area = (num_sides * side ** 2) / (4 * math.tan(math.pi/num_sides))
    print ('The area of the polygon is' , area)
main()
