import os
os.system("cls")

print("To show the first two and last two digits of an integer:")
first = num = int(input("Enter an integer: "))

while(first > 99):
    first//=10
last = num%100
newnum = first*100+last

if num<1000:
    print("\nPlease enter atleast a 4 digit integer\n")
else:
    print("\nFirst 2 digits: ",first, 
    "\nLast 2 digits: ", last, 
    "\nNumber formed with them: ", newnum,"\n", sep='')


