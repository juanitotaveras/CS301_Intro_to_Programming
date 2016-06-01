def main():
  st = eval(input("Enter string: "))
  window = 1
  final_string = ""
  for i in range(0, len(st)):
    bit = st[i:i+window]
    final_string += bit
    window += 1
  print (final_string)
main()
