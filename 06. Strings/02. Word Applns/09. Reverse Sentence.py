import os
os.system("cls")

word, new_sent="", ""
print("To reverse position of each word in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

for ch in sent:
    if ch.isalnum():
        word+=ch
    else:
        new_sent=word+ch+ new_sent
        if ch!=' ':
            new_sent=new_sent.strip()+" "
        word=""

print("\nSentence after reversal:\n",new_sent,"\n",sep='')