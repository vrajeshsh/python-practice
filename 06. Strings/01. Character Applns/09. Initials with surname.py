import os
os.system("cls")

name = input("Enter name (in full) to display initials with surname:\n")

shortName, nameLen, surname = name[0].upper(), len(name), ""
for i in range(1, nameLen):
    if name[i-1]==' ':
        surname= ""
        shortName+= "."+name[i].upper()
    else:
        surname+= name[i].lower()
shortName+= surname

print("\nInials with surname:\n",shortName,"\n", sep='')