def locateLargest(a):
  
  i = a.index(max(a))   # returns max row
  j = a[i].index(max(a[i]))   # return max column
  return (i, j)
  
def main():
  num_rows = int(input("Enter the number of rows in the list: "))
  a = []
  for i in range(num_rows):
    row = input("Enter a row: ")
    lst = row.split()
    for i in range(len(lst)):
      lst[i] = int(lst[i])
    a.append(lst)
  print (a)
  print (locateLargest(a))
main()
  
