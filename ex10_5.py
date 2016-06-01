def main():
  nums = input("Enter ten numbers: ")
  lst1 = nums.split()
  for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
  lst2 = []
  for i in range(len(lst1)):
    if lst2.count(lst1[i]) == 0:
      lst2.append(lst1[i])
  for i in range(len(lst2)):
    lst2[i] = str(lst2[i])
  str1 = ' '.join(lst2)
  print ("The distinct numbers are:", str1)
main()
