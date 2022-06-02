import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

def isFibonacci(num):
    a, b, ssum = 1, 1, 0
    if num==0 or num==1:
        return True
    else:
        while ssum<num:
            ssum = a + b
            a, b = b, ssum
        return ssum == num

start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

print("\nComposite non-fibonacci numbers from", start,"to", end,":\n")
for i in range(start, end+1):
    if not isPrime(i) and not isFibonacci(i):
        print(i," ", end="")
print()
