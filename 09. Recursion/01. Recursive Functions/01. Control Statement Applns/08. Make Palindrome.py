import os
os.system("cls")

def reverse(n): 
    global rev
    if n>0:
        dig = n%10
        rev = rev*10+dig
        reverse(n//10)
    return rev

def makepalindrome(n):
    global rev
    rev = 0
    rev = reverse(n)
    return n if rev==n else makepalindrome(rev+n)
        
rev = 0
print("To make a number Palindrome:")
n = int(input("Enter a number: "))

print("\nThe palindrome of ",n,": ", makepalindrome(n),"\n",sep='')