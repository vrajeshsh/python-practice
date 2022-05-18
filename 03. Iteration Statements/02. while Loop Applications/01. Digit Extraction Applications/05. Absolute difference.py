print("To calculate the absolute difference between a number and its reverse:")
num = int(input("Enter an integer: "))

temp, rev = num, 0
while(temp>0):
    dig=temp%10
    rev = (rev*10)+dig
    temp//=10
diff = abs(num-rev)

print("\nGiven integer:",num,
    "\nInteger's reverse:",rev,
    "\nAbsolute difference:",diff)
print("\n")