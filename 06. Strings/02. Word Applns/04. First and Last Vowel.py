import os
os.system("cls")

word, count, words, wrdCnt="", 0, "", 0

print("To display words which start and end with vowels:")
sent = input("Enter a sentence:\n")

for i in range(len(sent)):
    if sent[i].isalnum():
        word+=sent[i]
    elif word!="":
        if word[0] in "AEIOUaeiou" and word[-1] in "AEIOUaeiou":
            count+=1
            words+=word if words=="" else ", "+word
        wrdCnt+=1
        word=""

if count==0:
    print("\nWords which start and end with vowels NOT FOUND in the sentence!\n", sep='')
else:
    percent = (count*100)/wrdCnt
    print("\nWords that start and end with vowels are:\n",words,
        "\n\nPercentage: ",round(percent,2),"%\n", sep='')