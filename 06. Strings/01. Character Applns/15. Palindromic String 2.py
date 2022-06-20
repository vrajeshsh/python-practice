import os
os.system("cls")

sent = input("Enter a sentence to check for palindrome:\n")

sent_len = len(sent)
i, j = 0, sent_len-1

while i<j:
    if not sent[i].isalnum():       # incase an untoward char is found at the left end, update the right counter 
        j+= 1
    elif not sent[j].isalnum():     # do reverse in case the same occurs at the right end
        i-= 1
    elif sent[i].lower() != sent[j].lower():  # incase the letters do not match then...
        break                       # break the loop
    i+= 1                           # increment left counter
    j-= 1                           # decrement right counter

print("\n","Non-" if i<j else "","Palindromic Sentence.", sep='')
