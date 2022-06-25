import os
os.system("cls")

def digitToWord(num):
    return "Zero" if num==0 else "One" if num==1 else "Two" if num==2 \
        else "Three" if num==3 else "Four" if num==4 else "Five" \
            if num==5 else "Six" if num==6 else "Seven" if num==7\
                else "Eight" if num==8 else "Nine"
    
new_str, word, digword = "", "", ""

print("To convert the digits of the integers to words in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

for ch in sent:
    if ch.isalnum():
        word+=ch
        if ch.isdigit():
            digword+= digitToWord(int(ch))+" "
    elif word!="":
        if word.isdigit():
            word= digword.strip()
        new_str+= word+ch
        if ch!=' ':
            new_str+=" "
        word= digword= ""

print("\nSentence after converting numbers to words:\n",new_str, "\n", sep='')

# WELCOME to the (complex) World of Numeric Strings!!