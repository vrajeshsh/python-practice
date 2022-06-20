import os
os.system("cls")

def isVowel(chr):
    return chr.upper() in "AEIOU"

sent = input("Enter a sentence to check for twin vowels:\n")

vow, twinCnt= "", 0
sentLen = len(sent)
for i in range(sentLen-1):
    if isVowel(sent[i]) and isVowel(sent[i+1]): 
        twinCnt+=1
        vow+= sent[i]+sent[i+1] if vow=="" else ", "+sent[i]+sent[i+1]
    
print("\nOccurances of Twin Vowels are:\n",vow,
    "\nFrequency of Twin Vowels: ",twinCnt,"\n", sep='')