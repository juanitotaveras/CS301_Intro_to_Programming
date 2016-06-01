def main():
  nums = input("Enter integers between 1 and 100: ")
  lst = nums.split()
  for i in range(len(lst)):
    lst[i] = int(lst[i])
  lst.sort()
  print ("lst =", lst)
  for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
      print (lst[i], "occurs", lst.count(lst[i]), "time")
    else:
      print (lst[i], "occurs", lst.count(lst[i]), "times")
main()
