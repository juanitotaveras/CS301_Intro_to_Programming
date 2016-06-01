#  File: DNA.py

#  Description: Program that reads pairs of DNA strands and finds longest common sequence

#  Student Name: Juanito Taveras

#  Student UT EID: jmt3686

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: 10/28/14

#  Date Last Modified: 10/29/14



import string
def main():
    #open file for reading
    in_file = open ("./dna.txt", "r")
    #read number of pairs
    num_pairs = in_file.readline() #reads first line
    num_pairs = num_pairs.strip() #remove whitespace before and after
    num_pairs = int(num_pairs) #turn number of pairs into integer

    print ("Longest Common Sequences")

    #read pairs of strands
    pair_num = 1    # pair counter
    for i in range(num_pairs):
        st1 = in_file.readline() #reads second line in first iteration
        st2 = in_file.readline() #reads third line in first iteration
        st1 = st1.strip() #removes white space
        st1 = st1.upper() #makes uppercase
        st2 = st2.strip() #removes white space
        st2 = st2.upper() #makes uppercase
        #dna1 is longest strand, dna2 is shortest
        if (len(st1) > len(st2)):
            dna1 = st1   
            dna2 = st2   
        else:
            dna1 = st2
            dna2 = st1

        # get all substrings of dna2 and check if those substrings are in dna1
        wnd = len(dna2) # wnd stands for "window"
        max_length = 0
        while (wnd > 0):
            idx = 0
            while ((idx + wnd) <= len(dna2)):
                slice1 = dna2[idx: idx + wnd]
                match = dna1.find(slice1) # finds substrings in longer sequence
                if match != -1:   # -1 means none found
                    matching_substring = dna1[match: match + wnd] 
                    if len(matching_substring) >= max_length:
                        print ("Pair", pair_num, ": ", matching_substring)
                        max_length = len(matching_substring)
                else:
                    matching_substring = "No Common Sequence Found"
                idx += 1
            wnd -= 1
        if len(matching_substring) > 1:
            print ("Pair", pair_num, ": ", matching_substring)
        pair_num += 1
    # close file
    in_file.close()
main()

