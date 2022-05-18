from hashlib import sha1
import os
os.system("cls")

print("To count number of times a particular digit d occurs and replace it my d+1:")
temp = num = int(input("Enter the integer: "))
d= int(input("Enter the digit to search for: "))

fdig, matchcnt, newnum, index, lead0cnt = 0, 0, 0, 0, 0

while(temp>0):
    fdig = temp%10
    if fdig==d:
        matchcnt+= 1
    dig= 0 if fdig==9 else fdig+1 if fdig==d else fdig
    lead0cnt= lead0cnt+1 if dig==0 else 0 
    newnum+= dig*10**index
    index+=1
    temp//=10

print("\nThe digit",d,"occurs",matchcnt,"times.", 
    "\nThe new number is ", end= '')
print('0'*lead0cnt, end='')
print(newnum, "\n")
