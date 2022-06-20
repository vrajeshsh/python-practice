from hashlib import new
import os
os.system('cls')

sent = input ("Enter a sentence to remove all vowels from it:\n")

new_str=""

for chr in sent:
    if chr not in "AEIOUaeiou":
        new_str+= chr

print("\nSentence without Vowels:\n",new_str,"\n")