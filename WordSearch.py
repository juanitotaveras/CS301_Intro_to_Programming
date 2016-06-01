#  File: WordSearch.py

#  Description: Program that finds the words in a word search.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E 

#  Unique Number: 52700

#  Date Created: 11/21/2014

#  Date Last Modified: 11/21/2014

def search_word_block(word_block, word, m, n):
  #word_block is a 2-D list, word is string, m is how many rows, n is how many columns
  word_orig = word

  # check rows for match (forwards)
  i = 0
  j = 0  # j is column word is in
  for i in range(m): # check rows for match
    row = ""
    for ch in word_block[i]:   # make row into string
      row += ch
    if row.find(word) != -1: # if it's a match
      j = row.find(word)
      j += 1  # add one to the column
      i += 1  # add one to the row
      location = str(i) + " " + str(j)  # row plus space plus column
      return location                    # if it's a match, the function ends here
  # now reverse word and check again
    word_list = []    # make new list
    for ch in word_orig:   # for every character in word string
      word_list.append(ch)  # add character to list
    word_list.reverse()  # reverse list
    word_rev = ""  # make new string
    for char in word_list: # for every character in reversed word list
      word_rev += char  # add character to the reversed word string
    if row.find(word_rev) != -1:  # if there's a match
      j = row.find(word_rev)  # j is column word is in
      j += len(word_rev)   # since word is in reverse, add length of word to get location of first letter
      i += 1    # add one to row
      location = str(i) + " " + str(j)   # row plus space plus column
      return location
      
  # check columns for match
  # pretty much a repeat of above
  # reset variables if word not found in rows
  word = word_orig
  i = 0
  j = 0
  for j in range(n): # n is column number
    col = [] 
    for i in range(m): # m is row number
      col.append(word_block[i][j])  # make new list out of characters in column
    col_str = ""  # make new string
    for ch in col:
      col_str += ch # makes col into string
    if col_str.find(word) != -1: # if it's a match
      i = col_str.find(word)
      i += 1
      j += 1
      location = str(i) + " " + str(j)
      return location
    # now check again with reversed word 
    if col_str.find(word_rev) != -1:
      i = col_str.find(word_rev)
      i += 1
      j += 1
      location = str(i) + " " + str(j)
      return location

  # check diagonals
  word = word_orig
  i = 0
  j = 0
  

  # word is not found
  return "0 0"
# end function

def main():
  inFile = open ("./hidden.txt", "r") # open file with words
  outFile = open ("./found.txt", "w") # output 
  line = inFile.readline() # read first line
  num_mn = line.strip() # remove whitespace
  num_mn = num_mn.split()  # split into elements in list
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
  
  # read number of words to be searched for
  word_num = inFile.readline() 
  word_num = word_num.strip()
  word_num = int(word_num)

  for words in range(word_num):
    word = inFile.readline()
    word = word.strip()
   # check if word is in block
    out = (search_word_block(word_block, word, m, n)) # use our beautifully crafted function
    out = out.rjust(30 - len(word), ' ')  # justify it!
    output = word + out + "\n" # don't forget to add the 'break line' thingy
    outFile.write(output)  # write output to output file

# close our files
  inFile.close()
  outFile.close()
main()
  
