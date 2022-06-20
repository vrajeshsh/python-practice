from hashlib import new
import os
os.system('cls')

sent = input("Enter a sentence to covert to Title case:\n")

new_str, sentLen = "", len(sent)

for i in range(sentLen):
    chr= sent[i]
    chr= chr.upper() if i==0 or sent[i-1]==' ' else \
         chr.lower() if chr.isalnum() or chr==' ' else ""
    new_str+= chr
            
print("\nOriginal sentence in Title Case:\n",new_str,"\n", sep='')
