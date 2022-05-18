import os
os.system("cls")

print("To calculate sum of intsums and percentage of fractions")

i, intsum, count = 0, 0, 0

while True:
    i+= 1
    print("Enter number", i,": ", end='')
    num = float(input())
    if num==0:
        break
    if num-int(num)==0:
        intsum+= num
    else:
        count+=1
percent = count/(i-1)*100   # i-1 to counter balance the terminating number

print("\nSum of integral numbers:",intsum,
    "\nPercentage of fractional numbers:",round(percent, 2),"%\n")
