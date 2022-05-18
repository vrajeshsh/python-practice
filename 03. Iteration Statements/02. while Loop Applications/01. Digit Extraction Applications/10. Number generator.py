import os
os.system("cls")

print("To generate a number from a digit:")
dig = int(input("Enter a digit: "))

i,num=1,0
while(i<=dig):
    num=(num*10)+i
    i+=1
num*=9

if 0>dig>10:
    print("\nNumber formed:",num,"\n")
    
else:
    print("\nPlease enter a digit between 0 and 10\n")