import os
os.system("cls")

word, count, words, wrdCnt, vowCnt="", 0, "", 0, 0

print("To display words which contain more than 2 vowels:")
sent = input("Enter the sentence:\n")

for ch in sent:
    if ch.isalnum():
        if ch in "AEIOUaeiou":
            vowCnt+=1
        word+=ch
    elif word!="":
        if vowCnt>=2:
            count+=1
            words+=word if words=="" else ", "+word
        wrdCnt+=1
        vowCnt = 0
        word=""
        
if count==0:
    print("\nNo words with more than 3 letters FOUND in the sentence!\n", sep='')
else:
    percent = (count*100)/wrdCnt
    print("\nWords having 2 or more vowels:\n",words,
        "\n\nPercentage: ",round(percent,2),"%\n", sep='')