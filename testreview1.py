def freq_string(st):
  da_dict = {}
  for ch in st:
    if ch != ' ':
      if ch not in da_dict:
        da_dict[ch] = 1
      else:
        da_dict[ch] += 1
  return sorted(da_dict)

def common_string(list1, list2):
  s1 = set(list1)
  s2 = set(list2)
  common = []
  for el in s1:
    if el in s2:
      common.append(el)
  return common

import random
def three_by_five (list):
  for i in range(3):
    new = []
    for j in range(5):
      new.append(random.randint(1, 100))
    list.append(new)
  return list

def sum_lists (list1, list2):
  list3 = []
  for i in range (len(list1)):
    new = []
    for j in range (len(list1[i])):
      new.append(list1[i][j] + list2[i][j])
    list3.append(new)
  return list3

def revRows(a):
	m = []
	for row in a:
		m.append(row.reverse())
	return m
def revRow_2(a):
  rev_list = []
  for i in range(len(a)):
    row = []
    for j in range(1, len(a[0] + 1):
      row.append(a[i][-j])
    rev_list.append(row)
  return rev_list
  
      

def main():
  list1 = ["penis", "poop", "cock", "dick", "shit"]
  list2 = ["cock", "poop", "vagina", "shit", "cunt"]
  print (common_string(list1, list2))
  list = []
  l1 = [ [1, 2, 3], [2, 2, 3] ]
  l2 = [ [2, 2, 3], [1, 2, 3] ]
  print ("sum_lists:", sum_lists (l1, l2))
  print (three_by_five(list))
  print()
  print ("revRows:", revRows(l1))
main()
