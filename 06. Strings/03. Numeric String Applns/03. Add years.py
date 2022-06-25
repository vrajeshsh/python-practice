import os
os.system("cls")

new_str, word= "", ""
print("To add year(s) to the year present in sentence:")
sent = input("Enter the sentence:\n").strip()+" "
yrs = int(input("Years to add: "))

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if word.isdigit() and len(word)==4:
            word = str(int(word)+yrs)
        new_str+=word+ch
        if ch!=" ":
            new_str+=" "
        word=""

print("\nSentence after adding",yrs,"to the year:\n",new_str, "\n", sep='')