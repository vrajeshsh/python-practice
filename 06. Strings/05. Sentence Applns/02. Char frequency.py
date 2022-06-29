import os
os.system("cls")

def isendofsentence(para, pos):
    paralen = len(para)
    if pos==paralen-1:
        return True
    if para[pos] in ".!?":
        if pos<paralen-1 and para[pos+1]==' ':
            if pos<paralen-2 and para[pos+2].isupper() or para[pos+2].isdigit():
                return True
    return False

def getfreqofchars(sent):
    vow, con, dig, spc, spl = 0, 0, 0, 0, 0
    for ch in sent:
        if ch in "AEIOUaeiou":
            vow+=1
        elif ch.isalpha():
            con+=1
        elif ch == ' ':
            spc+=1
        elif ch.isdigit():
            dig+=1
        else:
            spl+=1
    
    return vow,con,dig,spc,spl

print("To display frequency of vowels, consonants, space and special characters in paragraph:")
para = input("Enter the paragraph:\n").strip()
paralen = len(para)

sent, count = "", 0
print("\nSentences in the paragraph:")
for i in range(paralen):
    sent+=para[i]
    if isendofsentence(para, i):
        sent= sent.strip()
        vow, con, dig, spc, spl = getfreqofchars(sent)
        count+=1
        print(count,". ",sent.strip(),sep='')
        print("List of different characters and their frequencies:",
            "\nVOW\tCON\tDIG\tSPC\tSPL\n",
                vow,"\t",con,"\t",dig,"\t",spc,"\t",spl,"\n",sep='')
        sent=""
print()