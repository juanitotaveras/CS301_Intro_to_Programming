def equals(m1, m2):
  l_m1 = m1.split()
  l_m2 = m2.split()
  for i in range(len(l_m1)):
    l_m1[i] = int(l_m1[i])
  for i in range(len(l_m2)):
    l_m2[i] = int(l_m2[i])
  l_m1.sort()
  l_m2.sort()
  return l_m1 == l_m2

def main():
  u_m1 = input("Enter m1: ")
  u_m2 = input("Enter m2: ")
  if equals(u_m1, u_m2):   # if true
    print("The two lists are identical")
  else:                # if not true
    print("The two lists are not identical")
main()
