import os
os.system("cls")

def tobinary(n):
    return 0 if n==0 else n%2+10*tobinary(n//2)

def tooctal(n): 
    return 0 if n==0 else n%8+10*tooctal(n//8)

def tohexadecimal(n):
    return "" if n==0 else tohexadecimal(n//16)+(chr(48+n%16) if n%16<10 else chr(55+n%16))

print("To convert a given decimal number to Binary, Octal and Hexadecimal system:")
n = int(input("Enter a number: "))

print("\n",n," in Binary: ", tobinary(n),
    "\n",n," in Octal: ", tooctal(n),
    "\n",n," in Hexadecimal: ", tohexadecimal(n),"\n", sep='')