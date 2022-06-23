import os
os.system("cls")

word, new_sent="", ""
print("To replace all occurences of a given word by another word in a sentence:")
sent = input("Enter the sentence:\n")
rem = input("\nEnter the word to replace: ")
rep = input("Enter the new word: ")

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if word.lower()==rem.lower():
            word= rep
        new_sent+= word+ch
        if ch!=' ':
            new_sent=new_sent.strip()+" "
        word=""

print("\nSentence after replacing '",rem,"':\n",new_sent,"\n", sep='')