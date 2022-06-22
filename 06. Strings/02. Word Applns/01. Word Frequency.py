import os
os.system("cls")

myword, count = "", 0

print("To find the frequency of a word in a sentence:")
sent = input("Enter the sentence:\n")
word = input("\nEnter the word: ")

for ch in sent:
    if ch.isalnum():
        myword+= ch
    else:
        if myword.lower() == word.lower():
            count+=1
        myword= ""

if count==0:
    print("\nThe word '", word,"' was NOT FOUND in the sentence!\n", sep='')
else:
    print("\nFrequency of '",word,"': ",count,"\n", sep='')
