def sortColumns(m):  # function that sorts columns
  col1list = []
  col2list = []
  col3list = []
  for i in range(len(m)):
    col1list.append(m[i][0]) # makes single 3-item list with elements in first column
  for i in range(len(m)):
    col2list.append(m[i][1]) # makes single 3-item list with elements in second column
  for i in range (len(m)):
    col3list.append(m[i][2])
  col1list.sort()   # sorts the lists
  col2list.sort()
  col3list.sort()
  for i in range(len(col1list)): # replaces first column items with items in first list
    m[i][0] = col1list[i]
  for i in range(len(col2list)):
    m[i][1] = col2list[i]
  for i in range(len(col3list)):
    m[i][2] = col3list[i]
  return m   # returns sorted list
      




def main():
  print ("Enter a 3-by-3 matrix row by row:")
  list = []
  for i in range(3):
    row = input()
    lst = row.split()
    for i in range(len(lst)):
      lst[i] = float(lst[i])  # turns everything into floats
    list.append(lst)
  print("The column-sorted list is")
  outlist = sortColumns(list)
  for i in range(len(outlist)):
    for j in range(len(outlist)):
      outlist[i][j] = str(outlist[i][j]) # turns all items into strings
  for i in range(len(outlist)):
    outlist[i] = ' '.join(outlist[i])

  for i in range(len(outlist)):
    print(outlist[i])
  
main()
