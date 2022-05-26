import os, math
os.system("cls")

def isDivisibleBy11(num):
    sign, ssum = 1, 0
    while num>0:
        ssum+=(sign)*(num%10)
        sign*=-1
        num//=10
    return ((ssum/11)==(ssum//11)) or ssum==0

num = int(input("Enter an integer to check divisibility by 11: "))
print("\nThe number",num,"is","" if isDivisibleBy11(num) else "NOT","divisible by 11!\n")
