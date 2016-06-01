# function sums the perimeter of rectangular 2-D list
def main():
  b = [4, 9, 2], [3, 5, 7], [8, 1, 6]
  # sum the first row
  sumrowstart = 0
  for j in range (len(b[0])):
    sumrowstart += b[0][j]
  print (sumrowstart)

  # sum the last row
  sumrowend = 0
  for j in range (len(b[-1])):
    sumrowend += b[-1][j]
  print (sumrowend)

  # sum the first column
  sumcolfirst = 0
  for i in range (len(b[0])):   # returns 3, so i goes 0, 1, 2
    sumcolfirst += b[i][0]
  print (sumcolfirst)

  # sum the last column
  sumcollast = 0
  for i in range (len(b[0])):
    sumcollast += b[i][-1]
  print (sumcollast)

  # sum everything and subtract the corner elements
  sum_p = sumrowstart + sumrowend + sumcolfirst + sumcollast - b[0][0] - b[-1][0] - b[0][-1] - b[-1][-1]
  print (sum_p)
main()

