print("To find the highest and lowest digits of an integer:")
num = int(input("Enter an integer: "))

temp, maxi, mini = num, 0, 0
while(temp>0):
    dig=temp%10
    if maxi==0 or  dig > maxi:
        maxi=dig
    if mini==0 or dig < mini:
        mini=dig
    temp//=10

print("\nHighest:",maxi,
    "\nLowest:",mini)
