import os
os.system("cls")

def reverseSum(num):
    rev = 0
    while num>0:
        rev = rev*10+num%10
        num//=10
    return rev

palin, rev = 0, 0
print("To covert an integer to its palindrome:")
temp = num = int(input("Enter an integer: "))

while(rev != temp):
     temp+=rev
     rev = reverseSum(temp)

print("\nThe Palindrome of", num, "is:", temp,"\n")
