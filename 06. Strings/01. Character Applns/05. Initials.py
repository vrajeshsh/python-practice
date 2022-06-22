import os
os.system("cls")

ini=""
name = input("Enter a full name to display initials: ")

for i in range(len(name)):
    if (i==0 and name[0].isalpha()) or \
        (name[i-1].isspace() and name[i].isalpha()):
        ini+= name[i]+"."

print("\nInials of ",name.strip(),": ",ini.upper(),"\n", sep='')
