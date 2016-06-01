#  File: Benford.py

#  Description: Program that calculates the frequency of the first digit of every population entry in the U.S. Census.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 11/25/2014

#  Date Last Modified: 11/25/2014

def main():
  pop_num = []                             # create new list
  inFile = open ("./Census_2009.txt", "r") # open file
  

  count = 0
  for line in inFile:                 # for each line in file
    count += 1                        # increase count by one
    line = line.strip()               # remove white space
    word_list = line.split()          # split line into elements in list
    pop_num.append (word_list[-1])    # add last element in list (population number) to list


  pop_freq = {}                # make new dictionary
  for num in pop_num:          # for every number in list of population numbers
    if num[0] not in pop_freq: # if number is not in our dictionary
      pop_freq[num[0]] = 1     # set its frequency to one
    else:                      # if it is
      pop_freq[num[0]] += 1    # add one to its frequency

# output
  print ("Digit  Count  %")     
  for key in sorted(pop_freq):                                    # for every key in our sorted dictionary
    percent = str(round((pop_freq[key]/count * 100), 1))          # calculate percentage of frequency
    value = str(pop_freq[key])                                    # make frequency into printable string
    print (key, "    ", value, (" " * (5 - len(value))), percent) # print

  inFile.close()    # close file

main()
