import os
os.system("cls")

word= ""

print("To find the longest and shortest words in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

maxi = mini = sent[0:sent.index(" ")]
for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if len(word) > len(maxi):
            maxi = word
        if len(word) < len(mini):
            mini = word
        word = ""

print("\nLongest word:",maxi,"\nShortest word:", mini,"\n")
