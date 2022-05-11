import os
os.system("cls")

print("To search digit in integer:")
temp = num = int(input("Enter the integer: "))
finddig= int(input("Enter the digit to search for: "))

digcnt, pos = 0, 0

while(temp>0):
    dig= temp%10
    if(dig == finddig):
        pos= digcnt
    digcnt+=1
    temp//=10

if pos == 0:
    print("\nThe digit '", finddig, "'was not found!\n")
else:
    print("\nThe digit '",finddig,"' occurs at position",
    (digcnt-pos), "\n")
