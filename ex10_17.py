def isAnagram(s1, s2):
  s1 = str(s1)
  s2 = str(s2)
  lst1 = []
  for ch in s1:
    lst1.append(ch)
  lst2 = []
  for ch in s2:
    lst2.append(ch)
  lst1.sort()
  lst2.sort()
  if lst1 == lst2:
    return ("is anagram")
  else:
    return ("not anagram")

def main():
  s1, s2 = eval(input("Enter two strings: "))
  print (isAnagram(s1, s2))
main()
