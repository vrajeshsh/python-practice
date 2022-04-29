'''To calculate highest and lowest among n numbers'''

print("To calculate highest and lowest among n numbers")
n = int(input("Enter number of numbers: "))

maxi, mini= 0, 0
print()
for i in range(1,n+1):
    print("Enter Number #", i, ": ", end='', sep='')
    num = float(input())
    if i==1 or num > maxi:
        maxi = num
    if i==1 or num < mini:
        mini = num

print("\nHighest of all numbers: ",maxi,
    "\nLowest of all numbers: ",mini)

# Fixed and accepted