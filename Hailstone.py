#  File: Hailstone.py

#  Description: Program that inputs numbers from range into Hailstone sequence and outputs the number with the longest cycle length

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10/9/14

#  Date Last Modified: 10/9/14

def main():
#enter starting and ending numbers in range
    start_num = eval(input("Enter starting number of the range: "))
    end_num = eval(input("Enter ending number of the range: "))
#check if both numbers are positive and starting less than ending
    while (start_num <= 0) or (end_num <= 0) or (start_num >= end_num):
        start_num = eval(input("Enter starting number of the range: "))
        end_num = eval(input("Enter ending number of the range: "))
#Compute
    i = 0
    cycle_length = 0
    max_length = 0
    cur_num = 0
    max_num = 0
    end_num = end_num + 1 #makes end_num actually included in range
    for i in range (start_num, end_num):
        cur_num = i #this is current number going into loop
        while (i > 1): #perform Hailstone computations
            if (i % 2 == 0):
                i = i // 2
            elif (i % 2 == 1):
                i = (3 * i + 1)
        #when i is 1, loop will exit but number tested is still cur_num
            cycle_length += 1 #count how many iterations to get to 1
        if cycle_length >= max_length: #records max number and cycle length
            max_length = cycle_length
            max_num = cur_num
        cycle_length = 0 #resets variable before loop starts again   
    print ("The number", max_num, "has the longest cycle length of", max_length)
main()
