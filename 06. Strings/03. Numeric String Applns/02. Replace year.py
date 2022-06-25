import os
os.system("cls")

new_str, word= "", ""
print("To replace year in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "
new_yr = int(input("Year to replace with: "))

for ch in sent:
    if ch.isalnum():
        word+= ch
    elif word!="":
        if word.isdigit() and len(word)==4:
            word = str(new_yr)
        new_str+=word+ch
        if ch!=" ":
            new_str+=" "
        word=""

print("\nSentence after replacing the year:\n",new_str, "\n", sep='')