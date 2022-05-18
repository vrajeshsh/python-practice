import os
os.system("cls")

print("To find the missing digits of an integer (if any):")
num = int(input("Enter the integer: "))

missdigits, i = "", 0
for i in range(10):  # this program based on for-while combo
    temp=num
    while temp > 0:
        dig= temp%10
        if i==dig:
            break
        temp//=10
    if(temp == 0):
        missdigits+= str(i) if missdigits == "" else ", "+str(i)

if missdigits=="":
    print("\nAll digits are present\n")
else:
    print("\nThe missing digits of '",num,"' are:\n", missdigits,"\n",sep='')
