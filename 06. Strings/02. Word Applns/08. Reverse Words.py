import os
os.system("cls")

word, new_sent="", ""
print("To reverse each word in a sentence:")
sent = input("Enter the sentence:\n")

for ch in sent:
    if ch.isalnum():
        word+=ch
    else:
        new_sent+=word[::-1]+ch
        if ch!=' ':
            new_sent = new_sent.strip()+' '
        word=""

print("\nSentence after reversal:\n",new_sent,"\n",sep='')