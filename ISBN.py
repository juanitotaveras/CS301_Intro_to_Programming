#  File: ISBN.py

#  Description: Program that checks if ISBN is valid

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10/30/2014

#  Date Last Modified: 11/01/2014


#open file for reading and writing
in_file = open ("./isbn.txt", "r") # input file
out_file = open ("./isbnOut.txt", "w") # output file

# making function to output a valid code and write to file (for later use)
def correct(line):
  output = (line + "  valid \n")
  print (output)
  out_file.write (output)

# making function to output a valid code and write to file (for later use)
def incorrect(line):
  output = (line + "  invalid \n")
  print (output)
  out_file.write (output)
  
def main():
  for line in in_file: # read line
    line = line.strip() # remove whitespace before and after
    isbn_num = line # makes new variable
    isbn_num = isbn_num.replace("-", "") # replace hyphens with nothing
    isbn_num = isbn_num.upper() # change num to uppercase
    line = str(line) # makes sure line is string for outputting at end
    da_list = [] # creates list one
    da_list2 = [] # creates list two dd
    if len(isbn_num) == 10: # checks if ten digits
      first_nine = isbn_num[:9]
      last = isbn_num[9]
      if first_nine.isdigit() and (last == "X" or "0" <= last <= "9"):
        for i in range(10): #start creating list 1
          if ("0" <= isbn_num[i] <= "9"):
            int_num = int(isbn_num[i]) # change into integers
            da_list.append(int_num) # create list
          else: # if the last character is 'X',add 10 b/c X represents 10
            da_list.append(10) 
        for i in range(1, len(da_list)):  #calculate partial sum
          da_list[i] = da_list[i - 1] + da_list[i]
        da_list2 = da_list #copy into second list
        for i in range(1, len(da_list2)): # calculate second partial sum
          da_list2[i] = da_list2[i - 1] + da_list2[i]
        if da_list2[9] % 11 == 0: # if partial sum is divisible by 11 then it's valid ISBN
          correct(line)
        else:
          incorrect(line)
      else:
        incorrect(line)
    else:
      incorrect(line)
main()

#close file
in_file.close()
