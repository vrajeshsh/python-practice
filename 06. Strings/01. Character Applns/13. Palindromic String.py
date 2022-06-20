import os
os.system('cls')

sent = input("Enter a sentence to check palindrome:\n")

orig, rev = "", ""
for chr in sent.lower():
    if chr.isalnum():
        orig+= chr
        rev= chr + rev

print("\nNON " if orig != rev else "\n",
        "Palindromic Sentence\n", sep='')