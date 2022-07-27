import os
os.system("cls")

print("To display all names stating with user input letter:")
n = int(input("Enter the number of names: "))
print()

names, matches = [], ""
for i in range(n):
    print("Enter name #",i+1,": ",sep='', end='')
    names.append(input())

alpha = input("Enter alphabet to search for names: ")

for i in range(n):
    if names[i][0].lower()==alpha.lower():
        matches+= names[i]+"\n"
    
if matches=="":
    print("\nNone of the names start with ",alpha,"!\n",sep='')
else:
    print("\nThe matching names:\n",matches, sep='')