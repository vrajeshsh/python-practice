import os
os.system("cls")

print("To count the number of positive and negative numbers:")

poscnt, negcnt, i = 0, 0, 0

print("\nGo on entering numbers below. Enter 0 to stop.")
while True:
    i+= 1
    print("Enter number", i,": ", end='')
    num = float(input())
    if num == 0:
        break
    if num>0:
        poscnt+=1
    else:
        negcnt+=1

print("\nCount of negative nos:",negcnt,
    "\nCount of positive nos:", poscnt, "\n")
