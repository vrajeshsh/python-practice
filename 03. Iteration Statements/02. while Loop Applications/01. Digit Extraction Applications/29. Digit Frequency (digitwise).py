import os, math
os.system("cls")

print("To display the frequency of the digits as per the sequence of the digits:")
temp = num = int(input("Enter the integer: "))

newStr, newnum, digcnt = "", 0, int(math.log10(num)+1)

print("\nDIGIT\t\tFREQUENCY")
while(digcnt > 0):
    digcnt-= 1
    pow= 10**digcnt
    dig= temp//pow
    newnum= newnum*10+dig
    temp%= pow
    n, freq = num, 0
    while n > 0:
        if n%10 == dig:
            freq+= 1
        n//= 10
    n, cnt = newnum, 0
    while n > 0:
        if n%10 == dig:
            cnt+= 1
        n//= 10
    if cnt==1:
        print(dig, "\t\t", freq)

# No string used! What a relief  -- English, Maths and Logic -- That's all is reqd.