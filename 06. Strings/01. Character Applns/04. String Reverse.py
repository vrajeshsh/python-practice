import os
os.system("cls")

new_wrd=""
word = input("Enter a word to check Palindrome: ")

for chr in word:
    new_wrd = chr + new_wrd

print("\n","Non-" if word.lower() != new_wrd.lower() else "", 
    "Palindromic String\n",sep='')