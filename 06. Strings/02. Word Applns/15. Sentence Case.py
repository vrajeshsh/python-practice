import os
os.system("cls")

word, count, new_str= "", 0, ""

print("To change a given string to sentence case:")
sent = input("Enter the string:\n").strip()+"."

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        count+=1
        if word=="i":
            word="I"
        if count==1 and not word.isupper():
            word=word.title()
        elif not word.isupper():
            word=word.lower()
        new_str+=word+ch
        if ch != ' ':
            new_str+= " "
        word=""

print("\nConverted sentence:\n",new_str,"\n", sep='')
