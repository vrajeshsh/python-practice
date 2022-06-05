import os
os.system('cls')

new_str=''
sent = input("Enter a sentence to convert vowels to upper and consonants to lower case:\n")

for chr in sent:
    chr= chr.lower() if chr in "AEIOUaeiou" else \
         chr.upper() if chr.isalpha() else chr
    new_str+= chr

print("\nSentence after converting cases:\n",new_str,"\n", sep='')

