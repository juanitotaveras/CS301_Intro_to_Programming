# File: Deal.py

# Description: Program that computes whether or not switching your guess in "Let's Make a Deal" will increase your likelihood of winning

# Student Name: Juanito Taveras
 
# Student UT EID: jmt3686

# Course Name: CS 303E

# Unique Number: 52700

# Date Created: 10/4/14

# Date Last Modified: 10/4/14

import random
def main():
    runs = eval(input("Enter number of times you want to play: "))
    wins = 0
    count = 0
    print ('Prize','Guess','View','New Guess')
    while(count < runs):
        prize = random.randint (1, 3)
        guess = random.randint (1, 3)
        view = 0
        if ((prize != 3) and (guess != 3)):
            view = 3
        elif (prize != 2 and guess != 2):
            view = 2
        else:
            view = 1
        newGuess = 0
        if (guess != 3 and view != 3):
            newGuess = 3
        elif (guess != 2 and view != 2):
            newGuess = 2
        else:
            newGuess = 1
        #track wins
        if newGuess == prize:
            wins += 1
        count += 1      #exit loop
        print (' ', prize,'   ', guess,'  ', view,'     ', newGuess)
    prob_switch = wins / runs
    prob_notswitch = 1 - prob_switch
    print ('Probability of winning if you switch =', round(prob_switch, 2))
    print ('Probability of winning if you do not switch =', round(prob_notswitch, 2))

main()


    
