import os
os.system("cls")

print("To calculate digital sum of numbers starting and ending with 5:")

ssum, i= 0, 0

print("\nGo on entering numbers below. Enter number <=0 to stop.")
while True:
    i+= 1
    print("Enter number", i,": ", end='')
    temp = num = int(input())
    if num <= 0:
        break
    last, ssum = num%10, 0
    while temp>0:
        first = temp%10
        ssum+= first
        temp//= 10
    if last == 5 and first==5:
        print("\nQualifying number",num,"starting and ending with 5 found!",
            "\nIts digital sum is ",ssum,"\n")
print("\n")
