#  File: GuessingGame.py

#  Description: Program that guesses what number you're thinking of in seven tries or less.

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 11/15/2014

#  Date Last Modified: 11/16/2014


def main():
  print ("Guessing game")
  print ()
  print ("Think of a number between 1 and 100 inclusive.")
  print ("And I will guess what it is in 7 tries or less.")
  print ()
  ready = ""   # creates blank string
  list = []    # creates empty list
  for i in range(1, 101):   # adds numbers 1 - 100, inclusive, to list
    list.append(i)
  while ready != "y" and ready != "n":     # if user doesn't input y or n, keep asking for input
    ready = str(input("Are you ready? (y/n): "))
  if ready == "n":    # if user inputs n, print Bye and exit
    print ("Bye")
    return
  elif ready == "y":   # if user inputs "y", run series of guesses
    lo = 0
    hi = len(list)
    guess = 1
    while guess < 8:
      while (lo <= hi):
        mid = (lo + hi) // 2
        user1 = 3   # random number that isn't -1, 0, or 1
        while (user1 != -1 and user1 != 1 and user1 != 0):
          print ("Guess", guess, ": The number you thought was", mid)
          user1 = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
        if user1 == 1:  # if user says guess was high, search lower half
          hi = mid - 1
        elif user1 == -1:  # if user says guess was low, search higher half
          lo = mid + 1
        elif user1 == 0:    # if user says guess was right, exit
          print ("Thank you for playing the Guessing Game.")
          return
        guess += 1
      print ("Either you guessed a number out of range or you had an incorrect entry.")
      return
main()
    

