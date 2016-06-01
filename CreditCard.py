#  File: CreditCard.py

#  Description: Program in which user enters a credit card number and checks its validity and type of card

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10/20/2014

#  Date Last Modified: 10/20/2014

#Function checks if number is valid
def is_valid (cc_num): 
    if (14 < len(str(cc_num)) < 17): #if number is 15 or 16 digits
        final_sum = 0 
        for i in range (0, 16):
            int(cc_num) #convert back to integer
            di = ((cc_num // 10**i) % 10) #isolates each variable
            if i % 2 == 1: #if position is odd
                di = di * 2 #multiply by 2
                if di > 9: #if digit * 2 has two digits
                    di = (di % 10) + ((di//10)%10) #isolate digits and add them together
            final_sum += di #add it all up
        if (final_sum % 10 == 0): 
            return True
        else:
            print ("Invalid credit card number")
            return False
    else:
        print ("Not a 15 or 16-digit number")
        return False


#Returns type of credit card
def cc_type (cc_num):
    c = str(cc_num)
    if c[0] == '4':
        print ("Valid Visa credit card number")
        return
    if c[0] == '3' and (c[1] == '4' or c[1] == '7'):
        print ("Valid American Express credit card number")
        return
    if c[0] == '6' and ((c[1] == '0' and c[2] == '1' and c[3] == '1') or (c[1] == '4' and c[2] == '4') or (c[1] == '5')):
        print ("Valid Discover credit card number")
        return
    if c[0] == '5' and ('0' <= c[1] <= '5'):
        print ("Valid Mastercard credit card number")
        return
    else:
        print ("Valid credit card number")

#Put it all together
def main():
    ccnum = int(input("Enter a 15 or 16-digit credit card number: ")) 
    if is_valid(ccnum) == True:
        cc_type(ccnum)
main()
