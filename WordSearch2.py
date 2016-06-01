#  File: WordSearch.py

#  Description:

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E 

#  Unique Number: 52700

#  Date Created: 11/21/14

#  Date Last Modified: 6/1/16

def main():
  #word_block is a 2-D list, word is string, m is how many rows, n is how many columns
  word_block = ['P', 'O', 'S', 'T', 'T', 'U', 'B', 'Q', 'P', 'O'], ['P', 'O', 'P', 'J', 'U', 'A', 'N', 'I', 'T', 'O']
  word = "BUTTS"
  m = 2
  n = 10
  word_orig = word

  # check rows for match (forwards)
  i = 0
  j = 0  # j is column word is in
  for i in range(m): # check rows for match
    row = ""
    for ch in word_block[i]:   # make row into string
      row += ch
    if row.find(word) != -1:
      j = row.find(word)
      location = (str(m) + " " + str(j))
      print (location)

  # now reverse word and check again
    word_list = []
    for ch in word_orig:
      print(ch)
      word_list.append(ch)
    word_list.reverse()
    word_rev = ""
    print (word_list)
    return
    for char in word_list: # turn word into list again
      word_rev += char
    if row.find(word_rev) != -1:
      j = row.find(rev)
      location = str(m) + " " + str(j)
      print (location)

      
  # check columns for match
  # reset variables if word not found in rows
  word = word_orig
  i = 0
  j = 0
  for i in range(n): # n is column number
    col = [] 
    for j in range(m):
      col.append(word_block[j][i])
    col_str = ""
    for ch in col:
      col_str += ch # makes col into string
    if col_str.find(word) != -1:
      i = col_str.find(word)
      location = str(i) + " " + str(n)
      print (location)
    # now reverse word and check again
    word_list = []
    for ch in word:
      word_list.append(ch)
    word_list = word_list.reverse()
    word_rev = ""
    for ch in word_list:
      word_rev += ch
    if col_str.find(word_rev) != -1:
      i = col.str.find(word_rev)
      location = str(i) + " " + str(n)
      print (location)
#if __name__ = "__main__":
  main()
'''
def main():
  inFile = open ("./hidden.txt", "r") # open file with words
  outFile = open ("./found.txt", "w") # output 
  line = inFile.readline()
  num_mn = line.strip()
  num_mn = num_mn.split()
  m = int(num_mn[0])  # m is number of lines in grid
  n = int(num_mn[1])  # n is number of characters in each line
  blank = inFile.readline() # read blank line

  word_block = [] # make new list where characters will go
  # grid line will be m, column will be n
  for i in range(m):
    char_line = inFile.readline()
    char_line = char_line.strip()
    char_line = char_line.split()
    word_block.append(char_line) 

  blank2 = inFile.readline()  # read second blank line
  
  word_num = inFile.readline()
  word_num = word_num.strip()
  word_num = int(word_num)

  for words in range(word_num):
    word = inFile.readline()
    word = word.strip()
   # word_1 = word_1.split   # makes word_1 into list
    # now we check if word_1 is in word_block
    out = (search_word_block(word_block, word, m, n))
    print(word_1, out)

  inFile.close()
  outFile.close()

main()
'''
  

