import os
os.system("cls")

vow, con, pun, spl, spc, dig = 0, 0, 0, 0, 0, 0

sent = input("Enter a sentence for counting different types of characters:\n")

for chr in sent:
    chr= chr.lower()
    if chr in "aeiou":
        vow+=1
    elif chr.isalpha():
        con+= 1
    elif chr== ' ':
        spc+=1
    elif chr in ".?!;:'-\"":
        pun+=1
    elif chr.isdigit():
        dig+=1
    else:
        spl+=1

print("\nList of different characters and their frequencies:",
    "\nVOW\tCON\tDIG\tSPC\tPUN\tSPL\n",
    vow,"\t",con,"\t",dig,"\t",spc,"\t",pun,"\t",spl,"\n",sep='')
