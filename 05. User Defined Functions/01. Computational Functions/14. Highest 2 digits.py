import os
os.system("cls")

def highestDig(num):
    max = 0
    while num>0:
        dig = num%10
        if dig>max:
            max = dig
        num//=10
    return max

print("To find the maxghest possible 2-digited number in an integer:")
temp = num = int(input("Enter an integer: "))

count, max, secmax = 0, highestDig(num), 0

while temp > 0:
    dig = temp%10
    if dig==max:
        count+=1
    elif dig > secmax and dig < max:
        secmax= dig
    temp//=10
secmax = max if count>1 else secmax
max_num = max*10+secmax

print("\nHighest 2-digit number formed from",num,":",max_num,"\n")
        