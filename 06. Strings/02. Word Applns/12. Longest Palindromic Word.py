import os
os.system("cls")

word, rev, maxlen, wrdlen = "", "", 0, 0

print("To display the longest Palindromic word in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

for ch in sent:
    if ch.isalnum():
        word+=ch
        rev=ch+rev
        wrdlen+= 1
    elif word!="":
        if rev.lower()==word.lower() and wrdlen > maxlen:
            maxlen = wrdlen
            max_word = word
        word, rev, wrdlen = "", "", 0

print("\nLongest Palindromic word: ",max_word,"\n",sep='')