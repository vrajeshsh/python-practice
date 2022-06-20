import os
os.system("cls")

dbl_cnt, dbl_wrd = 0, 0

sent = input("Enter a sentence to count double-lettered words:\n")

sent_len = len(sent)
for i in range(0, sent_len-1):
    if sent[i].isalpha() and sent[i] == sent[i+1]:
        dbl_cnt+= 1                     # counting double-letters here
    if sent[i]== ' ' or i==sent_len-2:  # if the end of the word or sentence has been reached
        if dbl_cnt > 0:                 # if at that instance, double-letters had been found...
            dbl_wrd+= 1                 # then increment the dbl-word counter and...
            dbl_cnt= 0                  # reset the dbl-letter counter

print("\nNo. of double-lettered words:",dbl_wrd)
