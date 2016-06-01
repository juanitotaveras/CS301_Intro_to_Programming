def isConsecutiveFour(values):
  lst = values.split()
  count = 0
  for i in range(len(lst) - 3):
    if lst[i] == lst[i + 1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
      count += 1
  return count >= 1

def main():
  values = input("Enter some values: ")
  if isConsecutiveFour(values):
    print ("has consecutive four")
  else:
    print ("no consecutive four")
main()

