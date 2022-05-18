import os
os.system("cls")

print("To find the greatest odd and smallest even digit and calculate difference of comibation:")
num = int(input("Enter a multidigit integer: "))

temp, maxi, mini = num, 0, 0
while(temp > 0):
    dig = temp%10
    if dig%2==0 and (maxi==0 or dig > maxi):
        maxi = dig
    elif mini==0 or dig < mini:
        mini = dig
    temp//=10
combi1 = maxi*10+mini
combi2 = mini*10+maxi

diff = abs(combi1-combi2)
print("\nGreatest Even Digit:",maxi,
    "\nSmallest Odd Digit:",mini,
    "\nAbsolute difference between",combi1,"and",combi2,"is",diff,"\n")
    