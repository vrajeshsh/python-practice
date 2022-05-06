import os
os.system("cls")

print("To check if a given number is a Tech number or not:")
num = int(input("Enter an integer: "))

temp, temp2, count=num, num, 0

while(temp>0):
    count+=1
    temp//=10

part1 = temp2%(10**(count/2))
part2 = temp2//(10**(count/2))

if count%2==0 and (part1+part2)**2==num:
    print("\n",num,"is a Tech number\n")
else:
    print("\n",num,"is not a Tech number\n")

#print("\nThe integer ",num," is"," NOT " if count%2==0 or (part1+part2)**2!=num else ""," a Tech number\n",sep='')
