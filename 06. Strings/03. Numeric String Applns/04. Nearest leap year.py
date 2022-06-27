import os
os.system("cls")

new_str, word = "", ""
print("To replace year(s) in a sentence to nearest leap years:")
sent = input("Enter the sentence:\n").strip()+" "

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        if word.isdigit() and len(word)==4:
            year = int(word)
            if not (year%4==0 and year%100!=0 or year%400==0):
                if year%4==1 or ((year%100>96 and year%100<=99) and\
                     (year//100)%4!=3):
                    year-= year%4
                else:
                    year+= 4-year%4
            word = str(year)
        new_str+=word+ch
        if ch!=" ":
            new_str+=" "
        word=""

print("\nSentence after making the year(s) leap:\n",new_str,"\n",sep='')


            
