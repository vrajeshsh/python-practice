import os
os.system("cls")

word, count, words, wrdCnt="", 0, "", 0

print("To display words which contain more than 3 letters:")
sent = input("Enter the sentence:\n")

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if len(word)>3:
            count+=1
            words+=word if words=="" else ", "+word
        wrdCnt+=1
        word=""

if count==0:
    print("\nNo words with more than 3 letters FOUND in the sentence!\n", sep='')
else:
    percent = (count*100)/wrdCnt
    print("\nWords having more than 3 letters:\n",words,
        "\n\nPercentage: ",round(percent,2),"%\n", sep='')
