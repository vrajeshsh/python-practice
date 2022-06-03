import os
os.system("cls")

upVow, lowCon, spl, wrdLen, wrdCnt = 0, 0, 0, 0, 0

sent = input("Enter a sentence for counting different types of characters:\n")

for chr in sent:
    if chr.isalnum() or chr=='-':
        spl+= 1 if chr== '-' else 0
        wrdLen+= 1
        if chr in "AEIOU":
            upVow+=1
        elif chr.isalpha() and chr not in "aeiou":
            lowCon+=1
    else:
        wrdCnt+= 1 if wrdLen > 3 else 0
        if chr!=' ':
            spl+=1
        wrdLen= 0    
    
print("\nList of different characters and their frequencies:",
    "\nNo. of uppercase vowels: ",upVow,
    "\nNo. of lowercase consonants: ",lowCon,
    "\nNo. of special characters: ",spl,
    "\nNo. of words whose length >3: ",wrdCnt,"\n",sep='')
