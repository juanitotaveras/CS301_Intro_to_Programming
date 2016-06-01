def is_palindrome (st):
  return (st == st[::-1])


def rotate(st, rot):
  end = st[-(rot):]
  start = st[:-(rot)]
  return (end + start)

def two_str(inFile, st):
  in_file = open (inFile, "r")
  count = 0
  for line in in_file:
    line = line.strip()
    count += line.count(st)
  return count

def taboo (inFile, words):
  in_file = open (inFile, "r")
  for line in in_file:
    for i in range(len(words)):
      return line.count(words[i]) > 0

def products(list1, list2):
  sum = 0
  for i in range(len(list1)): # both are same size so whatever
    sum += (list1[i] * list2[i])
  return sum

def ascending(a):
  return a == a.sort()

def bubblesort(dalist):
  newlist = []
  newlist.append(min(dalist))
  dalist.remove(min(dalist))
  newlist.append(min(dalist))
  dalist.remove(min(dalist))
  newlist.append(max(dalist))
  return newlist

def shuffle(dalist):
  import random
  return random.shuffle(dalist)

def series(n):
  sum = 0
  for i in range(0, n+1):
    sum +=  ((n + 1)*(n + 2)) ** (-1)
  return sum

def addFraction(k):
  sum = 0
  for i in range(k):
    sum += (-1)**(k+1) * (1/2)**(2 * k-1)
  return (sum)
  
def pattern(n):
  for i in range(1, n+1):
    string = str(i) + " "
    string *= i
    print(string)


def main():
  print ("Question 1: ", is_palindrome("racecar"))
  print ("Question 2: ", rotate("computer", 2))
  print ("Question 3: ", two_str("isbn.txt", "X"))
  print ("Question 4: ", taboo ("isbn.txt", ["X", "32"]))
  print ("Question 5: ", products ([1, 2, 3], [4, 5, 6]))
  print ("Question 6: ", ascending([1, 2, 3, 4, 5, 6]))
  print ("Question 7: ", bubblesort([1, 3, 2]))
  print ("Question 8: ", shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))
  print()
  print ("SAMPLE QUESTIONS FROM ACTUAL CLASS NOTES")
  print ("Question 1: ", series(5))
  print ("Question 2: ", addFraction(7))
  print (pattern(5))
main()
