
def isMarkovMatrix(m):  # m is 2-D list
  col1 = 0
  col2 = 0
  col3 = 0
  for i in range(len(m)):  # returns 3     
    col1 += m[i][0] #sum column 1
  for i in range(len(m)):
    col2 += m[i][1] #sum column 2
  for i in range(len(m)):
    col3 += m[i][2] #sum column 3
  for i in range(len(m)):
    for j in range(len(m)):
      if m[i][j] > 0: #if all elements are positive
        return col1 == 1 and col2 == 1 and col3 == 1
      else:
        return False


def main():
  print ("Enter a 3-by-3 matrix row by row:")
  list = []
  for i in range(3):
    row = input()
    lst = row.split()
    for i in range(len(lst)):
      lst[i] = float(lst[i])
    list.append(lst)
    
  if isMarkovMatrix(list):
    print ("It is a Markov matrix")
  else:
    print ("It is not a Markov matrix")
main()
  
  
