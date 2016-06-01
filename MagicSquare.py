#  File: MagicSquare.py

#  Description: Program that checks if squares are magic squares

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 11/11/2014

#  Date Last Modified: 11/12/2014


def isMagic(b):   # function checking if square is magic
  # sum the first row
  sumrowstart = 0
  for j in range (len(b[0])):
    sumrowstart += b[0][j]

  # sum the last row
  sumrowend = 0
  for j in range (len(b[-1])):
    sumrowend += b[-1][j]

  # sum the first column
  sumcolfirst = 0
  for i in range (len(b[0])):
    sumcolfirst += b[i][0]

  # sum the last column
  sumcollast = 0
  for i in range (len(b[0])):
    sumcollast += b[i][-1]

  # sum of diagonal left to right
  sum_lr = 0
  for i in range (len(b)):
    sum_lr += b[i][i]

  # sum of diagonal right to left
  sum_rl = 0
  for i in range (len(b)):
    sum_rl += b[i][len(b) - 1 - i]

  # use magic square formula to get side sum that should equal other sums
  sidesum = len(b[0]) * (len(b[0]) ** 2 + 1) / 2

  # return true if everything equals each other
  return (sumrowstart == sidesum and sumrowstart == sumrowend and sumcolfirst == sumcollast and sumrowend == sumcolfirst and sumrowstart == sum_lr and sum_lr == sum_rl)


def main():
  inFile = open ("squares.txt", "r") # open file for reading
  outFile = open ("results.txt", "w") # open file for writing
  num_squares = inFile.readline()    # read first line
  num_squares = num_squares.strip()   # remove white space
  num_squares = int(num_squares)     # turn number of squares into usable integer
  outFile.write(str(num_squares) + "\n")   # start writing to output

  # process each square separately
  for i in range (num_squares):
    # read blank line
    blank = inFile.readline()
    # read dimensions of square
    dim = inFile.readline()
    dim = dim.strip()
    dim = int(dim)
    a = []   # create 2-D list
    row_string = "" # make string to write to output
    for row in range(dim):
      row = inFile.readline()
      row = row.strip()
      row_string += row + "\n"   # making string of square for output
      b = row.split()
      for k in range(len(b)):
        b[k] = int(b[k])
      a.append(b)

    # write output
    outFile.write("\n")  # blank line
    if isMagic(a):
      outFile.write(str(dim) + " valid \n")
    else:
      outFile.write(str(dim) + " invalid \n")
    outFile.write(row_string)   # loop ends here

  print ("The output has been written to results.txt")

main()
